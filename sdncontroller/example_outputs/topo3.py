topo3 = [
     {
         "node_id": "1003232235769000000000009",
         "node_details": {
             "ls-nlri-type": "bgpls-node",
             "l3-routing-topology": 100,
             "protocol-id": 2,
             "node-descriptors": {
                 "autonomous-system": 100,
                 "bgp-ls-identifier": "3232235769",
                 "router-id": "000000000009"
             },
             "nexthop": "192.168.0.249"
         },
         "node_attributes": {
             "origin": "igp",
             "local-preference": 100,
             "bgp-ls": {
                 "area-id": "490001",
                 "local-te-router-ids": [
                     "10.255.255.9"
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
                         "router-id": "000000000009"
                     },
                     "remote-node-descriptors": {
                         "autonomous-system": 100,
                         "bgp-ls-identifier": "3232235769",
                         "router-id": "000000000006"
                     },
                     "interface-address": {
                         "interface-address": "10.0.69.9"
                     },
                     "neighbor-address": {
                         "neighbor-address": "10.0.69.6"
                     }
                 },
                 "link_attributes": {
                     "origin": "igp",
                     "local-preference": 100,
                     "bgp-ls": {
                         "local-te-router-ids": [
                             "10.255.255.9"
                         ],
                         "remote-te-router-id": "10.255.255.6",
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
             },
             {
                 "link": {
                     "ls-nlri-type": "bgpls-link",
                     "l3-routing-topology": 100,
                     "protocol-id": 2,
                     "local-node-descriptors": {
                         "autonomous-system": 100,
                         "bgp-ls-identifier": "3232235769",
                         "router-id": "000000000009"
                     },
                     "remote-node-descriptors": {
                         "autonomous-system": 100,
                         "bgp-ls-identifier": "3232235769",
                         "router-id": "000000000008"
                     },
                     "interface-address": {
                         "interface-address": "10.0.89.9"
                     },
                     "neighbor-address": {
                         "neighbor-address": "10.0.89.8"
                     }
                 },
                 "link_attributes": {
                     "origin": "igp",
                     "local-preference": 100,
                     "bgp-ls": {
                         "local-te-router-ids": [
                             "10.255.255.9"
                         ],
                         "remote-te-router-id": "10.255.255.8",
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
                         "router-id": "000000000009"
                     },
                     "ip-reachability-tlv": "10.255.255.9",
                     "ip-reach-prefix": "10.255.255.9/32",
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
                         "router-id": "000000000009"
                     },
                     "ip-reachability-tlv": "10.0.89.0",
                     "ip-reach-prefix": "10.0.89.0/24",
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
                         "router-id": "000000000009"
                     },
                     "ip-reachability-tlv": "10.0.69.0",
                     "ip-reach-prefix": "10.0.69.0/24",
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
         "node_id": "1003232235769000000000008",
         "node_details": {
             "ls-nlri-type": "bgpls-node",
             "l3-routing-topology": 100,
             "protocol-id": 2,
             "node-descriptors": {
                 "autonomous-system": 100,
                 "bgp-ls-identifier": "3232235769",
                 "router-id": "000000000008"
             },
             "nexthop": "192.168.0.249"
         },
         "node_attributes": {
             "origin": "igp",
             "local-preference": 100,
             "bgp-ls": {
                 "area-id": "490001",
                 "local-te-router-ids": [
                     "10.255.255.8"
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
                         "router-id": "000000000008"
                     },
                     "remote-node-descriptors": {
                         "autonomous-system": 100,
                         "bgp-ls-identifier": "3232235769",
                         "router-id": "000000000009"
                     },
                     "interface-address": {
                         "interface-address": "10.0.89.8"
                     },
                     "neighbor-address": {
                         "neighbor-address": "10.0.89.9"
                     }
                 },
                 "link_attributes": {
                     "origin": "igp",
                     "local-preference": 100,
                     "bgp-ls": {
                         "local-te-router-ids": [
                             "10.255.255.8"
                         ],
                         "remote-te-router-id": "10.255.255.9",
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
             },
             {
                 "link": {
                     "ls-nlri-type": "bgpls-link",
                     "l3-routing-topology": 100,
                     "protocol-id": 2,
                     "local-node-descriptors": {
                         "autonomous-system": 100,
                         "bgp-ls-identifier": "3232235769",
                         "router-id": "000000000008"
                     },
                     "remote-node-descriptors": {
                         "autonomous-system": 100,
                         "bgp-ls-identifier": "3232235769",
                         "router-id": "000000000007"
                     },
                     "interface-address": {
                         "interface-address": "10.0.78.8"
                     },
                     "neighbor-address": {
                         "neighbor-address": "10.0.78.7"
                     }
                 },
                 "link_attributes": {
                     "origin": "igp",
                     "local-preference": 100,
                     "bgp-ls": {
                         "local-te-router-ids": [
                             "10.255.255.8"
                         ],
                         "remote-te-router-id": "10.255.255.7",
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
             },
             {
                 "link": {
                     "ls-nlri-type": "bgpls-link",
                     "l3-routing-topology": 100,
                     "protocol-id": 2,
                     "local-node-descriptors": {
                         "autonomous-system": 100,
                         "bgp-ls-identifier": "3232235769",
                         "router-id": "000000000008"
                     },
                     "remote-node-descriptors": {
                         "autonomous-system": 100,
                         "bgp-ls-identifier": "3232235769",
                         "router-id": "000000000006"
                     },
                     "interface-address": {
                         "interface-address": "10.0.68.8"
                     },
                     "neighbor-address": {
                         "neighbor-address": "10.0.68.6"
                     }
                 },
                 "link_attributes": {
                     "origin": "igp",
                     "local-preference": 100,
                     "bgp-ls": {
                         "local-te-router-ids": [
                             "10.255.255.8"
                         ],
                         "remote-te-router-id": "10.255.255.6",
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
                         "router-id": "000000000008"
                     },
                     "ip-reachability-tlv": "10.255.255.8",
                     "ip-reach-prefix": "10.255.255.8/32",
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
                         "router-id": "000000000008"
                     },
                     "ip-reachability-tlv": "10.0.89.0",
                     "ip-reach-prefix": "10.0.89.0/24",
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
                         "router-id": "000000000008"
                     },
                     "ip-reachability-tlv": "10.0.78.0",
                     "ip-reach-prefix": "10.0.78.0/24",
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
                         "router-id": "000000000008"
                     },
                     "ip-reachability-tlv": "10.0.68.0",
                     "ip-reach-prefix": "10.0.68.0/24",
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
         "node_id": "1003232235769000000000007",
         "node_details": {
             "ls-nlri-type": "bgpls-node",
             "l3-routing-topology": 100,
             "protocol-id": 2,
             "node-descriptors": {
                 "autonomous-system": 100,
                 "bgp-ls-identifier": "3232235769",
                 "router-id": "000000000007"
             },
             "nexthop": "192.168.0.249"
         },
         "node_attributes": {
             "origin": "igp",
             "local-preference": 100,
             "bgp-ls": {
                 "area-id": "490001",
                 "local-te-router-ids": [
                     "10.255.255.7"
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
                         "router-id": "000000000007"
                     },
                     "remote-node-descriptors": {
                         "autonomous-system": 100,
                         "bgp-ls-identifier": "3232235769",
                         "router-id": "000000000004"
                     },
                     "interface-address": {
                         "interface-address": "10.0.47.7"
                     },
                     "neighbor-address": {
                         "neighbor-address": "10.0.47.4"
                     }
                 },
                 "link_attributes": {
                     "origin": "igp",
                     "local-preference": 100,
                     "bgp-ls": {
                         "local-te-router-ids": [
                             "10.255.255.7"
                         ],
                         "remote-te-router-id": "10.255.255.4",
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
             },
             {
                 "link": {
                     "ls-nlri-type": "bgpls-link",
                     "l3-routing-topology": 100,
                     "protocol-id": 2,
                     "local-node-descriptors": {
                         "autonomous-system": 100,
                         "bgp-ls-identifier": "3232235769",
                         "router-id": "000000000007"
                     },
                     "remote-node-descriptors": {
                         "autonomous-system": 100,
                         "bgp-ls-identifier": "3232235769",
                         "router-id": "000000000008"
                     },
                     "interface-address": {
                         "interface-address": "10.0.78.7"
                     },
                     "neighbor-address": {
                         "neighbor-address": "10.0.78.8"
                     }
                 },
                 "link_attributes": {
                     "origin": "igp",
                     "local-preference": 100,
                     "bgp-ls": {
                         "local-te-router-ids": [
                             "10.255.255.7"
                         ],
                         "remote-te-router-id": "10.255.255.8",
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
                         "router-id": "000000000007"
                     },
                     "ip-reachability-tlv": "10.255.255.7",
                     "ip-reach-prefix": "10.255.255.7/32",
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
                         "router-id": "000000000007"
                     },
                     "ip-reachability-tlv": "10.0.78.0",
                     "ip-reach-prefix": "10.0.78.0/24",
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
                         "router-id": "000000000007"
                     },
                     "ip-reachability-tlv": "10.0.47.0",
                     "ip-reach-prefix": "10.0.47.0/24",
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
         "node_id": "1003232235769000000000006",
         "node_details": {
             "ls-nlri-type": "bgpls-node",
             "l3-routing-topology": 100,
             "protocol-id": 2,
             "node-descriptors": {
                 "autonomous-system": 100,
                 "bgp-ls-identifier": "3232235769",
                 "router-id": "000000000006"
             },
             "nexthop": "192.168.0.249"
         },
         "node_attributes": {
             "origin": "igp",
             "local-preference": 100,
             "bgp-ls": {
                 "area-id": "490001",
                 "local-te-router-ids": [
                     "10.255.255.6"
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
                         "router-id": "000000000006"
                     },
                     "remote-node-descriptors": {
                         "autonomous-system": 100,
                         "bgp-ls-identifier": "3232235769",
                         "router-id": "000000000009"
                     },
                     "interface-address": {
                         "interface-address": "10.0.69.6"
                     },
                     "neighbor-address": {
                         "neighbor-address": "10.0.69.9"
                     }
                 },
                 "link_attributes": {
                     "origin": "igp",
                     "local-preference": 100,
                     "bgp-ls": {
                         "local-te-router-ids": [
                             "10.255.255.6"
                         ],
                         "remote-te-router-id": "10.255.255.9",
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
             },
             {
                 "link": {
                     "ls-nlri-type": "bgpls-link",
                     "l3-routing-topology": 100,
                     "protocol-id": 2,
                     "local-node-descriptors": {
                         "autonomous-system": 100,
                         "bgp-ls-identifier": "3232235769",
                         "router-id": "000000000006"
                     },
                     "remote-node-descriptors": {
                         "autonomous-system": 100,
                         "bgp-ls-identifier": "3232235769",
                         "router-id": "000000000008"
                     },
                     "interface-address": {
                         "interface-address": "10.0.68.6"
                     },
                     "neighbor-address": {
                         "neighbor-address": "10.0.68.8"
                     }
                 },
                 "link_attributes": {
                     "origin": "igp",
                     "local-preference": 100,
                     "bgp-ls": {
                         "local-te-router-ids": [
                             "10.255.255.6"
                         ],
                         "remote-te-router-id": "10.255.255.8",
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
             },
             {
                 "link": {
                     "ls-nlri-type": "bgpls-link",
                     "l3-routing-topology": 100,
                     "protocol-id": 2,
                     "local-node-descriptors": {
                         "autonomous-system": 100,
                         "bgp-ls-identifier": "3232235769",
                         "router-id": "000000000006"
                     },
                     "remote-node-descriptors": {
                         "autonomous-system": 100,
                         "bgp-ls-identifier": "3232235769",
                         "router-id": "000000000005"
                     },
                     "interface-address": {
                         "interface-address": "10.0.56.6"
                     },
                     "neighbor-address": {
                         "neighbor-address": "10.0.56.5"
                     }
                 },
                 "link_attributes": {
                     "origin": "igp",
                     "local-preference": 100,
                     "bgp-ls": {
                         "local-te-router-ids": [
                             "10.255.255.6"
                         ],
                         "remote-te-router-id": "10.255.255.5",
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
                         "router-id": "000000000006"
                     },
                     "ip-reachability-tlv": "10.255.255.6",
                     "ip-reach-prefix": "10.255.255.6/32",
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
                         "router-id": "000000000006"
                     },
                     "ip-reachability-tlv": "10.0.69.0",
                     "ip-reach-prefix": "10.0.69.0/24",
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
                         "router-id": "000000000006"
                     },
                     "ip-reachability-tlv": "10.0.68.0",
                     "ip-reach-prefix": "10.0.68.0/24",
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
                         "router-id": "000000000006"
                     },
                     "ip-reachability-tlv": "10.0.56.0",
                     "ip-reach-prefix": "10.0.56.0/24",
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
         "node_id": "1003232235769000000000005",
         "node_details": {
             "ls-nlri-type": "bgpls-node",
             "l3-routing-topology": 100,
             "protocol-id": 2,
             "node-descriptors": {
                 "autonomous-system": 100,
                 "bgp-ls-identifier": "3232235769",
                 "router-id": "000000000005"
             },
             "nexthop": "192.168.0.249"
         },
         "node_attributes": {
             "origin": "igp",
             "local-preference": 100,
             "bgp-ls": {
                 "area-id": "490001",
                 "local-te-router-ids": [
                     "10.255.255.5"
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
                         "router-id": "000000000005"
                     },
                     "remote-node-descriptors": {
                         "autonomous-system": 100,
                         "bgp-ls-identifier": "3232235769",
                         "router-id": "000000000006"
                     },
                     "interface-address": {
                         "interface-address": "10.0.56.5"
                     },
                     "neighbor-address": {
                         "neighbor-address": "10.0.56.6"
                     }
                 },
                 "link_attributes": {
                     "origin": "igp",
                     "local-preference": 100,
                     "bgp-ls": {
                         "local-te-router-ids": [
                             "10.255.255.5"
                         ],
                         "remote-te-router-id": "10.255.255.6",
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
             },
             {
                 "link": {
                     "ls-nlri-type": "bgpls-link",
                     "l3-routing-topology": 100,
                     "protocol-id": 2,
                     "local-node-descriptors": {
                         "autonomous-system": 100,
                         "bgp-ls-identifier": "3232235769",
                         "router-id": "000000000005"
                     },
                     "remote-node-descriptors": {
                         "autonomous-system": 100,
                         "bgp-ls-identifier": "3232235769",
                         "router-id": "000000000004"
                     },
                     "interface-address": {
                         "interface-address": "10.0.45.5"
                     },
                     "neighbor-address": {
                         "neighbor-address": "10.0.45.4"
                     }
                 },
                 "link_attributes": {
                     "origin": "igp",
                     "local-preference": 100,
                     "bgp-ls": {
                         "local-te-router-ids": [
                             "10.255.255.5"
                         ],
                         "remote-te-router-id": "10.255.255.4",
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
                         "router-id": "000000000005"
                     },
                     "ip-reachability-tlv": "10.255.255.5",
                     "ip-reach-prefix": "10.255.255.5/32",
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
                         "router-id": "000000000005"
                     },
                     "ip-reachability-tlv": "10.0.56.0",
                     "ip-reach-prefix": "10.0.56.0/24",
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
                         "router-id": "000000000005"
                     },
                     "ip-reachability-tlv": "10.0.45.0",
                     "ip-reach-prefix": "10.0.45.0/24",
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
         "node_id": "1003232235769000000000004",
         "node_details": {
             "ls-nlri-type": "bgpls-node",
             "l3-routing-topology": 100,
             "protocol-id": 2,
             "node-descriptors": {
                 "autonomous-system": 100,
                 "bgp-ls-identifier": "3232235769",
                 "router-id": "000000000004"
             },
             "nexthop": "192.168.0.249"
         },
         "node_attributes": {
             "origin": "igp",
             "local-preference": 100,
             "bgp-ls": {
                 "area-id": "490001",
                 "local-te-router-ids": [
                     "10.255.255.4"
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
                         "router-id": "000000000004"
                     },
                     "remote-node-descriptors": {
                         "autonomous-system": 100,
                         "bgp-ls-identifier": "3232235769",
                         "router-id": "000000000007"
                     },
                     "interface-address": {
                         "interface-address": "10.0.47.4"
                     },
                     "neighbor-address": {
                         "neighbor-address": "10.0.47.7"
                     }
                 },
                 "link_attributes": {
                     "origin": "igp",
                     "local-preference": 100,
                     "bgp-ls": {
                         "local-te-router-ids": [
                             "10.255.255.4"
                         ],
                         "remote-te-router-id": "10.255.255.7",
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
             },
             {
                 "link": {
                     "ls-nlri-type": "bgpls-link",
                     "l3-routing-topology": 100,
                     "protocol-id": 2,
                     "local-node-descriptors": {
                         "autonomous-system": 100,
                         "bgp-ls-identifier": "3232235769",
                         "router-id": "000000000004"
                     },
                     "remote-node-descriptors": {
                         "autonomous-system": 100,
                         "bgp-ls-identifier": "3232235769",
                         "router-id": "000000000002"
                     },
                     "interface-address": {
                         "interface-address": "10.0.24.4"
                     },
                     "neighbor-address": {
                         "neighbor-address": "10.0.24.1"
                     }
                 },
                 "link_attributes": {
                     "origin": "igp",
                     "local-preference": 100,
                     "bgp-ls": {
                         "local-te-router-ids": [
                             "10.255.255.4"
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
             },
             {
                 "link": {
                     "ls-nlri-type": "bgpls-link",
                     "l3-routing-topology": 100,
                     "protocol-id": 2,
                     "local-node-descriptors": {
                         "autonomous-system": 100,
                         "bgp-ls-identifier": "3232235769",
                         "router-id": "000000000004"
                     },
                     "remote-node-descriptors": {
                         "autonomous-system": 100,
                         "bgp-ls-identifier": "3232235769",
                         "router-id": "000000000005"
                     },
                     "interface-address": {
                         "interface-address": "10.0.45.4"
                     },
                     "neighbor-address": {
                         "neighbor-address": "10.0.45.5"
                     }
                 },
                 "link_attributes": {
                     "origin": "igp",
                     "local-preference": 100,
                     "bgp-ls": {
                         "local-te-router-ids": [
                             "10.255.255.4"
                         ],
                         "remote-te-router-id": "10.255.255.5",
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
                         "router-id": "000000000004"
                     },
                     "ip-reachability-tlv": "10.255.255.4",
                     "ip-reach-prefix": "10.255.255.4/32",
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
                         "router-id": "000000000004"
                     },
                     "ip-reachability-tlv": "10.0.47.0",
                     "ip-reach-prefix": "10.0.47.0/24",
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
                         "router-id": "000000000004"
                     },
                     "ip-reachability-tlv": "10.0.45.0",
                     "ip-reach-prefix": "10.0.45.0/24",
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
                         "router-id": "000000000004"
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
             }
         ]
     },
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
                         "router-id": "000000000003"
                     },
                     "interface-address": {
                         "interface-address": "10.0.23.1"
                     },
                     "neighbor-address": {
                         "neighbor-address": "10.0.23.3"
                     }
                 },
                 "link_attributes": {
                     "origin": "igp",
                     "local-preference": 100,
                     "bgp-ls": {
                         "local-te-router-ids": [
                             "10.255.255.2"
                         ],
                         "remote-te-router-id": "10.255.255.3",
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
             },
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
                         "router-id": "000000000004"
                     },
                     "interface-address": {
                         "interface-address": "10.0.24.1"
                     },
                     "neighbor-address": {
                         "neighbor-address": "10.0.24.4"
                     }
                 },
                 "link_attributes": {
                     "origin": "igp",
                     "local-preference": 100,
                     "bgp-ls": {
                         "local-te-router-ids": [
                             "10.255.255.2"
                         ],
                         "remote-te-router-id": "10.255.255.4",
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
             },
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
         "node_id": "1003232235769000000000003",
         "node_details": {
             "ls-nlri-type": "bgpls-node",
             "l3-routing-topology": 100,
             "protocol-id": 2,
             "node-descriptors": {
                 "autonomous-system": 100,
                 "bgp-ls-identifier": "3232235769",
                 "router-id": "000000000003"
             },
             "nexthop": "192.168.0.249"
         },
         "node_attributes": {
             "origin": "igp",
             "local-preference": 100,
             "bgp-ls": {
                 "area-id": "490001",
                 "local-te-router-ids": [
                     "10.255.255.3"
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
                         "router-id": "000000000003"
                     },
                     "remote-node-descriptors": {
                         "autonomous-system": 100,
                         "bgp-ls-identifier": "3232235769",
                         "router-id": "000000000002"
                     },
                     "interface-address": {
                         "interface-address": "10.0.23.3"
                     },
                     "neighbor-address": {
                         "neighbor-address": "10.0.23.1"
                     }
                 },
                 "link_attributes": {
                     "origin": "igp",
                     "local-preference": 100,
                     "bgp-ls": {
                         "local-te-router-ids": [
                             "10.255.255.3"
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
                         "router-id": "000000000003"
                     },
                     "ip-reachability-tlv": "10.255.255.3",
                     "ip-reach-prefix": "10.255.255.3/32",
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
                         "router-id": "000000000003"
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