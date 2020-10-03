from app import app
from modules import dbfunctions
import time
import json

### Work in progress - These functions don't work correctly/or won't work at all
def validate_same_neighbor(topology):
    first_update_host = topology[0]["host"] #Check first input on host
    first_update_neighbor_local = topology[0]["neighbor"]["address"]["local"] #Check first input on neighbor address local
    first_update_neighbor_remote = topology[0]["neighbor"]["address"]["peer"] #Check first input on neighbor address remote

    #Top 3 should always match in the topology - However needs to rewritten for more than 1 neighbor to the API...
    for update in topology:
        if not update["host"] == first_update_host:
            return False
        if not update["neighbor"]["address"]["local"] == first_update_neighbor_local:
            return False
        if not update["neighbor"]["address"]["peer"] == first_update_neighbor_remote:
            return False

    return True

def build_ted(topology):
    nodes = []
    links = []
    prefixes = []

    if validate_same_neighbor(topology):
        for update in topology:
            peer_ip = update["neighbor"]["address"]["peer"]
            if "eor" in str(update["neighbor"]["message"]):
                break
            for announcement in update["neighbor"]["message"]["update"]["announce"]["bgp-ls bgp-ls"][peer_ip]:
                if "bgpls-node" == announcement["ls-nlri-type"]:
                    node_descriptor = announcement["node-descriptors"]
                    app.logger.debug("Node descriptor is {}".format(node_descriptor))
                    node_id = "{}{}{}".format(node_descriptor["autonomous-system"], node_descriptor["bgp-ls-identifier"], node_descriptor["router-id"])
                    # I am generating a node_id because this should be unique in the whole network, using the AS + BGPLS ID + BGP RID I think will guarantee
                    node = {"node_id": node_id,
                            "node_details": announcement,
                            "node_attributes": update["neighbor"]["message"]["update"]["attribute"],
                            "links": [],
                            "prefixes": []}
                    nodes.append(node)
                if "bgpls-link" == announcement["ls-nlri-type"]:
                    link = {"link": announcement, "link_attributes": update["neighbor"]["message"]["update"]["attribute"]}
                    links.append(link)
                if "bgpls-prefix-v4" == announcement["ls-nlri-type"]:
                    prefix = {"prefix": announcement, "prefix_attributes": update["neighbor"]["message"]["update"]["attribute"]}
                    prefixes.append(prefix)

    full_topology = []

    for entry_node in nodes:
        entry_node["links"] = []
        entry_node["prefixes"] = []
        #node_descriptor = entry_node["node_details"]["node-descriptors"]
        #node_id = "{}{}{}".format(node_descriptor["autonomous-system"], node_descriptor["bgp-ls-identifier"], node_descriptor["router-id"])
        #app.logger.debug("Found node ({})".format(node_id))
        for entry_link in links:
            link_descriptor = entry_link["link"]["local-node-descriptors"]
            link_node_id = "{}{}{}".format(link_descriptor["autonomous-system"], link_descriptor["bgp-ls-identifier"], link_descriptor["router-id"])
            if link_node_id == entry_node["node_id"]:
                entry_node["links"].append(entry_link)
        for entry_prefix in prefixes:
            prefix_descriptor = entry_prefix["prefix"]["node-descriptors"]
            prefix_node_id = "{}{}{}".format(prefix_descriptor["autonomous-system"], prefix_descriptor["bgp-ls-identifier"], prefix_descriptor["router-id"])
            if prefix_node_id == entry_node["node_id"]:
                entry_node["prefixes"].append(entry_prefix)
        full_topology.append(entry_node)
    return full_topology

def modify_ted(topology):
    return None

def build_visual_ted(topology):
    """ function is based on topology generated via database models """
    nodes = []
    edges = []
    node_placeholders = []
    for node in topology:
        node_sid = str(int(node.sr_sids[-1]) + int(dbfunctions.get_bgpls_node_routerid_prefix(node.id).sr_sids[-1]))
        node_data = {
            "id": node.id,
            "label": node.local_te_router_ids[0],
            "title": "SID Labels: {}".format(node_sid),
            "sr_labels": node_sid
        }
        app.logger.debug(json.dumps(node_data, indent=4))
        nodes.append(node_data)

        for link in node.bgpls_links:
            remote_link = dbfunctions.get_bgpls_link_remote_node(link.id)
            if not remote_link:
                continue
            node_placeholder = {
                "id": "N{}L{}-N{}L{}".format(node.id, link.id, remote_link.node_id, remote_link.id)
            }

            if "N{}L{}-N{}L{}".format(remote_link.node_id, remote_link.id, node.id, link.id) in node_placeholders:
                link_data = {
                    "from": node.id,
                    "to": "N{}L{}-N{}L{}".format(remote_link.node_id, remote_link.id, node.id, link.id),
                    "label": link.sr_sids[0] if link.sr_sids else None,
                    "font": {"align": "middle"},
                    "title": "Label: {}<br>IP Address: {}<br>TE Metric: {}<br>IGP Metric: {}".format(link.sr_sids[0] if link.sr_sids else None, link.local_interface_address, link.te_metric, link.igp_metric)
                }
                edges.append(link_data)
            else:
                node_placeholders.append("N{}L{}-N{}L{}".format(node.id, link.id, remote_link.node_id, remote_link.id))
                link_data = {
                    "from": node.id,
                    "to": "N{}L{}-N{}L{}".format(node.id, link.id, remote_link.node_id, remote_link.id),
                    "label": link.sr_sids[0] if link.sr_sids else None,
                    "font": {"align": "middle"},
                    "title": "Label: {}<br>IP Address: {}<br>TE Metric: {}<br>IGP Metric: {}".format(link.sr_sids[0] if link.sr_sids else None, link.local_interface_address, link.te_metric, link.igp_metric)
                }
                edges.append(link_data)
            #app.logger.debug("Local Link: {} (Node: {})\nRemote Link: {} (Node: {})".format(link.id, link.node_id, remote_link.id, remote_link.node_id))

    for node_placeholder in node_placeholders:
        nodes.append({"id": node_placeholder, "hidden": True})

    vis_js_topology = {"nodes": nodes, "edges": edges}
    return vis_js_topology

def generate_ted_id(update):
    initial_id = "{}{}{}{}".format(
        update["neighbor"]["asn"]["local"],
        update["neighbor"]["address"]["local"],
        update["neighbor"]["asn"]["peer"],
        update["neighbor"]["address"]["peer"]
    )

    return initial_id.replace(".","")
