import database as db
import fitbit
import time
import datetime
import variables as v
import sys

def get_formatted_yesterday():
	yesterday = datetime.date.fromtimestamp(time.time() - 60*60*24)
	return yesterday.strftime('%Y-%m-%d')

def get_today_timestamp():
	today = datetime.datetime.now()
	return time.mktime((today.year, today.month, today.day, 0, 0, 0, 0, 0, 0))

def date_to_timestamp(date):# ex) 2016-09-22
	return time.mktime(datetime.datetime.strptime(date, "%Y-%m-%d").timetuple())

def user_login(access_token, refresh_token):
	user = fitbit.Fitbit(v.CLIENT_ID, v.CLIENT_SECRET, access_token=access_token, refresh_token=refresh_token)
	return user

def get_step(user, _date):# ex) 2016-09-22
	if _date == 'yesterday':
		__date = get_formatted_yesterday()
	else:
		__date = _date
	data = user.intraday_time_series('activities/steps', base_date=__date, detail_level='1min')
	result = list()
	for mindata in data['activities-steps-intraday']['dataset']:
		temp = dict()
		steps = int(str(mindata['value']))
		_time = str(mindata['time'])
		hour = int(_time.split(':')[0])
		minute = int(_time.split(':')[1])
		second = int(_time.split(':')[2])
		year = int(_date.split('-')[0])
		month = int(_date.split('-')[0])
		day = int(_date.split('-')[0])
		timestamp = time.mktime((year, month, day, hour, minute, second, 0, 0, 0))
		temp['value'] = steps
		temp['timestamp'] = timestamp
		result.append(temp)
	return result

def main():
	assert len(sys.argv) == 2, 'Usage : python step.py [YYYY-mm-dd]'
	assert get_today_timestamp() > date_to_timestamp(sys.argv[1]), 'Input previous day'
	for db_user in db.select_user():
		user = user_login(db_user['access_token'], db_user['refresh_token'])
		for steps in get_step(user, sys.argv[1]):
			db.insert_fitbit(user_id=db_user['user_id'], timestamp=steps['timestamp'], step=steps['value'])

main()
