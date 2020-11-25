from app import app
from flask import Blueprint, request
from modules import dbfunctions
import json
import logging
import requests

bp = Blueprint("api", __name__, url_prefix="/api/v1")

@bp.route("/topology", methods=["GET"])
def get_bgpls_topology():
    nodes = dbfunctions.get_bgpls_nodes_all()
    ted_topology = [node.as_dict() for node in nodes]
    return json.dumps({"nodes": ted_topology}, indent=4)

@bp.route("/bgpls-node/sr_sid/<int:id>", methods=["GET"])
def bgpls_node_sr_sid(id):
    node = dbfunctions.get_bgpls_node_id(id)
    sr_sids = None

    if node:
        app.logger.debug("API TEST: node_id: {}\nnode_local_te_router_ids: {}".format(node.node_id, node.local_te_router_ids))
        prefix = dbfunctions.get_bgpls_node_routerid_prefix(node.id)
        if prefix:
            sr_sids = prefix.sr_sids

    return {"node": id, "sr_sids": sr_sids}

@bp.route("/deploy", methods=["POST"])
def deploy():
    if not request.is_json:
        return {"error": True, "message": "Incorrect format (must be JSON)."}

    data = request.get_json()

    if not "prefix" in data:
        return {"error": True, "message": "prefix not found."}
    if not "nexthop" in data:
        return {"error": True, "message": "nexthop not found."}
    if not "label_path" in data:
        return {"error": True, "message": "label path not found."}

    cmd = "neighbor 192.168.0.249 announce route {} next-hop {} label [ {} ]".format(data["prefix"], data["nexthop"], " ".join(map(str, data["label_path"])))
    output = requests.request(
        "POST",
        "http://192.168.0.16:5001/exabgp/cli/announce/label",
        json={"command": cmd}
    )

    app.logger.debug(output.text)
    results = json.loads(output.text)

    app.logger.debug(json.dumps(results, indent=4))
    return {"command": cmd, "exabgpapi_cli": results}
