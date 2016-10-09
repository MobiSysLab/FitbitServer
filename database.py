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
# if GPS.table_exists():
	# db.drop_table(GPS)
# if User.table_exists():
	# db.drop_table(User)
# if Fitbit.table_exists():
	# db.drop_table(Fitbit)

# db.create_table(GPS, safe=True)
# db.create_table(User, safe=True)
# db.create_table(Fitbit, safe=True)

def insert_gps(latitude, longitude, timestamp, user_id=None, key=None):
	try:
		if user_id is None and key is None:
			return {'success':False, 'error_type':'no key or user_id'}
		if key is not None:
			user_id = select_user(key=key)['user_id']
		if select_user(user_id=user_id)['count'] != 1:
			return {'success':False, 'error_type':'no user'}
		GPS.insert(user_id=user_id, latitude=latitude, longitude=longitude, timestamp=timestamp).execute()
		return {'success':True}
	except Exception, e:
		return {'success':False, 'error_type':e}

def insert_user(access_token, expires_in, refresh_token, scope, token_type, user_id, key):
	try:
		# insert new user
		query = select_user(user_id=user_id)
		print 'query'
		print query
		if query['count']==0:
			User.insert(access_token=access_token, expires_in=expires_in, refresh_token=refresh_token, scope=scope, token_type=token_type, user_id=user_id, key=key).execute()
			return {'success':True, 'exists':False}
		# update user
		elif query['count']==1:
			User.update(access_token=access_token, expires_in=expires_in, refresh_token=refresh_token, scope=scope, token_type=token_type, key=key).where(User.user_id==user_id).execute()
			return {'success':True, 'exists':True}
		return {'success':False, 'error_type':None}
	except Exception, e:
		return {'success':False, 'error_type':e}

def insert_fitbit(timestamp, step, user_id=None, key=None):
	try:
		if user_id is None and key is None:
			return {'success':False}
		if key is not None:
			user_id = select_user(key=key)['user_id']
		fitbit = Fitbit(user_id=user_id, timestamp=timestamp, step=step)
		fitbit.save()
		return {'success':True}
	except Exception, e:
		return {'success':False, 'error_type':e}

def select_gps_fitbit(start_timestamp, end_timestamp, user_id=None, key=None):
	try:
		if user_id is None and key is None:
			return {'success':False}
		if key is not None:
			user_id = select_user(key=key)['user_id']
		result = dict()
		result['user_id'] = user_id
		result['data'] = list()
		for data in Fitbit.select(Fitbit, GPS).join(GPS, JOIN.LEFT_OUTER, on = ((Fitbit.user_id==GPS.user_id)&(Fitbit.timestamp==GPS.timestamp))):
			temp = dict()
			temp['timestamp'] = data.timestamp
			temp['latitude'] = data.gps.latitude
			temp['longitude'] = data.gps.longitude
			temp['step'] = data.step
			result['data'].append(temp)
		result['success'] = True
		return result
	except Exception, e:
		return {'success':False, 'error_type':e}

def select_user(user_id=None, key=None):
	try:
		if user_id is None and key is None:
			result = list()
			query = User.select()
			for user in User.select():
				temp = dict()
				temp['user_id'] = user.user_id
				temp['access_token'] = user.access_token
				temp['expires_in'] = user.expires_in
				temp['refresh_token'] = user.refresh_token
				temp['scope'] = user.scope
				temp['token_type'] = user.token_type
				temp['key'] = user.key
				result.append(temp)
			return result
		# select by user_id
		result = dict()
		if user_id is not None:#using user_id
			query = User.select().where(User.user_id==user_id)
		else:#using key
			query = User.select().where(User.key==key)
		result['count'] = len(query)
		for user in query:
			result['user_id'] = user.user_id
			result['access_token'] = user.access_token
			result['expires_in'] = user.expires_in
			result['refresh_token'] = user.refresh_token
			result['scope'] = user.scope
			result['token_type'] = user.token_type
			result['key'] = user.key
		result['success'] = True
		return result
	except Exception, e:
		return {'success':False, 'error_type':str(e), 'count':-1}

def delete_user_info(user_id=None, key=None):
	try:
		assert user_id is not None or key is not None
		# delete by user_id
		result = {'success':True}
		if key is None:# user_id
			User.update(access_token=None, expires_in=None, refresh_token=None, scope=None, token_type=None, key=None).where(User.user_id==user_id).execute()
		else:
			User.update(access_token=None, expires_in=None, refresh_token=None, scope=None, token_type=None, key=None).where(User.key==key).execute()
		return result
	except Exception, e:
		return {'success':False, 'error_type':str(e)}
