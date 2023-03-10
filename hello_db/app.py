import sqlalchemy as db
import db_connector

engine = db_connector.get_engine('sql_lite_abc')
metadata = db.MetaData()
engine.connect()
census = db.Table('census', metadata, autoload = True, autoload_with = engine)

'''
engine = db.create_engine('sqlite:///census.sqlite')
connection = engine.connect()
metadata = db.MetaData()
census = db.Table('census', metadata, autoload=True, autoload_with=engine)
'''