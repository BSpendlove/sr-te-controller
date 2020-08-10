from app import app
from flask import Blueprint, request
from modules import dbfunctions
from modules.bgp_message_handler import (
    create_bgp_node,
    create_bgp_link,
    create_bgp_prefix_v4,
    create_bgp_prefix_v6,
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
    #Sanity check to confirm message type is 'update' (eg. withdraw/announce update)
    if data["type"] == "update":
        app.logger.debug("Received 'update' message from {}.".format(data["neighbor"]["address"]["peer"]))
        app.logger.debug("Data Output debug:\n{}".format(json.dumps(data, indent=4)))
        if "bgpls-node" in str(data):
            #Node Information
            bgp_node = create_bgp_node(data)
            app.logger.debug("BGP Node created for database...\n{}".format(json.dumps(bgp_node, indent=4)))
            node = dbfunctions.add_bgpls_node(bgp_node)
            app.logger.debug("Added BGP Node into database...\n{}".format(json.dumps(node.as_dict(), indent=4)))
    return data

@bp.route("/link", methods=["POST"])
def announce_bgpls_link():
    if not request.is_json:
        return {"error": True, "message": "Incorrect format (must be JSON)."}

    data = request.get_json()
    #Sanity check to confirm message type is 'update' (eg. withdraw/announce update)
    if data["type"] == "update":
        if "bgpls-link" in str(data):
            bgp_link = create_bgp_link(data)
            app.logger.debug("BGP Link created for database...\n{}".format(json.dumps(bgp_link, indent=4)))
            node_id = find_node_id_from_update(data)
            app.logger.debug("node_id is: {}".format(node_id))
            link = dbfunctions.add_bgpls_link(bgp_link["node_id"], bgp_link)
            app.logger.debug("Added BGP Link into database...\n{}".format(json.dumps(link.as_dict(), indent=4)))
    return data

@bp.route("/prefixv4", methods=["POST"])
def announce_bgpls_prefixv4():
    if not request.is_json:
        return {"error": True, "message": "Incorrect format (must be JSON)."}

    data = request.get_json()
    #Sanity check to confirm message type is 'update' (eg. withdraw/announce update)
    if data["type"] == "update":
        if "bgpls-prefix-v4" in str(data):
            bgp_prefix = create_bgp_prefix_v4(data)
            app.logger.debug("BGP Prefix(es) V4 created for database...\n{}".format(json.dumps(bgp_prefix, indent=4)))
            for prefix in bgp_prefix:
                output = dbfunctions.add_bgpls_prefix_v4(prefix["node_id"], prefix)
                app.logger.debug("Added BGP Prefix V4 into database...\n{}".format(json.dumps(output.as_dict(), indent=4)))

    return data

@bp.route("/prefixv6", methods=["POST"])
def announce_bgpls_prefixv6():
    if not request.is_json:
        return {"error": True, "message": "Incorrect format (must be JSON)."}

    data = request.get_json()
    #Sanity check to confirm message type is 'update' (eg. withdraw/announce update)
    if data["type"] == "update":
        if "bgpls-prefix-v6" in str(data):
            bgp_prefix = create_bgp_prefix_v6(data)
            app.logger.debug("BGP Prefix(es) V6 created for database...\n{}".format(json.dumps(bgp_prefix, indent=4)))
            for prefix in bgp_prefix:
                output = dbfunctions.add_bgpls_prefix_v6(prefix["node_id"], prefix)
                app.logger.debug("Added BGP Prefix V6 into database...\n{}".format(json.dumps(output.as_dict(), indent=4)))

    return data

