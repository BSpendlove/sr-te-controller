# This topology is what is to be expected after gathering all UPDATEs after a neighbor has come UP and we receive the EOR (end of RIB) - eg. the end of the BGP update...
# This is not a topology built with the 'build_ted' function, so you can use this topology to build the TED if you make any changes to that function and want sample data to work with...

json_topology = [
{
    "exabgp": "4.0.1",
    "time": 1595789630.8830001,
    "host": "4a0efa848708",
    "pid": 16,
    "ppid": 1,
    "counter": 5,
    "type": "update",
    "neighbor": {
        "address": {
            "local": "0.0.0.0",
            "peer": "192.168.0.249"
        },
        "asn": {
            "local": 100,
            "peer": 100
        },
        "direction": "receive",
        "message": {
            "update": {
                "attribute": {
                    "origin": "igp",
                    "local-preference": 100,
                    "bgp-ls": {
                        "local-te-router-ids": [
                            "10.255.255.1"
                        ],
                        "remote-te-router-id": "10.255.255.2",
                        "admin-group-mask": [
                            0
                        ],
                        "maximum-link-bandwidth": 125000000.0,
                        "maximum-reservable-link-bandwidth": 0.0,
                        "unreserved-bandwidth": [
                            0.0,
                            0.0,
                            0.0,
                            0.0,
                            0.0,
                            0.0,
                            0.0,
                            0.0
                        ],
                        "te-metric": 10,
                        "igp-metric": 10
                    }
                },
                "announce": {
                    "bgp-ls bgp-ls": {
                        "192.168.0.249": [
                            {
                                "ls-nlri-type": "bgpls-link",
                                "l3-routing-topology": 100,
                                "protocol-id": 2,
                                "local-node-descriptors": {
                                    "autonomous-system": 100,
                                    "bgp-ls-identifier": "3232235769",
                                    "router-id": "000000000001"
                                },
                                "remote-node-descriptors": {
                                    "autonomous-system": 100,
                                    "bgp-ls-identifier": "3232235769",
                                    "router-id": "000000000002"
                                },
                                "interface-address": {
                                    "interface-address": "10.0.12.1"
                                },
                                "neighbor-address": {
                                    "neighbor-address": "10.0.12.2"
                                }
                            }
                        ]
                    }
                }
            }
        }
    }
},
{
    "exabgp": "4.0.1",
    "time": 1595789630.8839865,
    "host": "4a0efa848708",
    "pid": 16,
    "ppid": 1,
    "counter": 7,
    "type": "update",
    "neighbor": {
        "address": {
            "local": "0.0.0.0",
            "peer": "192.168.0.249"
        },
        "asn": {
            "local": 100,
            "peer": 100
        },
        "direction": "receive",
        "message": {
            "update": {
                "attribute": {
                    "origin": "igp",
                    "local-preference": 100,
                    "bgp-ls": {
                        "local-te-router-ids": [
                            "10.255.255.2"
                        ],
                        "remote-te-router-id": "10.255.255.1",
                        "admin-group-mask": [
                            0
                        ],
                        "maximum-link-bandwidth": 125000000.0,
                        "maximum-reservable-link-bandwidth": 0.0,
                        "unreserved-bandwidth": [
                            0.0,
                            0.0,
                            0.0,
                            0.0,
                            0.0,
                            0.0,
                            0.0,
                            0.0
                        ],
                        "te-metric": 10,
                        "igp-metric": 10
                    }
                },
                "announce": {
                    "bgp-ls bgp-ls": {
                        "192.168.0.249": [
                            {
                                "ls-nlri-type": "bgpls-link",
                                "l3-routing-topology": 100,
                                "protocol-id": 2,
                                "local-node-descriptors": {
                                    "autonomous-system": 100,
                                    "bgp-ls-identifier": "3232235769",
                                    "router-id": "000000000002"
                                },
                                "remote-node-descriptors": {
                                    "autonomous-system": 100,
                                    "bgp-ls-identifier": "3232235769",
                                    "router-id": "000000000001"
                                },
                                "interface-address": {
                                    "interface-address": "10.0.12.2"
                                },
                                "neighbor-address": {
                                    "neighbor-address": "10.0.12.1"
                                }
                            }
                        ]
                    }
                }
            }
        }
    }
},
{
    "exabgp": "4.0.1",
    "time": 1595789630.884672,
    "host": "4a0efa848708",
    "pid": 16,
    "ppid": 1,
    "counter": 9,
    "type": "update",
    "neighbor": {
        "address": {
            "local": "0.0.0.0",
            "peer": "192.168.0.249"
        },
        "asn": {
            "local": 100,
            "peer": 100
        },
        "direction": "receive",
        "message": {
            "update": {
                "attribute": {
                    "origin": "igp",
                    "local-preference": 100,
                    "bgp-ls": {
                        "area-id": "490001",
                        "local-te-router-ids": [
                            "10.255.255.1"
                        ]
                    }
                },
                "announce": {
                    "bgp-ls bgp-ls": {
                        "192.168.0.249": [
                            {
                                "ls-nlri-type": "bgpls-node",
                                "l3-routing-topology": 100,
                                "protocol-id": 2,
                                "node-descriptors": {
                                    "autonomous-system": 100,
                                    "bgp-ls-identifier": "3232235769",
                                    "router-id": "000000000001"
                                },
                                "nexthop": "192.168.0.249"
                            }
                        ]
                    }
                }
            }
        }
    }
},
{
    "exabgp": "4.0.1",
    "time": 1595789630.8855178,
    "host": "4a0efa848708",
    "pid": 16,
    "ppid": 1,
    "counter": 11,
    "type": "update",
    "neighbor": {
        "address": {
            "local": "0.0.0.0",
            "peer": "192.168.0.249"
        },
        "asn": {
            "local": 100,
            "peer": 100
        },
        "direction": "receive",
        "message": {
            "update": {
                "attribute": {
                    "origin": "igp",
                    "local-preference": 100,
                    "bgp-ls": {
                        "prefix-metric": 0
                    }
                },
                "announce": {
                    "bgp-ls bgp-ls": {
                        "192.168.0.249": [
                            {
                                "ls-nlri-type": "bgpls-prefix-v4",
                                "l3-routing-topology": 100,
                                "protocol-id": 2,
                                "node-descriptors": {
                                    "autonomous-system": 100,
                                    "bgp-ls-identifier": "3232235769",
                                    "router-id": "000000000002"
                                },
                                "ip-reachability-tlv": "10.255.255.2",
                                "ip-reach-prefix": "10.255.255.2/32",
                                "nexthop": "192.168.0.249"
                            },
                            {
                                "ls-nlri-type": "bgpls-prefix-v4",
                                "l3-routing-topology": 100,
                                "protocol-id": 2,
                                "node-descriptors": {
                                    "autonomous-system": 100,
                                    "bgp-ls-identifier": "3232235769",
                                    "router-id": "000000000001"
                                },
                                "ip-reachability-tlv": "10.255.255.1",
                                "ip-reach-prefix": "10.255.255.1/32",
                                "nexthop": "192.168.0.249"
                            }
                        ]
                    }
                }
            }
        }
    }
},
{
    "exabgp": "4.0.1",
    "time": 1595789630.886875,
    "host": "4a0efa848708",
    "pid": 16,
    "ppid": 1,
    "counter": 13,
    "type": "update",
    "neighbor": {
        "address": {
            "local": "0.0.0.0",
            "peer": "192.168.0.249"
        },
        "asn": {
            "local": 100,
            "peer": 100
        },
        "direction": "receive",
        "message": {
            "update": {
                "attribute": {
                    "origin": "igp",
                    "local-preference": 100,
                    "bgp-ls": {
                        "prefix-metric": 10
                    }
                },
                "announce": {
                    "bgp-ls bgp-ls": {
                        "192.168.0.249": [
                            {
                                "ls-nlri-type": "bgpls-prefix-v4",
                                "l3-routing-topology": 100,
                                "protocol-id": 2,
                                "node-descriptors": {
                                    "autonomous-system": 100,
                                    "bgp-ls-identifier": "3232235769",
                                    "router-id": "000000000002"
                                },
                                "ip-reachability-tlv": "10.0.24.0",
                                "ip-reach-prefix": "10.0.24.0/24",
                                "nexthop": "192.168.0.249"
                            },
                            {
                                "ls-nlri-type": "bgpls-prefix-v4",
                                "l3-routing-topology": 100,
                                "protocol-id": 2,
                                "node-descriptors": {
                                    "autonomous-system": 100,
                                    "bgp-ls-identifier": "3232235769",
                                    "router-id": "000000000002"
                                },
                                "ip-reachability-tlv": "10.0.23.0",
                                "ip-reach-prefix": "10.0.23.0/24",
                                "nexthop": "192.168.0.249"
                            },
                            {
                                "ls-nlri-type": "bgpls-prefix-v4",
                                "l3-routing-topology": 100,
                                "protocol-id": 2,
                                "node-descriptors": {
                                    "autonomous-system": 100,
                                    "bgp-ls-identifier": "3232235769",
                                    "router-id": "000000000002"
                                },
                                "ip-reachability-tlv": "10.0.12.0",
                                "ip-reach-prefix": "10.0.12.0/24",
                                "nexthop": "192.168.0.249"
                            },
                            {
                                "ls-nlri-type": "bgpls-prefix-v4",
                                "l3-routing-topology": 100,
                                "protocol-id": 2,
                                "node-descriptors": {
                                    "autonomous-system": 100,
                                    "bgp-ls-identifier": "3232235769",
                                    "router-id": "000000000001"
                                },
                                "ip-reachability-tlv": "192.168.0.0",
                                "ip-reach-prefix": "192.168.0.0/24",
                                "nexthop": "192.168.0.249"
                            },
                            {
                                "ls-nlri-type": "bgpls-prefix-v4",
                                "l3-routing-topology": 100,
                                "protocol-id": 2,
                                "node-descriptors": {
                                    "autonomous-system": 100,
                                    "bgp-ls-identifier": "3232235769",
                                    "router-id": "000000000001"
                                },
                                "ip-reachability-tlv": "10.0.12.0",
                                "ip-reach-prefix": "10.0.12.0/24",
                                "nexthop": "192.168.0.249"
                            },
                            {
                                "ls-nlri-type": "bgpls-prefix-v4",
                                "l3-routing-topology": 100,
                                "protocol-id": 2,
                                "node-descriptors": {
                                    "autonomous-system": 100,
                                    "bgp-ls-identifier": "3232235769",
                                    "router-id": "000000000001"
                                },
                                "ip-reachability-tlv": "10.0.11.0",
                                "ip-reach-prefix": "10.0.11.0/24",
                                "nexthop": "192.168.0.249"
                            }
                        ]
                    }
                }
            }
        }
    }
},
{
    "exabgp": "4.0.1",
    "time": 1595789630.8892982,
    "host": "4a0efa848708",
    "pid": 16,
    "ppid": 1,
    "counter": 15,
    "type": "update",
    "neighbor": {
        "address": {
            "local": "0.0.0.0",
            "peer": "192.168.0.249"
        },
        "asn": {
            "local": 100,
            "peer": 100
        },
        "direction": "receive",
        "message": {
            "update": {
                "attribute": {
                    "origin": "igp",
                    "local-preference": 100,
                    "bgp-ls": {
                        "area-id": "490001",
                        "local-te-router-ids": [
                            "10.255.255.2"
                        ]
                    }
                },
                "announce": {
                    "bgp-ls bgp-ls": {
                        "192.168.0.249": [
                            {
                                "ls-nlri-type": "bgpls-node",
                                "l3-routing-topology": 100,
                                "protocol-id": 2,
                                "node-descriptors": {
                                    "autonomous-system": 100,
                                    "bgp-ls-identifier": "3232235769",
                                    "router-id": "000000000002"
                                },
                                "nexthop": "192.168.0.249"
                            }
                        ]
                    }
                }
            }
        }
    }
}]
