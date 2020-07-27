from app import app, db
from models import (
    Neighbor,
    TED
)

def db_add_neighbor(neighbor_data):
    neighbor = Neighbor(neighbor_data=neighbor_data)
    db.session.add(neighbor)
    db.session.commit()
    app.logger.debug("Added neighbor ({}) to database".format(neighbor))
    return neighbor

def db_delete_neighbor(id):
    neighbor = Neighbor.query.get(id)
    db.session.delete(neighbor)
    db.session.commit()
    app.logger.debug("Deleted neighbor ({}) from database".format(neighbor))
    return neighbor

def db_get_neighbor(id):
    neighbor = Neighbor.query.get(id)
    app.logger.debug("Get neighbor ({}) from database".format(neighbor))
    return neighbor

def db_delete_all_neighbors():
    neighbors = db.session.query(Neighbor).delete()
    app.logger.debug("Deleted all neighbors ({}) from database".format(neighbors))
    return neighbors

def db_add_ted(id, ted):
    topology = None
    new_topology = {}
    if isinstance(ted, list):
        for node in ted:
            node_id = node["node_id"]
            new_topology[node_id] = node
        topology = TED(id=id, ted=new_topology)
    else:
        topology = TED(id=id, ted=ted)
    db.session.add(topology)
    db.session.commit()
    app.logger.debug("Added TED ({}) to database".format(topology))
    return topology

def db_delete_ted(id):
    topology = TED.query.get(id)
    db.session.delete(topology)
    db.session.commit()
    app.logger.debug("Deleted TED ({}) from database".format(topology))
    return topology

def db_get_ted(id):
    topology = TED.query.get(id)
    app.logger.debug("Get TED ({}) from database".format(id))
    return topology

def db_modify_ted(id, ted):
    topology = TED.query.get(id)
    topology.ted = ted
    db.session.commit()
    app.logger.debug("Modified TED ({}) from database".format(topology))
    return topology
