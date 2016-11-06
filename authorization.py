import requests
import simplejson as json
import time
import hmac
import database as db

url = 'https://api.fitbit.com/oauth2/token'
headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'Basic MjI3WkZMOmQyZDI3NjBmZWZiOTU0ZGVjZTZhNDI3OTk1OTRiYjYw'}
payloads = {'redirect_uri': 'http://10.0.2.2:8080/callback', 'clientId':'227ZFL', 'grant_type':'authorization_code'}# append code

def get_token(code):
    payloads['code'] = code
    response = requests.post(url, headers=headers, data=payloads, verify=False)
    json_response = json.loads(response.text)
    print '***************'
    print response.content
    print '***************'
    if 'success' in json_response:
        return json.loads(response.text)
    access_token = json_response['access_token']
    expires_in = json_response['expires_in']
    refresh_token = json_response['refresh_token']
    scope = json_response['scope']
    token_type = json_response['token_type']
    user_id = json_response['user_id']
    json_response['success'] = True
    return json_response

def make_key(user_id):
    timestamp = int(time.time())
    key = hmac.new(str(user_id)+str(timestamp)).hexdigest()
    return key

def is_token_expired(key):
    access_code = db.get_user_token_by_key(key)
    if access_code == "Failed" :
        print "Error occured to get access_code"
    else :
        