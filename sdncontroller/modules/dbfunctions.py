import env_file
import json
import pymongo
from app import app
from bson import json_util

env_creds = env_file.get(path="env/db")
mongo_client = pymongo.MongoClient("mongodb://{}:{}@{}:27017/".format(env_creds["MONGO_USERNAME"], env_creds["MONGO_PASSWORD"], env_creds["MONGO_HOST"]))

DEFAULT_DATABASE = mongo_client["exabgp"]

def insert_state(state_msg):
    state = DEFAULT_DATABASE["state"]
    result = state.insert_one(json.loads(json_util.dumps(state_msg)))
    return result

def insert_update(update_msg):
    update = DEFAULT_DATABASE["update"]
    result = update.insert_one(json.loads(json_util.dumps(update_msg)))
    return result

def initial_topology(topology):
    topo = DEFAULT_DATABASE["initial_topology"]
    result = topo.insert_one(json.loads(json_util.dumps(topology)))
    return result
