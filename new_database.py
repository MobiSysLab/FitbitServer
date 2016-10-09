import cherrypy
from peewee import *
import datetime
import variables as v

db = MySQLDatabase(v.DATABASE,host=v.HOST,port=3306, user=v.USER, passwd=v.PASSWD)

class GPS(Model):
    user_id = TextField()
    latitude = TextField()
    longitude = TextField()
    timestamp = TimestampField()
    class Meta:
        database = db

class User(Model):
    access_token = TextField()
    expires_in = IntegerField()
    refresh_token = TextField()
    scope = TextField()
    token_type = TextField()
    user_id = TextField()
    key = TextField()
    class Meta:
        database = db

class Fitbit(Model):
    user_id = TextField()
    timestamp = TimestampField()
    step = IntegerField()
    class Meta:
        database = db


db.connect()
if GPS.table_exists():
    db.drop_table(GPS)
if User.table_exists():
    db.drop_table(User)
if Fitbit.table_exists():
    db.drop_table(Fitbit)

db.create_table(GPS, safe=True)
db.create_table(User, safe=True)
db.create_table(Fitbit, safe=True)
