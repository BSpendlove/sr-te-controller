from app import db
from dataclasses import dataclass
from modules.jsonencoder import JsonEncodedDict

class Neighbor(db.Model):
    """ BGP Neighbor Model """
    id = db.Column(db.Integer, primary_key=True)
    neighbor_data = db.Column(JsonEncodedDict)

    def __repr__(self):
        return '<ExaBGP Neighbor {}>'.format(self.id)

class TED(db.Model):
    """ TED Model """
    id = db.Column(db.String, primary_key=True) # Rest in peace... Currently using local AS + local IP + remote AS + remote IP to identify the unique TED
    ted = db.Column(JsonEncodedDict)

    def __repr__(self):
        return '<ExaBGP TED {}>'.format(self.id)

# Above classes are OLD classes not used anymore...

class BGPLS_Node(db.Model):
    """ Class representing a BGP LS Node Update """
    id = db.Column(db.Integer, primary_key=True)
    node_id = db.Column(db.String)
    l3_nlri_type = db.Column(db.String)
    l3_routing_topology = db.Column(db.Integer)
    protocol_id = db.Column(db.Integer)
    asn = db.Column(db.String)
    bgp_ls_id = db.Column(db.String)
    router_id = db.Column(db.String)
    origin = db.Column(db.String)
    local_preference = db.Column(db.String)
    igp_area_id = db.Column(db.String)
    local_te_router_ids = db.Column(db.String)
    bgpls_links = db.relationship('BGPLS_Link', backref='links', lazy='dynamic')
    bgpls_prefixes_v4 = db.relationship('BGPLS_Prefix_V4', backref = 'prefixes_v4', lazy='dynamic')

    def __repr__(self):
        return '<ExaBGP BGPLS Node {}>'.format(self.node_id)

class BGPLS_Link(db.Model):
    """ Class representing a BGP LS Link Update """
    id = db.Column(db.Integer, primary_key=True)
    node_id = db.Column(db.String, db.ForeignKey('links.id'))
    l3_nlri_type = db.Column(db.String)
    l3_routing_topology = db.Column(db.Integer)
    local_asn = db.Column(db.Integer)
    local_bgp_ls_id = db.Column(db.String)
    local_router_id = db.Column(db.String)
    peer_asn = db.Column(db.Integer)
    peer_bgp_ls_id = db.Column(db.String)
    peer_router_id = db.Column(db.String)
    local_interface_address = db.Column(db.String)
    peer_interface_address = db.Column(db.String)
    origin = db.Column(db.String)
    local_preference = db.Column(db.String)
    local_te_router_ids = db.Column(db.String)
    peer_te_router_ids = db.Column(db.String)
    admin_group_mask = db.Column(db.String)
    maximum_link_bandwidth = db.Column(db.Float)
    maximum_reservable_bandwidth = db.Column(db.Float)
    unreserved_bandwidth = db.Column(db.String)
    te_metric = db.Column(db.Integer)
    igp_metric = db.Column(db.Integer)

    def __repr__(self):
        return '<ExaBGP BGPLS Link {}>'.format(self.id)

class BGPLS_Prefix_V4(db.Model):
    """ Class representing a BGP LS Prefix (IPv4) """
    id = db.Column(db.Integer, primary_key=True)
    node_id = db.Column(db.String, db.ForeignKey('prefixes_v4.id'))
    l3_nlri_type = db.Column(db.String)
    l3_routing_topology = db.Column(db.Integer)
    local_asn = db.Column(db.Integer)
    local_bgp_ls_id = db.Column(db.String)
    local_router_id = db.Column(db.String)
    ip_reachability_tlv = db.Column(db.String)
    ip_reachability_prefix = db.Column(db.String)
    nexthop = db.Column(db.String)
