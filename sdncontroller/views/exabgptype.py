from app import app
from flask import Blueprint, request
from modules.dbfunctions import db_add_neighbor, db_delete_neighbor, db_get_neighbor
from modules.ted import build_ted
import json
import logging

app.logger.setLevel(logging.DEBUG)

bp = Blueprint("exabgp", __name__, url_prefix="/exabgp")

INITIAL_TOPOLOGY = False
TOPOLOGY = []

@bp.route("/state", methods=["POST"])
def exabgp_state():
    global INITIAL_TOPOLOGY

    if not request.is_json:
        return {"error": True, "message": "Incorrect format (must be JSON)."}

    data = request.get_json()
    #Sanity check to confirm message type is 'state' (eg neighbor state up/down/connect)
    if data["type"] == "state":
        if data["neighbor"]["state"] == "up":
            app.logger.debug("Neighbor UP detected ({})... INITIAL_TOPOLOGY={}\n".format(data["host"], INITIAL_TOPOLOGY))
            neighbor = db_add_neighbor(data)
            INITIAL_TOPOLOGY = True
            return data

        if data["neighbor"]["state"] == "down":
            app.logger.debug("Neighbor DOWN detected ({})... INITIAL_TOPOLOGY={}\n".format(data["host"], INITIAL_TOPOLOGY))
            #Rewrite this code... to delete the correct neighbor...
            return data

    return data

@bp.route("/update", methods=["POST"])
def exabgp_update():
    global INITIAL_TOPOLOGY
    global TOPOLOGY

    if not request.is_json:
        return {"error": True, "message": "Incorrect format (must be JSON)."}

    data = request.get_json()
    #Sanity check to confirm message type is 'update' (eg. withdraw/announce update)
    if data["type"] == "update":
        app.logger.debug("Received 'update' message from {}".format(data["neighbor"]["address"]["peer"]))
        if INITIAL_TOPOLOGY:
            TOPOLOGY.append(data)
            app.logger.debug("Appending 'initial_topology' message to TOPOLOGY.\n{}".format(json.dumps(data, indent=4)))
            if "eor" in data["neighbor"]["message"]:
                INITIAL_TOPOLOGY = False
                new_topology = None
                topology_id = 123
                try:
                    new_topology = build_ted(TOPOLOGY)
                except Exception as error:
                    app.logger.debug("Exception building TED/topology: {}".format(error))
                app.logger.debug("EOR detected ({}).\nINITIAL_TOPOLOGY={}\nHere is what the topology looks like: {}".format(data["host"], INITIAL_TOPOLOGY, json.dumps(new_topology, indent=4)))
                if new_topology:
                    topology_id=1
                    if topology_id:
                        app.logger.debug("Successfully generated TED/Topology... Datbase ID = {}".format(topology_id))
                return {"ted_topology": new_topology }

    return data

