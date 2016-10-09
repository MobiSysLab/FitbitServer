import matplotlib.pyplot as plt
import database as db
import datetime
import time
import sys

def get_yesterday_timestamp():
    yesterday = datetime.date.fromtimestamp(time.time() - 60*60*24)
    return time.mktime(yesterday.timetuple())

def get_timestamp(day):
    return time.mktime(datetime.datetime.strptime(day, "%Y-%m-%d").timetuple())

assert len(sys.argv) == 2, 'Usage : python step.py [YYYY-mm-dd]'
assert get_today_timestamp() > date_to_timestamp(sys.argv[1]), 'Input previous day'

day = sys.argv[1]

for user in db.select_user():#time='2016-09-09' format or yesterday
    user_id = user['user_id']
    if day == 'yesterday':
        timestamp = get_yesterday_timestamp()
    else:
        timestamp = get_timestamp(day)
    print timestamp
    print timestamp+24*60*60-60
    result = db.select_gps_fitbit(timestamp, timestamp+24*60*60-60, user_id=user_id)
    x = list()
    y = list()
    if not result['success']:
        print result['error_type']
    else:
        for data in result['data']:
            x.append(time.mktime(data['timestamp'].timetuple()))
            y.append(data['step'])
        plt.plot(x, y)
        plt.grid(True)
        plt.show()



