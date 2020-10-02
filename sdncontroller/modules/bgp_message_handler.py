def find_node_id_from_update(update):
    """Returns node_id based on a raw exabgp update"""
    common_updates = ["bgpls-node", "bgpls-prefix-v4", "bgpls-prefix-v6"]
    if any(x in str(update) for x in common_updates):
        #bgpls-node, bgpls-prefix-v4 and bpls-prefix-v6 all have the same TLV/Attributes
        peer_ip = update["neighbor"]["address"]["peer"]
        peer_bgpls_info = update["neighbor"]["message"]["update"]["announce"]["bgp-ls bgp-ls"][peer_ip][0]
        node_id = "{}:{}".format(
            peer_bgpls_info["l3-routing-topology"],
            peer_bgpls_info["node-descriptors"]["router-id"]
        )
    
        return node_id

    if "bgpls-link" in str(update):
        #bgpls-link update
        peer_ip = update["neighbor"]["address"]["peer"]
        peer_bgpls_info = update["neighbor"]["message"]["update"]["announce"]["bgp-ls bgp-ls"][peer_ip][0]
        node_id = "{}:{}".format(
            peer_bgpls_info["l3-routing-topology"],
            peer_bgpls_info["local-node-descriptors"]["router-id"]
        )

        return node_id

def find_node_id_from_link(link):
    """Returns node_id based on BGP-LS Link NLRI"""
    if link["ls-nlri-type"] == "bgpls-link":
        node_id = "{}:{}".format(
            link["l3-routing-topology"],
            link["local-node-descriptors"]["router-id"]
        )

        return node_id

def find_node_id_from_prefix(prefix):
    """Returns node_id based on BGP-LS Prefix NLRI"""
    if prefix["ls-nlri-type"] == "bgpls-prefix-v4":
        node_id = "{}:{}".format(
            prefix["l3-routing-topology"],
            prefix["node-descriptors"]["router-id"]
        )

        return node_id

def create_bgp_state(update):
    """Prepares a dict from a raw BGP State Message to be used in the database"""
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

def create_bgpls_node(update):
    """Prepares a dict from a raw BGPLSNode NLRI Update to be used in the database"""
    peer_ip = update["neighbor"]["address"]["peer"]
    peer_bgpls_info = update["neighbor"]["message"]["update"]["announce"]["bgp-ls bgp-ls"][peer_ip][0]
    peer_attribute_info = update["neighbor"]["message"]["update"]["attribute"]

    node_data = {
        "node_id": find_node_id_from_update(update),
        "l3_nlri_type": peer_bgpls_info["ls-nlri-type"],
        "l3_routing_topology": peer_bgpls_info["l3-routing-topology"],
        "protocol_id": peer_bgpls_info["protocol-id"],
        "router_id": peer_bgpls_info["node-descriptors"]["router-id"],
        "nexthop": peer_bgpls_info["nexthop"],
        "origin": peer_attribute_info["origin"],
        "local_preference": peer_attribute_info["local-preference"],
        "igp_area_id": peer_attribute_info["bgp-ls"]["area-id"]
    }

    if "autonomous-system" in peer_bgpls_info["node-descriptors"]:
        node_data["asn"] = peer_bgpls_info["node-descriptors"]["autonomous-system"]

    if "bgp-ls-identifier" in peer_bgpls_info["node-descriptors"]:
        node_data["bgp_ls_id"] = peer_bgpls_info["node-descriptors"]["bgp-ls-identifier"]

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

def create_bgpls_link(update):
    """Prepares a dict from a raw BGPLSLink NLRI Update to be used in the database"""
    peer_ip = update["neighbor"]["address"]["peer"]
    peer_bgpls_info = update["neighbor"]["message"]["update"]["announce"]["bgp-ls bgp-ls"][peer_ip][0]
    peer_attribute_info = update["neighbor"]["message"]["update"]["attribute"]

    attribute_params = {
        "te-metric": "te_metric",
        "igp-metric": "igp_metric",
        "maximum-link-bandwidth":"maximum_link_bandwidth",
        "maximum-reservable-link-bandwidth": "maximum_reservable_bandwidth",
        "unreserved-bandwidth": "unreserved_bandwidth",
        "admin-group-mask": "admin_group_mask",
        "local-te-router-ids": "local_te_router_ids",
        "remote-te-router-id": "peer_te_router_ids",
        "sr-adj-weight": "sr_adj_weight"
    }

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
        "local_preference": peer_attribute_info["local-preference"]
    }

    link_data.update(param_mapper(attribute_params, **peer_attribute_info["bgp-ls"]))

    if "sr-adj-flags" in peer_attribute_info["bgp-ls"]:
        flag_string = ""
        flags = peer_attribute_info["bgp-ls"]["sr-adj-flags"]
        for key,value in flags.items():
            flag_string += "{}:{};".format(key, value)
        
        link_data["sr_adj_flags"] = flag_string

    if "sids" in peer_attribute_info["bgp-ls"]:
        link_data["sr_sids"] = peer_attribute_info["bgp-ls"]["sids"][0]

    return link_data

def create_bgpls_prefix_v4(update):
    """Prepares a dict from a raw BGPLSPrefixV4 NLRI Update to be used in the database"""
    peer_ip = update["neighbor"]["address"]["peer"]
    peer_attribute_info = update["neighbor"]["message"]["update"]["attribute"]
    prefixes = []

    for prefix in update["neighbor"]["message"]["update"]["announce"]["bgp-ls bgp-ls"][peer_ip]:
        prefix_data = {
            "node_id": find_node_id_from_prefix(prefix),
            "l3_nlri_type": prefix["ls-nlri-type"],
            "l3_routing_topology": prefix["l3-routing-topology"],
            "protocol_id": prefix["protocol-id"],
            "local_router_id": prefix["node-descriptors"]["router-id"],
            "ip_reachability_tlv": prefix["ip-reachability-tlv"],
            "ip_reachability_prefix": prefix["ip-reach-prefix"],
            "nexthop": prefix["nexthop"],
            "origin": peer_attribute_info["origin"],
            "local_preference": peer_attribute_info["local-preference"]
        }

        if "autonomous-system" in prefix["node-descriptors"]:
            prefix_data["local_asn"] = prefix["node-descriptors"]["autonomous-system"]

        if "bgp-ls-identifier" in prefix["node-descriptors"]:
            prefix_data["local_bgp_ls_id"] = prefix["node-descriptors"]["bgp-ls-identifier"]

        if "sr-prefix-flags" in peer_attribute_info["bgp-ls"]:
            flag_string = ""
            flags = peer_attribute_info["bgp-ls"]["sr-prefix-flags"]
            for key,value in flags.items():
                flag_string += "{}:{};".format(key, value)
            
            prefix_data["sr_prefix_flags"] = flag_string

        if "sids" in peer_attribute_info["bgp-ls"]:
            prefix_data["sr_sids"] = peer_attribute_info["bgp-ls"]["sids"]

        if "sr-prefix-attribute-flags" in peer_attribute_info["bgp-ls"]:
            flag_string = ""
            flags = peer_attribute_info["bgp-ls"]["sr-prefix-attribute-flags"]
            for key,value in flags.items():
                flag_string += "{}:{};".format(key, value)

            prefix_data["sr_prefix_attribute_flags"] = flag_string

        if "sr-algorithm" in peer_attribute_info["bgp-ls"]:
            prefix_data["sr_algorithm"] = peer_attribute_info["bgp-ls"]["sr-algorithm"]


        if "prefix-metric" in peer_attribute_info["bgp-ls"]:
            prefix_data["prefix_metric"] = peer_attribute_info["bgp-ls"]["prefix-metric"]

        prefixes.append(prefix_data)

    return prefixes

def create_bgpls_prefix_v6(update, update_type):
    """Prepares a dict from a raw BGPLSPrefixV6 NLRI Update to be used in the database"""
    # Not implemented yet
    return {
    }

def create_bgpls_withdraw(update):
    """Prepares a generic dict from any withdraw update and formats it to make database queries easier"""
    withdraw = {"nodes": [], "links": [], "prefixes_v4": [], "prefixes_v6": []}
    for entry in update["neighbor"]["message"]["update"]["withdraw"]["bgp-ls bgp-ls"]:
        if entry["ls-nlri-type"] == "bgpls-node":
            pass
        if entry["ls-nlri-type"] == "bgpls-link":
            withdraw["links"].append(create_bgpls_link_withdraw(entry))
        if entry["ls-nlri-type"] == "bgpls-prefix-v4":
            withdraw["prefixes_v4"].append(create_bgpls_prefix_v4_withdraw(entry))
        if entry["ls-nlri-type"] == "bgpls-prefix-v6":
            pass
    return withdraw

def create_bgpls_node_withdraw(nlri):
    """Prepares a more generic dict from a BGPLSNode NLRI Update"""
    pass

def create_bgpls_link_withdraw(nlri):
    """Prepares a more generic dict from a BGPLSLink NLRI Update"""
    return {
        "node_id": find_node_id_from_link(nlri),
        "ls_nlri_type": nlri["ls-nlri-type"],
        "l3_routing_topology": nlri["l3-routing-topology"],
        "protocol_id": nlri["protocol-id"],
        "local_asn": nlri["local-node-descriptors"]["autonomous-system"],
        "local_bgp_ls_id": nlri["local-node-descriptors"]["bgp-ls-identifier"],
        "local_router_id": nlri["local-node-descriptors"]["router-id"],
        "peer_asn": nlri["remote-node-descriptors"]["autonomous-system"],
        "peer_bgp_ls_id": nlri["remote-node-descriptors"]["bgp-ls-identifier"],
        "peer_router_id": nlri["remote-node-descriptors"]["router-id"],
        "local_interface_address": nlri["interface-address"]["interface-address"],
        "peer_interface_address": nlri["neighbor-address"]["neighbor-address"],
    }

def create_bgpls_prefix_v4_withdraw(nlri):
    """Prepares a more generic dict from a BGPLSPrefixV4 NLRI Update"""
    return {
        "node_id": find_node_id_from_prefix(nlri),
        "ls_nlri_type": nlri["ls-nlri-type"],
        "l3_routing_topology": nlri["l3-routing-topology"],
        "protocol_id": nlri["protocol-id"],
        "local_asn": nlri["node-descriptors"]["autonomous-system"],
        "local_bgp_ls_id": nlri["node-descriptors"]["bgp-ls-identifier"],
        "local_router_id": nlri["node-descriptors"]["router-id"],
        "ip_reachability_tlv": nlri["ip-reachability-tlv"],
        "ip_reachability_prefix": nlri["ip-reach-prefix"],
        "nexthop": nlri["nexthop"]
    }

def param_mapper(objmap=None, **kwargs):
    """Validates paramaters so we don't hardcode all the potential attributes that could appear in an update and throw an error"""
    params = {}
    for key, val in kwargs.items():
        if key in objmap:
            params[objmap[key]] = val
    return params
