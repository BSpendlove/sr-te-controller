from app import app
from flask import Blueprint, request
from modules import dbfunctions
from modules.bgp_message_handler import (
    create_bgpls_node,
    create_bgpls_link,
    create_bgpls_prefix_v4,
    create_bgpls_prefix_v6,
    find_node_id_from_update
)
import json
import logging

bp = Blueprint("bgpls-announce", __name__, url_prefix="/exabgp/update/bgpls/announce")

@bp.route("/node", methods=["POST"])
def announce_bgpls_node():
    if not request.is_json:
        return {"error": True, "message": "Incorrect format (must be JSON)."}

    data = request.get_json()
    if data["type"] == "update":
        if "bgpls-node" in str(data):
            #Node Information
            bgp_node = create_bgpls_node(data)
            node = dbfunctions.add_bgpls_node(bgp_node)
            app.logger.debug("Added BGPLSNode {} to database...".format(node.id))
    return data

@bp.route("/link", methods=["POST"])
def announce_bgpls_link():
    if not request.is_json:
        return {"error": True, "message": "Incorrect format (must be JSON)."}

    data = request.get_json()
    #app.logger.debug("Full link update is:\n{}".format(json.dumps(data, indent=4)))
    if data["type"] == "update":
        if "bgpls-link" in str(data):
            bgp_link = create_bgpls_link(data)
            node_id = find_node_id_from_update(data)
            link = dbfunctions.add_bgpls_link(bgp_link["node_id"], bgp_link)
            app.logger.debug("Added BGPLSLink ({}) to database for node {}".format(link.id, node_id))
    return data

@bp.route("/prefixv4", methods=["POST"])
def announce_bgpls_prefixv4():
    if not request.is_json:
        return {"error": True, "message": "Incorrect format (must be JSON)."}

    data = request.get_json()
    if data["type"] == "update":
        if "bgpls-prefix-v4" in str(data):
            bgp_prefix = create_bgpls_prefix_v4(data)
            for prefix in bgp_prefix:
                output = dbfunctions.add_bgpls_prefix_v4(prefix["node_id"], prefix)
                app.logger.debug("Added BGPLSPrefixV4 {} to database for node {}".format(output.id, prefix["node_id"]))

    return data

@bp.route("/prefixv6", methods=["POST"])
def announce_bgpls_prefixv6():
    if not request.is_json:
        return {"error": True, "message": "Incorrect format (must be JSON)."}

    data = request.get_json()
    if data["type"] == "update":
        if "bgpls-prefix-v6" in str(data):
            bgp_prefix = create_bgpls_prefix_v6(data)
            for prefix in bgp_prefix:
                output = dbfunctions.add_bgpls_prefix_v6(prefix["node_id"], prefix)
                app.logger.debug("Added BGPLSPrefixV6 {} to database for node {}".format(output.id, prefix["node_id"]))

    return data
