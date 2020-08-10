from app import app
from flask import Blueprint, request
import json
import logging

bp = Blueprint("bgpls-withdraw", __name__, url_prefix="/exabgp/update/bgpls/withdraw")

@bp.route("/node", methods=["POST"])
def withdraw_bgpls_node():
    if not request.is_json:
        return {"error": True, "message": "Incorrect format (must be JSON)."}

    data = request.get_json()
    #Sanity check to confirm message type is 'update' (eg. withdraw/announce update)
    if data["type"] == "update":
        if "bgpls-node" in str(data):
            app.logger.debug("Recevied Node withdraw")
    return data

@bp.route("/link", methods=["POST"])
def withdraw_bgpls_link():
    if not request.is_json:
        return {"error": True, "message": "Incorrect format (must be JSON)."}

    data = request.get_json()
    #Sanity check to confirm message type is 'update' (eg. withdraw/announce update)
    if data["type"] == "update":
        if "bgpls-link" in str(data):
            app.logger.debug("Recevied Link withdraw")
    return data

@bp.route("/prefixv4", methods=["POST"])
def withdraw_bgpls_prefixv4():
    if not request.is_json:
        return {"error": True, "message": "Incorrect format (must be JSON)."}

    data = request.get_json()
    #Sanity check to confirm message type is 'update' (eg. withdraw/announce update)
    if data["type"] == "update":
        if "bgpls-prefix-v4" in str(data):
            app.logger.debug("Received Prefix V4 Withdraw")

    return data

@bp.route("/prefixv6", methods=["POST"])
def withdraw_bgpls_prefixv6():
    if not request.is_json:
        return {"error": True, "message": "Incorrect format (must be JSON)."}

    data = request.get_json()
    #Sanity check to confirm message type is 'update' (eg. withdraw/announce update)
    if data["type"] == "update":
        if "bgpls-prefix-v6" in str(data):
            app.logger.debug("Received Prefix V6 withdraw")

    return data

