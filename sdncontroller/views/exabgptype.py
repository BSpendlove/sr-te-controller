from app import app
from flask import Blueprint, request
from modules.dbfunctions import db_add_neighbor, db_delete_neighbor, db_get_neighbor, db_add_ted, db_delete_ted, db_get_ted, db_modify_ted
from modules.ted import build_ted, modify_ted, generate_ted_id
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
            app.logger.debug("Neighbor UP detected ({})... INITIAL_TOPOLOGY={}\nData Type is: {}".format(data["host"], INITIAL_TOPOLOGY, type(data)))
            neighbor = db_add_neighbor(data)
            INITIAL_TOPOLOGY = True
            return data

        if data["neighbor"]["state"] == "down":
            app.logger.debug("Neighbor DOWN detected ({})... INITIAL_TOPOLOGY={}\n".format(data["host"], INITIAL_TOPOLOGY))
            ted_id = generate_ted_id(data)
            try:
                if db_get_ted(ted_id):
                    delete_ted = db_delete_ted(ted_id)
                    app.logger.debug("Successfully deleted TED ({})".format(ted_id))
                else:
                    app.logger.debug("TED ID ({}) does not exist in database...".format(ted_id))
            except:
                app.logger.debug("Unable to delete TED ({})".format(ted_id))
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
        app.logger.debug("Received 'update' message from {}.".format(data["neighbor"]["address"]["peer"]))
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
                        topology_id = db_add_ted(id=ted_id, ted=new_topology)
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
            try:
                modify_ted(data)
            except Exception as error:
                app.logger.debug("Exception modifying TED/topology: {}".format(error))
            """
    return data

