import requests
import http.cookiejar

agent = 'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
headers = {
    "Host": "esagittarius.com ",
    "Connection": "keep-alive",
    "Origin":"http://esagittarius.com",
    "Referer":"http://esagittarius.com/ltcreward/",
    'User-Agent':agent
}


def login(lite_pag):
    postdata = {
        'btc-address': lite_pag,  # 填写莱特币钱包账号
        'refby': '',
        'botprotection': 'im not',  # 我不是机器人哈哈哈
        'submit': 'Login',
        'submit_address': '1',
    }
    session = requests.Session()
    session.cookies = http.cookiejar.LWPCookieJar(lite_pag)
    try:
        result = session.post('http://esagittarius.com/ltcreward/', data=postdata, headers=headers)
    except:
        raise Exception('error')
    else:
        session.cookies.save(ignore_discard=True, ignore_expires=True)