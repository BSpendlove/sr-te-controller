from app import app
from flask import Blueprint, request
from modules import dbfunctions
from modules.bgp_message_handler import create_bgp_state
import json
import logging

bp = Blueprint("state", __name__, url_prefix="/exabgp/neighbor/state")

@bp.route("/down", methods=["POST"])
def neighbor_down():
    if not request.is_json:
        return {"error": True, "message": "Incorrect format (must be JSON)."}

    data = request.get_json()
    if data["type"] == "state":
        if data["neighbor"]["state"] == "down":
            app.logger.debug("Neighbor DOWN detected ({})...".format(data["host"]))

    # Implement logic to clear the database (BGPLSNode and the relevant BGPLSLinks+PrefixesV4/V6 learned by the specific neighbor
    return data

@bp.route("/up", methods=["POST"])
def neighbor_up():
    if not request.is_json:
        return {"error": True, "message": "Incorrect format (must be JSON)."}

    data = request.get_json()
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

@bp.route("/connected", methods=["POST"])
def neighbor_connected():
    if not request.is_json:
        return {"error": True, "message": "Incorrect format (must be JSON)."}

    data = request.get_json()
    if data["type"] == "state":
        if data["neighbor"]["state"] == "connected":
            app.logger.debug("Neighbor CONNECTED detected ({})...".format(data["host"]))

    return data
