from app import app
import time
import json

### Work in progress - These functions don't work correctly/or won't work at all

def build_ted(initial_topology):
    app.logger.debug("Initial TED is being built, current state: {} (type = {})".format(json.dumps(initial_topology, indent=4), type(initial_topology)))
    new_topology = validate_same_neighbor(initial_topology)
    if new_topology:
        for update in initial_topology:
            app.logger.debug("Per topology {}..\nType is {}".format(json.dumps(update, indent=4), type(update)))
            if "eor" in update["neighbor"]["message"]:
                return new_topology
            app.logger.debug("lsp: {}".format(json.dumps(update["neighbor"]["message"]["update"], indent=4)))
            for lsp in update["neighbor"]["message"]["bgp-ls"]["announce"]["bgp-ls bgp-ls"]:
                lsp.update({"attribute": update["neighbor"]["message"]["update"]["attribute"]})

    return new_topology

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

    return {"exabgp": topology[0]["exabgp"],
            "time": time.time(),
            "host": topology[0]["host"],
            "neighbors": []}
