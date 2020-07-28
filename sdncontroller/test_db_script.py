from modules import dbfunctions
from models import BGPLSLink
import json


node = dbfunctions.get_bgpls_node("1003232235769000000000005")
print(json.dumps(node.as_dict(), indent=4))

#node = dbfunctions.get_bgpls_node("1003232235769000000000005")
#print(node.bgpls_links.all())

"""
dbfunctions.delete_bgpls_nodes_all()
## Test to: Add node... Add Link to Node... Confirm relationship has been made in DB
node = dbfunctions.add_bgpls_node("1003232235769000000000005")
print("Node: {}".format(node))

print(dbfunctions.delete_bgpls_link(1))

new_link = BGPLSLink(l3_nlri_type="l3-route", local_asn=100, local_router_id="1.1.1.1")
print("Link (Class) prior to database add: {}".format(new_link))
link = dbfunctions.add_bgpls_link(node, new_link)
print("Link added into Database referencing id: {}".format(link))

print("Node {} all BGPLS Links: {}".format(node.node_id, node.bgpls_links.all()))
"""

#print(link.bgplsnode)
#bgpls_node = dbfunctions.get_bgpls_node("1003232235769000000000001")
#print(bgpls_node.id)
#new_link = BGPLSLink(l3_nlri_type="l3-route", local_asn=100, local_router_id="1.1.1.1", node_id=bgpls_node.id)
#inserted_link = dbfunctions.add_bgpls_link(new_link))
#link = dbfunctions.get_bgpls_link(1)
#print(link.node_id.l3_nlri_type)
#print(dbfunctions.add_bgpsls_node("1003232235769000000000005"))
#print(dbfunctions.add_bgpls_link("1003232235769000000000009", new_link))
#link = dbfunctions.get_bgpls_link(1)
#print(vars(link))
#node = dbfunctions.get_bgpls_node("1003232235769000000000001")
#print(vars(node))
#print(dbfunctions.get_bgpls_nodes_all())