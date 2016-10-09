import database as db

# result = db.select_user(user_id='user_id')
# if not result['success'] or result['count'] != 0:
#     print 'select_user with user_id error(no user)'

# result = db.select_user(key='key')
# if not result['success'] or result['count'] != 0:
#     print 'select_user with key error(no user)'

# result = db.insert_user(access_token='', expires_in='123', refresh_token='test_refresh_token', scope='test_scope', token_type='test_token_type', user_id='test_user_id', key='test_key')
# if not result['success']:
#     print 'insert_user error(no user)'

# result = db.insert_user(access_token='test_access_token2', expires_in='1234', refresh_token='test_refresh_token2', scope='test_scope2', token_type='test_token_type2', user_id='test_user_id', key='test_key2')
# if not result['success']:
#     print 'insert_user error(update columns)'

# result = db.select_user(user_id='test_user_id')
# if not result['success'] or result['count'] == 0:
#     print 'select_user error(yes user using user_id)'

# result = db.select_user(key='test_key2')
# if not result['success'] or result['count'] == 0:
#     print 'select_user error(yes user using key)'

# result = db.insert_gps(user_id='user_id', latitude='1234', longitude='12345', timestamp='1234567890')
# if result['success']:
#     print 'insert_gps error(wrong user using user_id)'

# result = db.insert_gps(key='keyyyy', latitude='1234', longitude='12345', timestamp='1234567890')
# if result['success']:
#     print 'insert_gps error(wrong user using key)'

# result = db.insert_gps(user_id='test_user_id', latitude='1234.0', longitude=float('12345.0'), timestamp=float('1234567890'))
# if not result['success']:
#     print result['error_type']
#     print 'insert_gps error(using user_id)'

# result = db.insert_gps(key='test_key2', latitude='1234.90', longitude=float('12345.0'), timestamp=float('1234567890'))
# if not result['success']:
#     print result['error_type']
#     print 'insert_gps error(using key)'

#result = db.select_gps_fitbit('1474815600', '1474815720', user_id='4WPSBP')

# result = db.delete_user_info(user_id='4WPSBP')
# print result
# result = db.delete_user_info(key='3ebb48b427c0b56aed9d9b142de7debf')
# print result

# import step
# print step.get_yesterday()
# user = step.user_login('eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI0V1BTQlAiLCJhdWQiOiIyMjdaRkwiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJ3aHIgd3BybyB3bnV0IHdzbGUgd3dlaSB3c29jIHdhY3Qgd3NldCB3bG9jIiwiZXhwIjoxNDc0OTgwNDA5LCJpYXQiOjE0NzQ5NTE2MDl9.WGixQiED8SfKzaUHVLawWu8bcyusiFHQmaZp1G5bSrc', '2522b2bcded92c3163bc8e5d54baee46c2ba1be17bd17448e9ffa0b63207f0df')
# print step.get_step(user)
