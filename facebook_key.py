import json
import pyquery
import requests


def main():
    # 將 Chrome 裡面看到的 cookie 複製貼上到這邊，以偽裝成臉書網站成功登入後的請求
    cookieParts = 'datr=cnF1WpFjT8H71d26GGHH8mgz; sb=e3F1WgBtxicwFHLhcQ6XGFy2; c_user=761761551; xs=79%3APx8gBx-CuVlfKw%3A2%3A1517646365%3A14635%3A11280; act=1527494050484%2F6; fr=0jfTmtaSju0KEj3RF.AWUYEHw65nGc2z2O8xJJSjVN-ws.Bac6G7.-n.FsL.0.0.BbC7kY.AWXUzQEo; presence=EDvF3EtimeF1527494945EuserFA2761761551A2EstateFDutF1527494945883CEchFDp_5f761761551F2CC; wd=960x1010'.split(
        '; ')
    cookies = {}
    for cookiePart in cookieParts:
        cookiePair = cookiePart.split('=')
        cookieKey = cookiePair[0]
        cookieVal = cookiePair[1]
        cookies[cookieKey] = cookieVal
    response = requests.get('https://www.facebook.com/pages_reaction_units/more/?page_id=46251501064&cursor=%7B%22card_id%22%3A%22page_composer_card%22%2C%22has_next_page%22%3Atrue%7D&surface=www_pages_home&unit_count=8&referrer&dpr=1&__user=761761551&__a=1&__dyn=5V4cjLx2ByK5A9UkKHqAyqomzFEbEyGgS8VpXheCGgqx-5Wzob4q5-ay8KFGUpG4VEG5UC226aDyUJoK48G5WAxamjDK7GgPwzxuFS58-4oHzoK26ih4-e-nyUgxCuiaAz8gCwoFoG9Km8yFUix6cw_xqUtVe49888vGfCCgWrxjyoG69Q4UlDCzopAxOdyFE-5o-6bG-m4ooAnyrzRG6q8IHGfjg8laUy2uibKqify4cBJ2oS1fx3yUymfVeeAK2G9AGeyUhUPy9oHWUGvww-A5ppbgqo8Ulz4UGmUhDzEjVEjyoG2S13z8aUO4oKV8CuqV8&__req=5&__be=1&__pc=PHASED%3ADEFAULT&__rev=3948835&__spin_r=3948835&__spin_b=trunk&__spin_t=1527494954', cookies=cookies)
    if response.status_code == 200:
        jsonBody = json.loads(response.text[9:])
        print(jsonBody['domops'][0][3]['__html'])
    else:
        print('回傳代碼並非 200')


if __name__ == '__main__':
    main()
