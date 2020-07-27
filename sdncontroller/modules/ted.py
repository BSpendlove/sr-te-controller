from app import app
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
        app.logger.debug("Found node ({})".format(node_id))
        for entry_link in links:
            link_descriptor = entry_link["link"]["local-node-descriptors"]
            link_node_id = "{}{}{}".format(link_descriptor["autonomous-system"], link_descriptor["bgp-ls-identifier"], link_descriptor["router-id"])
            if link_node_id == entry_node["node"]:
                entry_node["links"].append(entry_link)
        for entry_prefix in prefixes:
            prefix_descriptor = entry_prefix["prefix"]["node-descriptors"]
            prefix_node_id = "{}{}{}".format(prefix_descriptor["autonomous-system"], prefix_descriptor["bgp-ls-identifier"], prefix_descriptor["router-id"])
            if prefix_node_id == entry_node["node"]:
                entry_node["prefixes"].append(entry_prefix)
        full_topology.append(entry_node)
    return full_topology
