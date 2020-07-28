from app import app
from flask import Blueprint, request
from modules import dbfunctions
from modules.bgp_message_handler import (
    create_bgp_state,
    create_bgp_node,
    create_bgp_link,
    create_bgp_prefix_v4,
    create_bgp_prefix_v6,
    find_node_id_from_link_update
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
        if "bgpls-node" in str(data):
            #Node Information
            bgp_node = create_bgp_node(data)
            app.logger.debug("BGP Node created for database...\n{}".format(json.dumps(bgp_node, indent=4)))
            node = dbfunctions.add_bgpls_node(bgp_node)
            app.logger.debug("Added BGP Node into database...\n{}".format(json.dumps(node.as_dict(), indent=4)))
        if "bgpls-link" in str(data):
            bgp_link = create_bgp_link(data)
            app.logger.debug("BGP Link created for database...\n{}".format(json.dumps(bgp_link, indent=4)))
            node_id = find_node_id_from_link_update(data)
            app.logger.debug("node_id is: {}".format(node_id))
            if node_id:
                link = dbfunctions.add_bgpls_link(node_id, bgp_link)
                app.logger.debug("Added BGP Link into database...\n{}".format(json.dumps(link.as_dict(), indent=4)))
        """
        if INITIAL_TOPOLOGY:
            TOPOLOGY.append(data)
            #app.logger.debug("Appending 'initial_topology' message to TOPOLOGY.\n{}".format(json.dumps(data, indent=4)))
            if "eor" in data["neighbor"]["message"]:
                ted_id = generate_ted_id(data)
                app.logger.debug("Generate ted_id ({}) from update...".format(ted_id))
                INITIAL_TOPOLOGY = False
                new_topology = None
                try:
                    new_topology = build_ted(TOPOLOGY)
                except Exception as error:
                    app.logger.debug("Exception building TED/topology: {}".format(error))
                app.logger.debug("EOR detected ({}).\nINITIAL_TOPOLOGY={}\nHere is what the topology looks like: {}".format(data["host"], INITIAL_TOPOLOGY, json.dumps(new_topology, indent=4)))
                if new_topology:
                    try:
                        pass
                        #topology_id = db_add_ted(id=ted_id, ted=new_topology)
                    except Exception as error:
                        app.logger.debug("Error adding TED ({}) topology in database... Error: {}".format(ted_id, error))
                    if topology_id:
                        app.logger.debug("Successfully generated TED/Topology... Datbase entry = {}".format(topology_id))
                return {"ted_topology": new_topology }
        else:
            app.logger.debug("UPDATE message json dump:\n{}".format(data))
            ted_id = generate_ted_id(data)
            app.logger.debug("Generate ted_id ({}) from update...".format(ted_id))
            """
    return data

