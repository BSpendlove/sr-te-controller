from app import app
from flask import Blueprint, request
from modules import dbfunctions
from modules.bgp_message_handler import (
    create_bgp_state,
    create_bgp_node,
    create_bgp_link,
    create_bgp_prefix_v4,
    create_bgp_prefix_v6,
    find_node_id_from_update
)
import json
import logging

app.logger.setLevel(logging.DEBUG)

bp = Blueprint("exabgp", __name__, url_prefix="/exabgp")

@bp.route("/check_nodes", methods=["GET"])
def get_nodes():
    nodes = dbfunctions.get_bgpls_nodes_all()
    return {"nodes": [node.as_dict() for node in nodes]}

@bp.route("/state", methods=["POST"])
def exabgp_state():
    if not request.is_json:
        return {"error": True, "message": "Incorrect format (must be JSON)."}

    data = request.get_json()
    #Sanity check to confirm message type is 'state' (eg neighbor state up/down/connect)
    if data["type"] == "state":
        if data["neighbor"]["state"] == "up":
            app.logger.debug("Neighbor UP detected ({})...".format(data["host"]))
            bgp_state = create_bgp_state(data)
            app.logger.debug("BGP State created for database...\n{}".format(json.dumps(bgp_state, indent=4)))
            state = dbfunctions.add_bgp_state(bgp_state)
            if state:
                app.logger.debug("Added BGP State into database...\n{}".format(json.dumps(state.as_dict(), indent=4)))
            else:
                app.logger.debug("Unable to add BGP State into database...")
            return data

        if data["neighbor"]["state"] == "down":
            app.logger.debug("Neighbor DOWN detected ({})...".format(data["host"]))
            return data

    return data

@bp.route("/update", methods=["POST"])
def exabgp_update():
    if not request.is_json:
        return {"error": True, "message": "Incorrect format (must be JSON)."}

    data = request.get_json()
    #Sanity check to confirm message type is 'update' (eg. withdraw/announce update)
    if data["type"] == "update":
        app.logger.debug("Received 'update' message from {}.".format(data["neighbor"]["address"]["peer"]))
        app.logger.debug("Data Output debug:\n{}".format(json.dumps(data, indent=4)))
        if "withdraw" in str(data):
            app.logger.debug("Withdraw detected...")
            return dbfunctions.withdraw_update(data)
        if "bgpls-node" in str(data):
            #Node Information
            bgp_node = create_bgp_node(data)
            app.logger.debug("BGP Node created for database...\n{}".format(json.dumps(bgp_node, indent=4)))
            node = dbfunctions.add_bgpls_node(bgp_node)
            app.logger.debug("Added BGP Node into database...\n{}".format(json.dumps(node.as_dict(), indent=4)))
        if "bgpls-link" in str(data):
            bgp_link = create_bgp_link(data)
            app.logger.debug("BGP Link created for database...\n{}".format(json.dumps(bgp_link, indent=4)))
            node_id = find_node_id_from_update(data)
            app.logger.debug("node_id is: {}".format(node_id))
            link = dbfunctions.add_bgpls_link(bgp_link["node_id"], bgp_link)
            app.logger.debug("Added BGP Link into database...\n{}".format(json.dumps(link.as_dict(), indent=4)))
        if "bgpls-prefix-v4" in str(data):
            bgp_prefix = create_bgp_prefix_v4(data)
            app.logger.debug("BGP Prefix(es) created for database...\n{}".format(json.dumps(bgp_prefix, indent=4)))
            for prefix in bgp_prefix:
                app.logger.debug("--------------- for prefix in bgp_prefix:\nPrefix: {}".format(json.dumps(prefix, indent=4)))
                output = dbfunctions.add_bgpls_prefix_v4(prefix["node_id"], prefix)
                app.logger.debug("Added BGP Prefix into database...\n{}".format(json.dumps(output.as_dict(), indent=4)))

    return data

