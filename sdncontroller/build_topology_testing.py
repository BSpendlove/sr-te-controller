import time
import json
from example_topology import json_topology

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

def generate_json_topology(topology):
    nodes = []
    links = []
    prefixes = []

    if validate_same_neighbor(topology):
        for update in topology:
            peer_ip = update["neighbor"]["address"]["peer"]
            for announcement in update["neighbor"]["message"]["update"]["announce"]["bgp-ls bgp-ls"][peer_ip]:
                if "bgpls-node" == announcement["ls-nlri-type"]:
                    node = {"node": announcement, "node_attributes": update["neighbor"]["message"]["update"]["attribute"]}
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
        node_descriptor = entry_node["node"]["node-descriptors"]
        node_id = "{}{}{}".format(node_descriptor["autonomous-system"], node_descriptor["bgp-ls-identifier"], node_descriptor["router-id"])
        for entry_link in links:
            link_descriptor = entry_link["link"]["local-node-descriptors"]
            link_node_id = "{}{}{}".format(link_descriptor["autonomous-system"], link_descriptor["bgp-ls-identifier"], link_descriptor["router-id"])
            if link_node_id == node_id:
                entry_node["links"].append(entry_link)
        for entry_prefix in prefixes:
            prefix_descriptor = entry_prefix["prefix"]["node-descriptors"]
            prefix_node_id = "{}{}{}".format(prefix_descriptor["autonomous-system"], prefix_descriptor["bgp-ls-identifier"], prefix_descriptor["router-id"])
            if prefix_node_id == node_id:
                entry_node["prefixes"].append(entry_prefix)
        full_topology.append(entry_node)
    return full_topology

print(json.dumps(generate_json_topology(json_topology), indent=4))

"""
nodes = []
links = []
prefixes = []

if validate_same_neighbor(json_topology):
    for update in json_topology:
        peer_ip = update["neighbor"]["address"]["peer"]
        for announcement in update["neighbor"]["message"]["update"]["announce"]["bgp-ls bgp-ls"][peer_ip]:
            if "bgpls-node" == announcement["ls-nlri-type"]:
                node = {"node": announcement, "node_attributes": update["neighbor"]["message"]["update"]["attribute"]}
                nodes.append(node)
            if "bgpls-link" == announcement["ls-nlri-type"]:
                link = {"link": announcement, "link_attributes": update["neighbor"]["message"]["update"]["attribute"]}
                links.append(link)
            if "bgpls-prefix-v4" == announcement["ls-nlri-type"]:
                prefix = {"prefix": announcement, "prefix_attributes": update["neighbor"]["message"]["update"]["attribute"]}
                prefixes.append(prefix)
else:
    print("Can not validate TED topology...")

generated_topology = generate_json_topology(nodes, links, prefixes)
print(json.dumps(generated_topology, indent=4))

for entry_node in nodes:
    entry_node["links"] = []
    entry_node["prefixes"] = []
    node_descriptor = entry_node["node"]["node-descriptors"]
    node_id = "{}{}{}".format(node_descriptor["autonomous-system"], node_descriptor["bgp-ls-identifier"], node_descriptor["router-id"])
    for entry_link in links:
        link_descriptor = entry_link["link"]["local-node-descriptors"]
        link_node_id = "{}{}{}".format(link_descriptor["autonomous-system"], link_descriptor["bgp-ls-identifier"], link_descriptor["router-id"])
        if link_node_id == node_id:
            entry_node["links"].append(entry_link)
    for entry_prefix in prefixes:
        prefix_descriptor = entry_prefix["prefix"]["node-descriptors"]
        prefix_node_id = "{}{}{}".format(prefix_descriptor["autonomous-system"], prefix_descriptor["bgp-ls-identifier"], prefix_descriptor["router-id"])
        if prefix_node_id == node_id:
            entry_node["prefixes"].append(entry_prefix)
    full_topology.append(entry_node)

print(json.dumps(full_topology, indent=4))
print("Nodes:\n{}\n\nLinks:\n{}\n\nPrefixes:\n{}\n\n".format(
    json.dumps(nodes, indent=4),
    json.dumps(links, indent=4),
    json.dumps(prefixes, indent=4))
    )
"""
