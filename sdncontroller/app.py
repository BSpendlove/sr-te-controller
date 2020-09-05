from config import Config
from flask import Flask, request, render_template
from flask_migrate import Migrate
import json
import logging

app = Flask(__name__)
app.config.from_object(Config)

app.logger.setLevel(logging.DEBUG)

from models import db
migrate = Migrate(app, db)

from models import BGPLSNode, BGPLSLink, BGPLSPrefixV4
from modules import dbfunctions
from modules.ted import build_visual_ted

from views.exabgp.neighbor import state as bgp_state
from views.exabgp.update.bgpls import announce as bgpls_announce
from views.exabgp.update.bgpls import withdraw as bgpls_withdraw
from views import api as sr_te_api

db.init_app(app)
db.create_all()

@app.route("/", methods=["GET"])
def index():
    nodes = dbfunctions.get_bgpls_nodes_all()
    ted_topology = [node for node in nodes]
    basic_ted_topology = [node.as_dict_basic() for node in nodes]
    app.logger.debug("This is what nodes look like:\n{}".format(str(nodes)))
    topology = build_visual_ted(ted_topology)
    app.logger.debug("topology:\n{}".format(json.dumps(topology, indent=4)))
    return render_template("index.html", ted=json.dumps(basic_ted_topology,indent=4), ted_json=topology)

if __name__ == "__main__":
    app.register_blueprint(bgp_state.bp)
    app.register_blueprint(bgpls_announce.bp)
    app.register_blueprint(bgpls_withdraw.bp)
    app.register_blueprint(sr_te_api.bp)
    app.run(host="0.0.0.0", port=5000, debug=True)
