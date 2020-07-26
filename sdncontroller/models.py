from app import db
from dataclasses import dataclass
from modules.jsonencoder import JsonEncodedDict

class Neighbor(db.Model):
    """ BGP Neighbor Model """
    id = db.Column(db.Integer, primary_key=True)
    neighbor_data = db.Column(JsonEncodedDict)

    def __repr__(self):
        return '<ExaBGP Neighbor {}>'.format(self.id)
