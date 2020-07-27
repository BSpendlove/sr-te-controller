# This is a topology built with the 'build_ted' function. That takes the initial BGP topology (all updates including EOR) and parses them into a useful format, apending specific prefixes/links to their respective node.

topo1 = [
    {
        "node_id": "1003232235769000000000002",
        "node_details": {
            "ls-nlri-type": "bgpls-node",
            "l3-routing-topology": 100,
            "protocol-id": 2,
            "node-descriptors": {
                "autonomous-system": 100,
                "bgp-ls-identifier": "3232235769",
                "router-id": "000000000002"
            },
            "nexthop": "192.168.0.249"
        },
        "node_attributes": {
            "origin": "igp",
            "local-preference": 100,
            "bgp-ls": {
                "area-id": "490001",
                "local-te-router-ids": [
                    "10.255.255.2"
                ]
            }
        },
        "links": [
            {
                "link": {
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
                },
                "link_attributes": {
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
                }
            }
        ],
        "prefixes": [
            {
                "prefix": {
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
                "prefix_attributes": {
                    "origin": "igp",
                    "local-preference": 100,
                    "bgp-ls": {
                        "prefix-metric": 0
                    }
                }
            },
            {
                "prefix": {
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
                "prefix_attributes": {
                    "origin": "igp",
                    "local-preference": 100,
                    "bgp-ls": {
                        "prefix-metric": 10
                    }
                }
            },
            {
                "prefix": {
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
                "prefix_attributes": {
                    "origin": "igp",
                    "local-preference": 100,
                    "bgp-ls": {
                        "prefix-metric": 10
                    }
                }
            },
            {
                "prefix": {
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
                "prefix_attributes": {
                    "origin": "igp",
                    "local-preference": 100,
                    "bgp-ls": {
                        "prefix-metric": 10
                    }
                }
            }
        ]
    },
    {
        "node_id": "1003232235769000000000001",
        "node_details": {
            "ls-nlri-type": "bgpls-node",
            "l3-routing-topology": 100,
            "protocol-id": 2,
            "node-descriptors": {
                "autonomous-system": 100,
                "bgp-ls-identifier": "3232235769",
                "router-id": "000000000001"
            },
            "nexthop": "192.168.0.249"
        },
        "node_attributes": {
            "origin": "igp",
            "local-preference": 100,
            "bgp-ls": {
                "area-id": "490001",
                "local-te-router-ids": [
                    "10.255.255.1"
                ]
            }
        },
        "links": [
            {
                "link": {
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
                },
                "link_attributes": {
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
                }
            }
        ],
        "prefixes": [
            {
                "prefix": {
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
                },
                "prefix_attributes": {
                    "origin": "igp",
                    "local-preference": 100,
                    "bgp-ls": {
                        "prefix-metric": 0
                    }
                }
            },
            {
                "prefix": {
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
                "prefix_attributes": {
                    "origin": "igp",
                    "local-preference": 100,
                    "bgp-ls": {
                        "prefix-metric": 10
                    }
                }
            },
            {
                "prefix": {
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
                "prefix_attributes": {
                    "origin": "igp",
                    "local-preference": 100,
                    "bgp-ls": {
                        "prefix-metric": 10
                    }
                }
            },
            {
                "prefix": {
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
                },
                "prefix_attributes": {
                    "origin": "igp",
                    "local-preference": 100,
                    "bgp-ls": {
                        "prefix-metric": 10
                    }
                }
            }
        ]
    }
]