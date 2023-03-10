import sqlalchemy as db
from config import connections

def get_engine(connection_name: str):
    engine = db.create_engine(connections[connection_name])
    return engine