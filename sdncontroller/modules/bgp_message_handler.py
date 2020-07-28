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
    # Not implemented yet
    return {

    }

def create_bgp_link(update):
    # Not implemented yet
    return {

    }

def create_bgp_prefix_v4(update):
    # Not implemented yet
    return {

    }

def create_bgp_prefix_v6(update):
    # Not implemented yet
    return {

    }