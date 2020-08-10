from app import app, db
from models import (
    BGPNeighborship,
    BGPLSNode,
    BGPLSLink,
    BGPLSPrefixV4
)

def add_bgp_state(update):
    neighborship = BGPNeighborship(**update)
    db.session.add(neighborship)
    db.session.commit()
    return neighborship

def get_bgp_state(id):
    neighborship = BGPNeighborship.query.filter_by(id=id).first()
    return neighborship

def get_bgp_states_all():
    all_neighborships = BGPNeighborship.query.all()
    return all_neighborships

def delete_bgp_states_all():
    all_neighborships = BGPNeighborship.query.delete()
    db.session.commit()
    return all_neighborships

def add_bgpls_node(update):
    if get_bgpls_node(update["node_id"]):
        node = update_bgpls_node(update)
        return node
    node = BGPLSNode(**update)
    db.session.add(node)
    db.session.commit()
    return node

def delete_bgpls_node(id):
    return BGPLSNode.query.filter_by(id=id).delete()

def get_bgpls_node(node_id):
    node = BGPLSNode.query.filter_by(node_id=node_id).first()
    return node

def get_bgpls_nodes_all():
    all_nodes = BGPLSNode.query.all()
    return all_nodes

def delete_bgpls_nodes_all():
    nodes = BGPLSNode.query.delete()
    db.session.commit()
    return nodes

def update_bgpls_node(update):
    node = get_bgpls_node(update["node_id"])
    for key,value in update.items():
        setattr(node, key, value)
    db.session.commit()
    app.logger.debug("Updated Node in database...\n{}".format(node))
    return node

def get_bgpls_node_routerid_prefix(node_id):
    node = BGPLSNode.query.get(node_id)
    app.logger.debug(node.local_te_router_ids)
    routerid_prefix = BGPLSPrefixV4.query.filter_by(
        l3_routing_topology=node.l3_routing_topology,
        ip_reachability_tlv=node.local_te_router_ids[0]
    ).first()
    return routerid_prefix

def add_bgpls_link(node, link):
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
    link = BGPLSLink.query.filter_by(id=id).delete()
    app.logger.debug("Deleted Link {} from database".format(link))
    db.session.commit()
    return link

def get_bgpls_link(id):
    link = BGPLSLink.query.get(id)
    return link

def get_bgpls_link_remote_node(id):
    link = BGPLSLink.query.get(id)
    #app.logger.debug("get_bgpls_link_remote_node (link): {}".format(link))
    if link:
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
        if remote_link:
            return remote_link.node_id
        else:
            return None
    return None

def get_bgpls_links_all(node_id):
    links = BGPLSLink.query.filter_by(node_id=node_id)
    return links

def update_bgpls_link(update):
    link = get_bgpls_link(update["id"])
    for key,value in update.items():
        setattr(link, key, value)
    db.session.commit()
    app.logger.debug("Updated Link in database...\n{}".format(node))
    return link

def add_bgpls_prefix_v4(node, prefix):
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
            #app.logger.debug("Updated existing prefix {}".format(str(check_prefix)))
    new_prefix = BGPLSPrefixV4(**prefix)
    #app.logger.debug("Attempting to add Prefix {} to node {}".format(vars(new_prefix), node))
    node.bgpls_prefixes.append(new_prefix)
    db.session.commit()
    return new_prefix

def check_bgpls_prefix_v4(node, prefix):
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
    # Not fully implemented yet...
    if not get_bgpls_node(node):
        node = add_bgpls_node({"node_id": node})
    else:
        node = get_bgpls_node(node)

    return None

def delete_bgpls_prefix_v4(id):
    prefix = BGPLSPrefixV4.query.filter_by(id=id).delete()
    app.logger.debug("Deleted PrefixV4 from database".format(prefix))
    db.session.commit()
    return prefix

def get_bgpls_prefix_v4(id):
    prefix = BGPLSPrefixV4.query.get(id)
    return prefix

def get_bgpls_prefixes_v4_all(node_id):
    prefixes = BGPLSPrefixV4.query.filter_by(node_id=node_id)
    return prefixes
