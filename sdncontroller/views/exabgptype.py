from flask import Blueprint, request
from app import app
import json
import logging

app.logger.setLevel(logging.DEBUG)

bp = Blueprint("exabgp", __name__, url_prefix="/exabgp")

@bp.route("/state", methods=["POST"])
def exabgp_state():
    if not request.is_json:
        return {"error": True, "message": "Incorrect format (must be JSON)."}

    data = request.get_json()
    app.logger.debug(json.dumps(data, indent=4))
    #Sanity check to confirm message type is 'state' (eg neighbor state up/down/connect)
    if data["type"] == "state":
        pass

    return data

@bp.route("/update", methods=["POST"])
def exabgp_update():
    if not request.is_json:
        return {"error": True, "message": "Incorrect format (must be JSON)."}

    data = request.get_json()
    app.logger.debug(json.dumps(data, indent=4))

    #Sanity check to confirm message type is 'update' (eg. withdraw/announce update)
    if data["type"] == "update":
        pass

    return data
