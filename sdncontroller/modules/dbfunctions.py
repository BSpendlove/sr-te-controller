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
    neighborship = BGPNeighborship.query.filter_by(id).first()
    return neighborship

def get_bgp_states_all():
    all_neighborships = BGPNeighborship.query.all()
    return all_neighborships

def delete_bgp_states_all():
    all_neighborships = BGPNeighborship.query.delete()
    db.session.commit()
    return all_neighborships

def add_bgpls_node(update):
    node = BGPLSNode(**update)
    db.session.add(node)
    db.session.commit()
    return node

def delete_bgpls_node(id):
    return BGPLSNode.query.filter_by(id).delete()

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

def add_bgpls_link(node, link):
    if isinstance(node, str):
        node = get_bgpls_node(node_id=node)
    node.bgpls_links.append(link)
    db.session.commit()
    return link

def delete_bgpls_link(id):
    return BGPLSLink.query.filter_by(id=id).delete()

def get_bgpls_link(id):
    link = BGPLSLink.query.get(id)
    return link

def get_bgpls_links_all(node_id):
    links = BGPLSLink.query.filter_by(node_id=node_id)
    return links

def add_bgpls_prefix(node, prefix):
    note.bgpls_prefixes.append(prefix)
    db.session.commit()
    return prefix

def delete_bgpls_prefix(id):
    return BGPLSPrefixV4.query.filter_by(id).delete()

def get_bgpls_prefix(id):
    prefix = BGPLSPrefixV4.query.get(id)
    return prefix

def get_bgpls_prefixes_all(node_id):
    prefixes = BGPLSPrefixV4.query.filter_by(node_id=node_id)
    return prefixes
