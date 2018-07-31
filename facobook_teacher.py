import json
import requests

ACCESS_TOKEN = None

def grabPageFeed(pageId):
    response = requests.get('https://graph.facebook.com/v2.12/%s/feed?access_token=%s' % (pageId, ACCESS_TOKEN))
    if response.status_code == 200:
        # 讀取回傳資料
        jsonBody = response.json()
        print(jsonBody)
    else:
        # 新的應用程式都需要經過 Facebook 審核機制才能抓取專頁文章
        jsonBody = response.json()
        print(jsonBody)

def main():
    # 應用程式編號
    appId = '928812370635159'
    # 應用程式密鑰
    appSecret = '7415cfa8c8d8bfdd1e7275493aab3276'
    # 驗證應用程式以取得存取權杖（Access Token）
    response = requests.get('https://graph.facebook.com/oauth/access_token?client_id=%s&client_secret=%s&grant_type=client_credentials' % (appId, appSecret))
    if response.status_code == 200:
        # 讀取回傳資料
        jsonBody = response.json()
        # {'access_token': '928812370635159|s2AJop3rHfekwgTempSdBlFfvg0', 'token_type': 'bearer'}
        print(jsonBody)
        # 讀取存取權杖
        accessToken = jsonBody['access_token']
        print(accessToken)
    else:
        print('FB API 回傳代碼並非 200')

if __name__ == '__main__':
    main()
