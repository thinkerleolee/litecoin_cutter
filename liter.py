import requests
import http.cookiejar as cookielib
import time
from bs4 import BeautifulSoup



agent = 'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
headers = {
    "Host": "esagittarius.com ",
    "Connection": "keep-alive",
    "Origin":"http://esagittarius.com",
    "Referer":"http://esagittarius.com/ltcreward/",
    'User-Agent':agent
}

def get_liter(liter_pag,col):
    session = requests.session()
    session.cookies = cookielib.LWPCookieJar(filename=liter_pag)
    try:
        session.cookies.load(ignore_discard=True)
    except:
        print("Cookie 未能加载")
    postdata = {
        'page': 'button_' + str(col),
    }
    try:
        result = session.post('http://esagittarius.com/ltcreward/exttt.php', data=postdata, headers=headers)
    except:
        raise Exception('error')
    timest = time.time()
    strsp = str(int(timest))
    try:
        result = session.get('http://esagittarius.com/ltcreward/', headers=headers)
        num = result.text.index('#FFCC00')
    except:
        raise Exception('error')
    else:
        print(liter_pag + " now litecoin:" + result.text[num + 9: num + 20])


