from flask_sqlalchemy import SQLAlchemy
from __main__ import app

db = SQLAlchemy(app)

class BGPNeighborship(db.Model):
    __tablename__ = "bgpneighborship"
    """ Class representing a BGP Neighborship """
    id = db.Column(db.Integer, primary_key=True)
    exabgp_version = db.Column(db.String)
    time = db.Column(db.String)
    host = db.Column(db.String)
    pid = db.Column(db.Integer)
    ppid = db.Column(db.Integer)
    counter = db.Column(db.Integer)
    local_address = db.Column(db.String)
    peer_address = db.Column(db.String)
    local_asn = db.Column(db.String)
    peer_asn = db.Column(db.String)
    state_type = db.Column(db.String)

    def __repr__(self):
        return '<ExaBGP Neighborship {}>'.format(self.id)

    def as_dict(self):
        return {
            "id": self.id,
            "exabgp": self.exabgp_version,
            "time": self.time,
            "host": self.host,
            "pid": self.pid,
            "ppid": self.ppid,
            "counter": self.counter,
            "neighbor": {
                "address": {
                    "local": self.local_address,
                    "peer": self.peer_address
                },
                "asn": {
                    "local": self.local_asn,
                    "peer": self.peer_asn
                },
                "state": self.state_type
            }
        }

class BGPLSNode(db.Model):
    __tablename__ = "bgplsnode"
    """ Class representing a BGP LS Node Update """
    id = db.Column(db.Integer, primary_key=True)
    node_id = db.Column(db.String, unique=True)
    l3_nlri_type = db.Column(db.String)
    l3_routing_topology = db.Column(db.Integer)
    protocol_id = db.Column(db.Integer)
    asn = db.Column(db.String)
    bgp_ls_id = db.Column(db.String)
    router_id = db.Column(db.String)
    nexthop = db.Column(db.String)
    origin = db.Column(db.String)
    local_preference = db.Column(db.String)
    igp_area_id = db.Column(db.String)
    _local_te_router_ids = db.Column(db.String) 
    sr_capability_flags = db.Column(db.String)
    _sr_sids = db.Column(db.String)
    bgpls_links = db.relationship('BGPLSLink', backref='bgplsnode', lazy='dynamic')
    bgpls_prefixes = db.relationship('BGPLSPrefixV4', backref='bgplsnode', lazy='dynamic')

    def __repr__(self):
        return '<ExaBGP BGPLS Node {}>'.format(self.id)

    def as_dict(self, lazy=False):
        return {
            "id": self.id,
            "node_id": self.node_id,
            "node_details": {
                "l3_nlri_type": self.l3_nlri_type,
                "l3_routing_topology": self.l3_routing_topology,
                "protocol_id": self.protocol_id,
                "node_descriptors": {
                    "autonomous-system": self.asn,
                    "bgp-ls-identifier": self.bgp_ls_id,
                    "router-id": self.router_id
                },
                "nexthop": self.nexthop,
                "node_attributes": {
                    "origin": self.origin,
                    "local-preference": self.local_preference,
                    "bgp-ls": {
                        "area-id": self.igp_area_id,
                        "local-te-router-ids": self.local_te_router_ids,
                        "sr-capability-flags": {x[:1]: int(x[-1:]) for x in [entry for entry in self.sr_capability_flags.split(";") if entry]},
                        "sids": self.sr_sids
                    }
                },
            "links": (self.bgpls_links.all() if lazy else [link.as_dict() for link in self.bgpls_links.all()]),
            "prefixes": (self.bgpls_prefixes.all() if lazy else [prefix.as_dict() for prefix in self.bgpls_prefixes.all()])
            }
        }

    @property
    def local_te_router_ids(self):
        return [x for x in self._local_te_router_ids.split(";")]

    @local_te_router_ids.setter
    def local_te_router_ids(self, value):
        if isinstance(value, list):
            convert_list = [str(x) for x in value]
            self._local_te_router_ids = ";".join(convert_list)

    @property
    def sr_sids(self):
        return [int(x) for x in self._sr_sids.split(";")]

    @sr_sids.setter
    def sr_sids(self, value):
        if isinstance(value, list):
            convert_list = [str(x) for x in value]
            self._sr_sids = ";".join(convert_list)

class BGPLSLink(db.Model):
    __tablename__ = "bgplslink"
    """ Class representing a BGP LS Link Update """
    id = db.Column(db.Integer, primary_key=True)
    node_id = db.Column(db.Integer, db.ForeignKey('bgplsnode.id'))
    l3_nlri_type = db.Column(db.String)
    l3_routing_topology = db.Column(db.Integer)
    protocol_id = db.Column(db.Integer)
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
    _local_te_router_ids = db.Column(db.String)
    _peer_te_router_ids = db.Column(db.String)
    _admin_group_mask = db.Column(db.String)
    maximum_link_bandwidth = db.Column(db.Float)
    maximum_reservable_bandwidth = db.Column(db.Float)
    _unreserved_bandwidth = db.Column(db.String)
    te_metric = db.Column(db.Integer)
    igp_metric = db.Column(db.Integer)
    sr_adj_flags = db.Column(db.String)
    _sr_sids = db.Column(db.String)
    sr_adj_weight = db.Column(db.Integer)

    def __repr__(self):
        return '<ExaBGP BGPLS Link {}>'.format(self.id)

    def as_dict(self):
        return {
            "id": self.id,
            "node_id": self.node_id,
            "link": {
                "ls-nlri-type": self.l3_nlri_type,
                "l3-routing-topology": self.l3_routing_topology,
                "protocol-id": self.protocol_id,
                "local-node-descriptors": {
                    "autonomous-system": self.local_asn,
                    "bgp-ls-identifier": self.local_bgp_ls_id,
                    "router-id": self.local_router_id
                },
                "remote-node-descriptors": {
                    "autonomous-system": self.peer_asn,
                    "bgp-ls-identifier": self.peer_bgp_ls_id,
                    "router-id": self.peer_router_id
                },
                "interface-address": {
                    "interface-address": self.local_interface_address
                },
                "neighbor-address": {
                    "neighbor-address": self.peer_interface_address
                },
                "link_attributes": {
                    "origin": self.origin,
                    "local-preference": self.local_preference,
                    "bgp-ls": {
                        "local-te-router-ids": self.local_te_router_ids,
                        "peer-te-router-ids": self.peer_te_router_ids,
                        "admin-group-mask": self.admin_group_mask,
                        "maximum-link-bandwidth": self.maximum_link_bandwidth,
                        "maximum-reservable-link-bandwidth": self.maximum_reservable_bandwidth,
                        "unreserved-bandwidth": self.unreserved_bandwidth,
                        "te-metric": self.te_metric,
                        "igp-metric": self.igp_metric,
                        "sr_adj_flags": {x[:1]: int(x[-1:]) for x in [entry for entry in self.sr_adj_flags.split(";") if entry]},
                        "sids": self.sr_sids,
                        "sr-adj-weight": self.sr_adj_weight
                    }
                }
            }
        }

    @property
    def local_te_router_ids(self):
        if self._local_te_router_ids:
            return [x for x in self._local_te_router_ids.split(";")]

    @local_te_router_ids.setter
    def local_te_router_ids(self, value):
        if isinstance(value, list):
            convert_list = [str(x) for x in value]
            self._local_te_router_ids = ";".join(convert_list)

    @property
    def peer_te_router_ids(self):
        if self._peer_te_router_ids:
            return [x for x in self._peer_te_router_ids.split(";")]

    @peer_te_router_ids.setter
    def peer_te_router_ids(self, value):
        if isinstance(value, list):
            convert_list = [str(x) for x in value]
            self._peer_te_router_ids = ";".join(convert_list)

    @property
    def admin_group_mask(self):
        return [int(x) for x in self._admin_group_mask.split(";")]

    @admin_group_mask.setter
    def admin_group_mask(self, value):
        if isinstance(value, list):
            convert_list = [str(x) for x in value]
            self._admin_group_mask = ";".join(convert_list)

    @property
    def unreserved_bandwidth(self):
        return [float(x) for x in self._unreserved_bandwidth.split(";")]

    @unreserved_bandwidth.setter
    def unreserved_bandwidth(self, value):
        if isinstance(value, list):
            convert_list = [str(x) for x in value]
            self._unreserved_bandwidth = ";".join(convert_list)

    @property
    def sr_sids(self):
        return [int(x) for x in self._sr_sids.split(";")]

    @sr_sids.setter
    def sr_sids(self, value):
        if isinstance(value, list):
            convert_list = [str(x) for x in value]
            self._sr_sids = ";".join(convert_list)

class BGPLSPrefixV4(db.Model):
    __tablename__ = "bgplsprefixv4"
    """ Class representing a BGP LS Prefix (IPv4) """
    id = db.Column(db.Integer, primary_key=True)
    node_id = db.Column(db.Integer, db.ForeignKey('bgplsnode.id'))
    l3_nlri_type = db.Column(db.String)
    l3_routing_topology = db.Column(db.Integer)
    protocol_id = db.Column(db.Integer)
    local_asn = db.Column(db.Integer)
    local_bgp_ls_id = db.Column(db.String)
    local_router_id = db.Column(db.String)
    ip_reachability_tlv = db.Column(db.String)
    ip_reachability_prefix = db.Column(db.String)
    nexthop = db.Column(db.String)
    origin = db.Column(db.String)
    local_preference = db.Column(db.Integer)
    prefix_metric = db.Column(db.Integer)
    sr_prefix_flags = db.Column(db.String)
    _sr_sids = db.Column(db.String)
    sr_prefix_attribute_flags = db.Column(db.String)
    sr_algorithm = db.Column(db.String)

    def __repr__(self):
        return '<ExaBGP BGPLS PrefixV4 {}>'.format(self.id)

    def as_dict(self):
        result = {
            "id": self.id,
            "node_id": self.node_id,
            "prefix": {
                "ls-nlri-type": self.l3_nlri_type,
                "l3-routing-topology": self.l3_routing_topology,
                "protocol-id": self.protocol_id,
                "node-descriptors": {
                    "autonomous-system": self.local_asn,
                    "bgp-ls-identifier": self.local_bgp_ls_id,
                    "router-id": self.local_router_id
                },
                "ip-reachability-tlv": self.ip_reachability_tlv,
                "ip-reach-prefix": self.ip_reachability_prefix,
                "nexthop": self.nexthop,
                "prefix_attributes": {
                    "origin": self.origin,
                    "local-preference": self.local_preference,
                    "bgp-ls": {
                        "prefix-metric": self.prefix_metric,
                        "sr-algorithm": self.sr_algorithm
                    }
                }
            }
        }

        if self.sr_prefix_flags:
            result["prefix"]["prefix_attributes"]["bgp-ls"]["sr-prefix-flags"] = {x[:1] : int(x[-1:]) for x in [entry for entry in self.sr_prefix_flags.split(";") if entry]}

        if self._sr_sids:
            app.logger.debug(self.sr_sids)
            result["prefix"]["prefix_attributes"]["bgp-ls"]["sids"] = self.sr_sids

        if self.sr_prefix_attribute_flags:
            result["prefix"]["prefix_attributes"]["bgp-ls"]["sr-prefix-attribute-flags"] = {x[:1]: int(x[-1:]) for x in [entry for entry in self.sr_prefix_attribute_flags.split(";") if entry]}

        return result

    @property
    def sr_sids(self):
        return [int(x) for x in self._sr_sids.split(";")]

    @sr_sids.setter
    def sr_sids(self, value):
        if isinstance(value, list):
            convert_list = [str(x) for x in value]
            self._sr_sids = ";".join(convert_list)
