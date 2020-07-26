from app import app, db
from models import (
    Neighbor
)

def db_add_neighbor(neighbor_data):
    neighbor = Neighbor(neighbor_data=neighbor_data)
    db.session.add(neighbor)
    db.session.commit()
    app.logger.debug("Added neighbor ({}) from database".format(neighbor))
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
