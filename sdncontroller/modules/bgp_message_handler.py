def find_node_id_from_update(update):
    common_updates = ["bgpls-node", "bgpls-prefix-v4", "bgpls-prefix-v6"]
    if any(x in str(update) for x in common_updates):
        #bgpls-node, bgpls-prefix-v4 and bpls-prefix-v6 all have the same TLV/Attributes
        peer_ip = update["neighbor"]["address"]["peer"]
        peer_bgpls_info = update["neighbor"]["message"]["update"]["announce"]["bgp-ls bgp-ls"][peer_ip][0]
        node_id = "{}{}{}".format(
            peer_bgpls_info["node-descriptors"]["autonomous-system"],
            peer_bgpls_info["node-descriptors"]["bgp-ls-identifier"],
            peer_bgpls_info["node-descriptors"]["router-id"]
        )
    
        return node_id

    if "bgpls-link" in str(update):
        #bgpls-link update
        peer_ip = update["neighbor"]["address"]["peer"]
        peer_bgpls_info = update["neighbor"]["message"]["update"]["announce"]["bgp-ls bgp-ls"][peer_ip][0]
        node_id = "{}{}{}".format(
            peer_bgpls_info["local-node-descriptors"]["autonomous-system"],
            peer_bgpls_info["local-node-descriptors"]["bgp-ls-identifier"],
            peer_bgpls_info["local-node-descriptors"]["router-id"]
        )

        return node_id

def find_node_id_from_prefix(prefix):
    if prefix["ls-nlri-type"] == "bgpls-prefix-v4":
        node_id = "{}{}{}".format(
            prefix["node-descriptors"]["autonomous-system"],
            prefix["node-descriptors"]["bgp-ls-identifier"],
            prefix["node-descriptors"]["router-id"]
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
    node_data = {
        "node_id": find_node_id_from_update(update),
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
        node_data["local_te_router_ids"] = peer_attribute_info["bgp-ls"]["local-te-router-ids"]

    if "sr-capability-flags" in peer_attribute_info["bgp-ls"]:
        flags = peer_attribute_info["bgp-ls"]["sr-capability-flags"]
        flag_string = ""
        for key,value in flags.items():
            flag_string += "{}:{};".format(key, value)

        node_data["sr_capability_flags"] = flag_string

    if "sids" in peer_attribute_info["bgp-ls"]:
        node_data["sr_sids"] =  peer_attribute_info["bgp-ls"]["sids"][0]

    return node_data

def create_bgp_link(update):
    peer_ip = update["neighbor"]["address"]["peer"]
    peer_bgpls_info = update["neighbor"]["message"]["update"]["announce"]["bgp-ls bgp-ls"][peer_ip][0]
    peer_attribute_info = update["neighbor"]["message"]["update"]["attribute"]
    link_data = {
        "node_id": find_node_id_from_update(update),
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
        "admin_group_mask": peer_attribute_info["bgp-ls"]["admin-group-mask"],
        "maximum_link_bandwidth": peer_attribute_info["bgp-ls"]["maximum-link-bandwidth"],
        "maximum_reservable_bandwidth": peer_attribute_info["bgp-ls"]["maximum-reservable-link-bandwidth"],
        "unreserved_bandwidth": peer_attribute_info["bgp-ls"]["unreserved-bandwidth"],
        "te_metric": peer_attribute_info["bgp-ls"]["te-metric"],
        "igp_metric": peer_attribute_info["bgp-ls"]["igp-metric"]
    }

    if "local-te-router-ids" in peer_attribute_info["bgp-ls"]:
        link_data["local_te_router_ids"] = peer_attribute_info["bgp-ls"]["local-te-router-ids"]

    if "peer-te-router-ids" in peer_attribute_info["bgp-ls"]:
        link_data["peer_te_router_ids"] = peer_attribute_info["bgp-ls"]["remote-te-router-id"]

    if "sr-adj-flags" in peer_attribute_info["bgp-ls"]:
        flag_string = ""
        flags = peer_attribute_info["bgp-ls"]["sr-adj-flags"]
        for key,value in flags.items():
            flag_string += "{}:{};".format(key, value)
        
        link_data["sr_adj_flags"] = flag_string

    if "sids" in peer_attribute_info["bgp-ls"]:
        link_data["sr_sids"] = peer_attribute_info["bgp-ls"]["sids"][0]

    if "sr-adj-weight" in peer_attribute_info["bgp-ls"]:
        link_data["sr_adj_weight"] = peer_attribute_info["bgp-ls"]["sr-adj-weight"]

    return link_data

def create_bgp_prefix_v4(update):
    peer_ip = update["neighbor"]["address"]["peer"]
    peer_attribute_info = update["neighbor"]["message"]["update"]["attribute"]
    prefixes = []
    for prefix in update["neighbor"]["message"]["update"]["announce"]["bgp-ls bgp-ls"][peer_ip]:
        prefix_data = {
            "node_id": find_node_id_from_prefix(prefix),
            "l3_nlri_type": prefix["ls-nlri-type"],
            "l3_routing_topology": prefix["l3-routing-topology"],
            "protocol_id": prefix["protocol-id"],
            "local_asn": prefix["node-descriptors"]["autonomous-system"],
            "local_bgp_ls_id": prefix["node-descriptors"]["bgp-ls-identifier"],
            "local_router_id": prefix["node-descriptors"]["router-id"],
            "ip_reachability_tlv": prefix["ip-reachability-tlv"],
            "ip_reachability_prefix": prefix["ip-reach-prefix"],
            "nexthop": prefix["nexthop"],
            "origin": peer_attribute_info["origin"],
            "local_preference": peer_attribute_info["local-preference"],
            "prefix_metric": peer_attribute_info["bgp-ls"]["prefix-metric"]
        }

        if "sr-prefix-attribute-flags" in peer_attribute_info["bgp-ls"]:
            flag_string = ""
            flags = peer_attribute_info["bgp-ls"]["sr-prefix-attribute-flags"]
            for key,value in flags.items():
                flag_string += "{}:{};".format(key, value)
            
            prefix_data["sr_prefix_attribute_flags"] = flag_string

        prefixes.append(prefix_data)

    return prefixes

def create_bgp_prefix_v6(update):
    # Not implemented yet
    return {

    }
