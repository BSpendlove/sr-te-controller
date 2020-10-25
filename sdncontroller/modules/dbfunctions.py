from app import app, db
from models import (
    BGPNeighborship,
    BGPLSNode,
    BGPLSLink,
    BGPLSPrefixV4
)

def add_bgp_state(update):
    """Adds a BGP State"""
    neighborship = BGPNeighborship(**update)
    db.session.add(neighborship)
    db.session.commit()
    return neighborship

def get_bgp_state(id):
    """Returns a BGP State based on the database id"""
    neighborship = BGPNeighborship.query.filter_by(id=id).first()
    return neighborship

def get_bgp_states_all():
    """Returns all BGP States"""
    all_neighborships = BGPNeighborship.query.all()
    return all_neighborships

def delete_bgp_states_all():
    """Deletes all BGP States stored in the database"""
    all_neighborships = BGPNeighborship.query.delete()
    db.session.commit()
    return all_neighborships

def add_bgpls_node(update):
    """Adds a BGPLS Node"""
    if get_bgpls_node(update["node_id"]):
        node = update_bgpls_node(update)
        return node
    node = BGPLSNode(**update)
    db.session.add(node)
    db.session.commit()
    return node

def delete_bgpls_node(id):
    """Delete a BGPLS Node based on the database id"""
    return BGPLSNode.query.filter_by(id=id).delete()

def get_bgpls_node_id(id):
    return BGPLSNode.query.get(id)

def get_bgpls_node(node_id):
    """Returns a BGPLS Node based on node_id (not database id)"""
    node = BGPLSNode.query.filter_by(node_id=node_id).first()
    return node

def get_bgpls_nodes_all():
    """Returns all BGPLS Nodes"""
    all_nodes = BGPLSNode.query.all()
    return all_nodes

def delete_bgpls_nodes_all():
    """Deletes all BGPLS Nodes in the database"""
    nodes = BGPLSNode.query.delete()
    db.session.commit()
    return nodes

def update_bgpls_node(update):
    """Updates a BGPLS Node"""
    node = get_bgpls_node(update["node_id"])
    for key,value in update.items():
        setattr(node, key, value)
    db.session.commit()
    app.logger.debug("Updated Node in database...\n{}".format(node))
    return node

def get_bgpls_node_routerid_prefix(node_id):
    """Typically used to obtain the /32 route for the TE router address (eg. loopback)"""
    node = BGPLSNode.query.get(node_id)
    routerid_prefix = BGPLSPrefixV4.query.filter_by(
        l3_routing_topology=node.l3_routing_topology,
        ip_reachability_tlv=node.local_te_router_ids[0]
    ).first()
    return routerid_prefix

def add_bgpls_link(node, link):
    """Adds a BGPLS Link belonging to a node. If the node isn't already in the database, it will be created"""
    if not get_bgpls_node(node):
        node = add_bgpls_node({"node_id": node})
    else:
        node = get_bgpls_node(node)
    
    # Check if current link exists..
    #app.logger.debug("Trying to see if Link {} exist already...".format(link))
    check_link = BGPLSLink.query.filter_by(
        node_id=node.id,
        l3_routing_topology=link["l3_routing_topology"],
        local_router_id=link["local_router_id"],
        local_interface_address=link["local_interface_address"],
        peer_interface_address=link["peer_interface_address"]
    ).first()

    #app.logger.debug("check_link value is {}".format(check_link))
    if check_link:
        app.logger.debug("Link already exist {}".format(str(check_link)))
        # Temp solution atm...
        link["node_id"] = node.id
        for key,value in link.items():
            setattr(check_link, key, value)
        db.session.commit()
        app.logger.debug("Updated existing link {}".format(str(check_link)))
        return check_link

    new_link = BGPLSLink(**link)
    app.logger.debug("Attempting to add Link {} to node {}".format(new_link, node))
    node.bgpls_links.append(new_link)
    db.session.commit()
    return new_link

def check_bgpls_link(node, link):
    """Checks to see if link already exist in database, otherwise returns None"""
    if not get_bgpls_node(node):
        node = add_bgpls_node({"node_id": node})
    else:
        node = get_bgpls_node(node)

    check_link = BGPLSLink.query.filter_by(
        node_id=node.id,
        l3_routing_topology=link["l3_routing_topology"],
        local_router_id=link["local_router_id"],
        local_interface_address=link["local_interface_address"],
        peer_interface_address=link["peer_interface_address"]
    ).first()

    if not check_link:
        return None

    return check_link


def delete_bgpls_link(id):
    """Deleted a BGPLS Link based on the database id"""
    link = BGPLSLink.query.filter_by(id=id).delete()
    app.logger.debug("Deleted Link {} from database".format(link))
    db.session.commit()
    return link

def get_bgpls_link(id):
    """Returns a BGPLS Link based on the database id"""
    link = BGPLSLink.query.get(id)
    return link

def get_bgpls_link_remote_node(id):
    """Returns the remote node ID on a BGPLS Link (filtered by L3 Routing Domain and Local/Peer Interface Address"""
    link = BGPLSLink.query.get(id)
    app.logger.debug("Getting BGPLS LINK REMOTE NODE for LINK: {}".format(link))
    #app.logger.debug("get_bgpls_link_remote_node (link): {}".format(link))
    if not link:
        return None

    remote_link = BGPLSLink.query.filter_by(
        l3_routing_topology=link.l3_routing_topology,
        protocol_id=link.protocol_id,
        local_asn=link.peer_asn,
        local_bgp_ls_id=link.peer_bgp_ls_id,
        local_router_id=link.peer_router_id,
        local_interface_address=link.peer_interface_address,
        peer_interface_address=link.local_interface_address,
        #local_te_router_ids=link.peer_te_router_ids,
        #peer_te_router_ids=link.local_te_router_ids
    ).first()
    #app.logger.debug("get_bgpls_link_remote_node (remote_link): {}".format(remote_link))
    if not remote_link:
        return None

    return remote_link

def get_bgpls_links_all(node_id):
    """Returns all BGPLS Links that belong to a specific node"""
    links = BGPLSLink.query.filter_by(node_id=node_id)
    return links

def update_bgpls_link(update):
    """Updates a BGPLS Link"""
    link = get_bgpls_link(update["id"])
    for key,value in update.items():
        setattr(link, key, value)
    db.session.commit()
    app.logger.debug("Updated Link in database...\n{}".format(node))
    return link

def add_bgpls_prefix_v4(node, prefix):
    """Adds a BGPLS Prefix (V4) belonging to a node. If the node doesn't exist then it will be created automatically"""
    if not get_bgpls_node(node):
        node = add_bgpls_node({"node_id": node})
    else:
        node = get_bgpls_node(node)

    # Check if current prefix exists..
    #app.logger.debug("Trying to see if prefix {} exist already...".format(prefix))
    check_prefix = BGPLSPrefixV4.query.filter_by(
        node_id=node.id,
        l3_routing_topology=prefix["l3_routing_topology"],
        local_router_id=prefix["local_router_id"],
        ip_reachability_tlv=prefix["ip_reachability_tlv"],
        ip_reachability_prefix=prefix["ip_reachability_prefix"]
    ).first()

    #app.logger.debug("check_prefix value is {}".format(check_prefix))
    if check_prefix:
        #app.logger.debug("Prefix already exist {}".format(str(check_prefix)))
        prefix["node_id"] = node.id
        for key,value in prefix.items():
            setattr(check_prefix, key, value)
            db.session.commit()
            app.logger.debug("Updated existing prefix {}".format(str(check_prefix)))
            return check_prefix
    new_prefix = BGPLSPrefixV4(**prefix)
    #app.logger.debug("Attempting to add Prefix {} to node {}".format(vars(new_prefix), node))
    node.bgpls_prefixes.append(new_prefix)
    db.session.commit()
    return new_prefix

def check_bgpls_prefix_v4(node, prefix):
    """Checks to see if v4 Prefix already exist in database, otherwise return None"""
    if not get_bgpls_node(node):
        node = add_bgpls_node({"node_id": node})
    else:
        node = get_bgpls_node(node)

    check_prefix = BGPLSPrefixV4.query.filter_by(
        node_id=node.id,
        l3_routing_topology=prefix["l3_routing_topology"],
        local_router_id=prefix["local_router_id"],
        ip_reachability_tlv=prefix["ip_reachability_tlv"],
        ip_reachability_prefix=prefix["ip_reachability_prefix"]
    ).first()

    if not check_prefix:
        return None

    return check_prefix

def add_bgpls_prefix_v6(node, prefix):
    """Adds a BGPLS Prefix (V6)"""
    # Not fully implemented yet...
    if not get_bgpls_node(node):
        node = add_bgpls_node({"node_id": node})
    else:
        node = get_bgpls_node(node)

    return None

def delete_bgpls_prefix_v4(id):
    """Deletes a BGPLS Prefix (V4)"""
    prefix = BGPLSPrefixV4.query.filter_by(id=id).delete()
    app.logger.debug("Deleted PrefixV4 from database".format(prefix))
    db.session.commit()
    return prefix

def get_bgpls_prefix_v4(id):
    """Returns a BGPLS Prefix (V4) based on database id"""
    prefix = BGPLSPrefixV4.query.get(id)
    return prefix

def get_bgpls_prefixes_v4_all(node_id):
    """Returns all BGPLS Prefixes V4) that belong to a specific node"""
    prefixes = BGPLSPrefixV4.query.filter_by(node_id=node_id)
    return prefixes
