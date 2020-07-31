def find_node_id_from_link_update(update):
    peer_ip = update["neighbor"]["address"]["peer"]
    peer_bgpls_info = update["neighbor"]["message"]["update"]["announce"]["bgp-ls bgp-ls"][peer_ip][0]
    node_id = "{}{}{}".format(
        peer_bgpls_info["local-node-descriptors"]["autonomous-system"],
        peer_bgpls_info["local-node-descriptors"]["bgp-ls-identifier"],
        peer_bgpls_info["local-node-descriptors"]["router-id"]
    )
    return node_id

def find_node_id_from_node_update(update):
    peer_ip = update["neighbor"]["address"]["peer"]
    peer_bgpls_info = update["neighbor"]["message"]["update"]["announce"]["bgp-ls bgp-ls"][peer_ip][0]
    node_id = "{}{}{}".format(
        peer_bgpls_info["node-descriptors"]["autonomous-system"],
        peer_bgpls_info["node-descriptors"]["bgp-ls-identifier"],
        peer_bgpls_info["node-descriptors"]["router-id"]
    )
    return node_id

def create_bgp_state(update):
    return {
        "exabgp_version": update["exabgp"],
        "time": update["time"],
        "host": update["host"],
        "pid": update["pid"],
        "ppid": update["ppid"],
        "counter": update["counter"],
        "local_address": update["neighbor"]["address"]["local"],
        "peer_address": update["neighbor"]["address"]["peer"],
        "local_asn": update["neighbor"]["asn"]["local"],
        "peer_asn": update["neighbor"]["asn"]["peer"],
        "state_type": update["neighbor"]["state"]
    }

def create_bgp_node(update):
    peer_ip = update["neighbor"]["address"]["peer"]
    peer_bgpls_info = update["neighbor"]["message"]["update"]["announce"]["bgp-ls bgp-ls"][peer_ip][0]
    peer_attribute_info = update["neighbor"]["message"]["update"]["attribute"]
    node_id = "{}{}{}".format(
        peer_bgpls_info["node-descriptors"]["autonomous-system"],
        peer_bgpls_info["node-descriptors"]["bgp-ls-identifier"],
        peer_bgpls_info["node-descriptors"]["router-id"]
    )

    node_data = {
        "node_id": node_id,
        "l3_nlri_type": peer_bgpls_info["ls-nlri-type"],
        "l3_routing_topology": peer_bgpls_info["l3-routing-topology"],
        "protocol_id": peer_bgpls_info["protocol-id"],
        "asn": peer_bgpls_info["node-descriptors"]["autonomous-system"],
        "bgp_ls_id": peer_bgpls_info["node-descriptors"]["bgp-ls-identifier"],
        "router_id": peer_bgpls_info["node-descriptors"]["router-id"],
        "nexthop": peer_bgpls_info["nexthop"],
        "origin": peer_attribute_info["origin"],
        "local_preference": peer_attribute_info["local-preference"],
        "igp_area_id": peer_attribute_info["bgp-ls"]["area-id"]
    }

    if "local-te-router-ids" in peer_attribute_info["bgp-ls"]:
        node_data["local_te_router_ids"] = str(peer_attribute_info["bgp-ls"]["local-te-router-ids"])

    if "sr-capability-flags" in peer_attribute_info["bgp-ls"]:
        ivrsv = "{}/{}/{}".format(
                peer_attribute_info["bgp-ls"]["sr-capability-flags"]["I"],
                peer_attribute_info["bgp-ls"]["sr-capability-flags"]["V"],
                peer_attribute_info["bgp-ls"]["sr-capability-flags"]["RSV"],
        )
        node_data["sr_capability_flags"] = ivrsv

    if "sids" in peer_attribute_info["bgp-ls"]:
        node_data["sr_sids"] =  str(peer_attribute_info["bgp-ls"]["sids"])

    return node_data

def create_bgp_link(update):
    peer_ip = update["neighbor"]["address"]["peer"]
    peer_bgpls_info = update["neighbor"]["message"]["update"]["announce"]["bgp-ls bgp-ls"][peer_ip][0]
    peer_attribute_info = update["neighbor"]["message"]["update"]["attribute"]
    node_id = "{}{}{}".format(
        peer_bgpls_info["local-node-descriptors"]["autonomous-system"],
        peer_bgpls_info["local-node-descriptors"]["bgp-ls-identifier"],
        peer_bgpls_info["local-node-descriptors"]["router-id"]
    )
    return {
        "node_id": node_id,
        "l3_nlri_type": peer_bgpls_info["ls-nlri-type"],
        "l3_routing_topology": peer_bgpls_info["l3-routing-topology"],
        "protocol_id": peer_bgpls_info["protocol-id"],
        "local_asn": peer_bgpls_info["local-node-descriptors"]["autonomous-system"],
        "local_bgp_ls_id": peer_bgpls_info["local-node-descriptors"]["bgp-ls-identifier"],
        "local_router_id": peer_bgpls_info["local-node-descriptors"]["router-id"],
        "peer_asn": peer_bgpls_info["remote-node-descriptors"]["autonomous-system"],
        "peer_bgp_ls_id": peer_bgpls_info["remote-node-descriptors"]["bgp-ls-identifier"],
        "peer_router_id": peer_bgpls_info["remote-node-descriptors"]["router-id"],
        "local_interface_address": peer_bgpls_info["interface-address"]["interface-address"],
        "peer_interface_address": peer_bgpls_info["neighbor-address"]["neighbor-address"],
        "origin": peer_attribute_info["origin"],
        "local_preference": peer_attribute_info["local-preference"],
        "local_te_router_ids": str(peer_attribute_info["bgp-ls"]["local-te-router-ids"]),
        "peer_te_router_ids": peer_attribute_info["bgp-ls"]["remote-te-router-id"],
        "admin_group_mask": str(peer_attribute_info["bgp-ls"]["admin-group-mask"]),
        "maximum_link_bandwidth": peer_attribute_info["bgp-ls"]["maximum-link-bandwidth"],
        "maximum_reservable_bandwidth": peer_attribute_info["bgp-ls"]["maximum-reservable-link-bandwidth"],
        "unreserved_bandwidth": str(peer_attribute_info["bgp-ls"]["unreserved-bandwidth"]),
        "te_metric": peer_attribute_info["bgp-ls"]["te-metric"],
        "igp_metric": peer_attribute_info["bgp-ls"]["igp-metric"]
    }

def create_bgp_prefix_v4(update):
    # Not implemented yet
    return {

    }

def create_bgp_prefix_v6(update):
    # Not implemented yet
    return {

    }
