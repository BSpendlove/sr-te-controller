from app import app
from flask import Blueprint, request
import json
from modules import dbfunctions
from modules.bgp_message_handler import (
    find_node_id_from_link,
    find_node_id_from_prefix,
    create_bgpls_withdraw
)

bp = Blueprint("bgpls-withdraw", __name__, url_prefix="/exabgp/update/bgpls/withdraw")

@bp.route("/all", methods=["POST"])
def withdraw_bgpls_message():
    # Withdraw MESSAGES can contain a different range of NLRI information, eg. a mix of links and prefix withdraws when a link goes down.. Therefore a single flask route must handle all NLRI types..
    if not request.is_json:
        return {"error": True, "message": "Incorrect format (must be JSON)."}

    data = request.get_json()
    #Sanity check to confirm message type is 'update' (eg. withdraw/announce update)
    if data["type"] == "update":
        app.logger.debug("Received Withdraw message... Raw data is:\n{}".format(json.dumps(data, indent=4)))
        try:
            withdraw_messages = create_bgpls_withdraw(data)
            #Check nodes:
            if withdraw_messages["nodes"]:
                pass
            if withdraw_messages["links"]:
                for link in withdraw_messages["links"]:
                    withdraw_link = dbfunctions.check_bgpls_link(link["node_id"], link)
                    if withdraw_link:
                        result = dbfunctions.delete_bgpls_link(withdraw_link.id)
                        app.logger.debug("withdraw_link is: {}\nResult: {}".format(withdraw_link, result))
            if withdraw_messages["prefixes_v4"]:
                for prefix in withdraw_messages["prefixes_v4"]:
                    withdraw_prefix = dbfunctions.check_bgpls_prefix_v4(prefix["node_id"], prefix)
                    if withdraw_prefix:
                        result = dbfunctions.delete_bgpls_prefix_v4(withdraw_prefix.id)
                        app.logger.debug("withdraw_prefix is: {}\nResult: {}".format(withdraw_prefix, result))
            if withdraw_messages["prefixes_v6"]:
                pass
        except Exception as error:
            app.logger.debug("Exception caught: {}".format(error))
    return data
