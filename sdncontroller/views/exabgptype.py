from app import app
from flask import Blueprint, request
from modules.dbfunctions import insert_state, insert_update
import json
import logging

app.logger.setLevel(logging.DEBUG)

bp = Blueprint("exabgp", __name__, url_prefix="/exabgp")

@bp.route("/state", methods=["POST"])
def exabgp_state():
    if not request.is_json:
        return {"error": True, "message": "Incorrect format (must be JSON)."}

    data = request.get_json()
    #Sanity check to confirm message type is 'state' (eg neighbor state up/down/connect)
    if data["type"] == "state":
        app.logger.debug("Inserting 'state' message into database.\n{}".format(json.dumps(data, indent=4)))
        result = insert_state(data)

        data["_id"] = str(result.inserted_id)

    return data

@bp.route("/update", methods=["POST"])
def exabgp_update():
    if not request.is_json:
        return {"error": True, "message": "Incorrect format (must be JSON)."}

    data = request.get_json()

    #Sanity check to confirm message type is 'update' (eg. withdraw/announce update)
    if data["type"] == "update":
        app.logger.debug("Inserting 'update' message into database.\n{}".format(json.dumps(data, indent=4)))
        result = insert_update(data)

        data["_id"] = str(result.inserted_id)

    return data
