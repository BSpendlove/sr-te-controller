from config import Config
from flask import Flask, request
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

from models import db
migrate = Migrate(app, db)

from models import BGPLSNode, BGPLSLink, BGPLSPrefixV4
from views import exabgptype as exabgp_view

db.init_app(app)
db.create_all()

@app.route("/", methods=["GET"])
def index():
    return "test"

if __name__ == "__main__":
    app.register_blueprint(exabgp_view.bp)
    app.run(host="0.0.0.0", port=5000, debug=True)
