from app import db
from dataclasses import dataclass
from modules.jsonencoder import JsonEncodedDict

class Neighbor(db.Model):
    """ BGP Neighbor Model """
    id = db.Column(db.Integer, primary_key=True)
    neighbor_data = db.Column(JsonEncodedDict)

    def __repr__(self):
        return '<ExaBGP Neighbor {}>'.format(self.id)

class TED(db.Model):
    """ TED Model """
    id = db.Column(db.String, primary_key=True) # Rest in peace... Currently using local AS + local IP + remote AS + remote IP to identify the unique TED
    ted = db.Column(JsonEncodedDict)

    def __repr__(self):
        return '<ExaBGP TED {}>'.format(self.id)
