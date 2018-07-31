import json
import requests
ACCESS_TOKEN = None
def grabPageFeed(pageId):
    response = requests.get('https://graph.facebook.com/v2.12/%s/feed?access_token=%s' % (pageId, ACCESS_TOKEN))
    if response.status_code == 200 :
        jsonbody = response.json()
        print(jsonbody)
    else:
        jsonbody = response.json()
        print(jsonbody)
def main():
    global ACCESS_TOKEN
    appId = '2040776456185063'
    appSecret = '840c6694e727a97f219f39aba00e6f12'
    response = requests.get('https://graph.facebook.com/oauth/access_token?client_id=%s&client_secret=%s&grant_type=client_credentials' % (appId,appSecret))
    if response.status_code == 200 :
        jsonbody = response.json()
        print(jsonbody)
        accessToken = jsonbody['access_token']
        print(accessToken)
    else:
        print('fb api 回傳代碼並非200')

if __name__ == '__main__':
    main()