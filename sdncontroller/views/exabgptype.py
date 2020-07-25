from app import app
from flask import Blueprint, request
from modules.dbfunctions import insert_state, insert_update, initial_topology
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
            INITIAL_TOPOLOGY = True
            return data

        if data["neighbor"]["state"] == "down":
            app.logger.debug("Neighbor DOWN detected ({})... INITIAL_TOPOLOGY={}\n".format(data["host"], INITIAL_TOPOLOGY))
            return data

        result = insert_state(data)
        app.logger.debug("Inserted 'state' message ({}) into database.\n{}".format(str(result.inserted_id), json.dumps(data, indent=4)))
        data["_id"] = str(result.inserted_id)

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
        if INITIAL_TOPOLOGY:
            TOPOLOGY.append(data)
            app.logger.debug("Appending 'initial_topology' message to TOPOLOGY.\n{}".format(json.dumps(data, indent=4)))
            if "eor" in data["neighbor"]:
                topology_id = initial_topology(TOPOLOGY)
                INITIAL_TOPOLOGY = False
                app.logger.debug("EOR detected ({}).\nInserted TOPOLOGY into initial_topology database. topology_id={},INITIAL_TOPOLOGY={}".format(data["host"], topology_id, INITIAL_TOPOLOGY))
                return topology_id

        result = insert_update(data)
        app.logger.debug("Inserted 'update' message ({}) into database.\n{}".format(str(result.inserted_id), json.dumps(data, indent=4)))
        data["_id"] = str(result.inserted_id)

    return data

