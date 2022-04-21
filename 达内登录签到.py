import hashlib

import requests

import simulation

def get_tommc_session():
    result = requests.get("https://uc.tmooc.cn/message/getMsgNum?_=1650528570258")
    cookies = result.headers['Set-Cookie']
    cookie = cookies.split(";")[0]
    print(cookie)
    return cookie

def get_jsessionid(session,loginName):
    url = "https://uc.tmooc.cn/login/loginTimes"
    raw_headers = """Host: uc.tmooc.cn
Connection: keep-alive
Content-Length: 119
sec-ch-ua: "Chromium";v="94", "Microsoft Edge";v="94", ";Not A Brand";v="99"
Accept: */*
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38
sec-ch-ua-platform: "Windows"
Origin: https://www.tmooc.cn
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://www.tmooc.cn/
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: tedu.local.language=zh-CN; __root_domain_v=.tmooc.cn; _qddaz=QD.507033519332256; Hm_lvt_51179c297feac072ee8d3f66a55aa1bd=1633655154,1633741759,1633913221,1634002423; Hm_lpvt_51179c297feac072ee8d3f66a55aa1bd=1634002423; """+session
    kv = "loginName="+loginName+"&accountType=1"
    getOrpost = 1
    result = simulation.on(url=url, kv=kv, raw_headers=raw_headers, getOrPost=getOrpost)
    cookie = result['Set-Cookie'].replace("Path=/, ","").replace("Path=/; HttpOnly","").replace("Domain=.tmooc.cn; ","")
    print(cookie)
    return cookie

def login(cookie,loginName,password):
    url = "https://uc.tmooc.cn/login"
    raw_headers = """Host: uc.tmooc.cn
Accept: */*
X-Requested-With: XMLHttpRequest
Accept-Language: zh-CN,zh-Hans;q=0.9
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Origin: https://www.tmooc.cn
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Mobile/15E148 Safari/604.1
Connection: keep-alive
Referer: https://www.tmooc.cn/
Content-Length: 123
Cookie: Hm_lvt_51179c297feac072ee8d3f66a55aa1bd=1650528572; Hm_lpvt_51179c297feac072ee8d3f66a55aa1bd=1650529022;  """+cookie
    print(raw_headers)
    kv = "loginName="+loginName+"&password="+password+"&imgCode=agfz&accountType=1&whetherIntranet=10121002"
    getOrpost = 1
    result = simulation.on(url=url,kv=kv,raw_headers=raw_headers,getOrPost=getOrpost)
    # cookie = result['Set-Cookie']
    # print("cookie"+cookie)

def tmooc(id):
    url = "https://tts.tmooc.cn/user/myTTS?sessionId="+id+"&date=Thu%20Apr%2021%202022%2018:40:24%20GMT+0800%20(CST)"

    raw_header = """authority: tts.tmooc.cn
method: GET
path: /user/myTTS?sessionId="""+id+"""&date=Thu%20Apr%2021%202022%2018:40:24%20GMT+0800%20(CST)
scheme: https
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3884.400 QQBrowser/10.8.4560.400"""
    header = dict([line.split(": ", 1) for line in raw_header.split("\n")])
    a = requests.Session()
    resp = a.get(url,headers=header,allow_redirects=False)
    print("cookie:",resp.headers)
    return resp.headers['Set-Cookie'].split(";")[0]

def sign(sessionid):
    url1 = "https://tts.tmooc.cn/studentCenter/studentSign?studentClaId=905383"
    headers1 = """Host: tts.tmooc.cn
Connection: keep-alive
sec-ch-ua: "Chromium";v="94", "Microsoft Edge";v="94", ";Not A Brand";v="99"
Accept: */*
X-Requested-With: XMLHttpRequest
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38
sec-ch-ua-platform: "Windows"
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://tts.tmooc.cn/studentCenter/toMyttsPage
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: """+sessionid
    kv1=""
    getOrpost1 = 0
    simulation.on(url=url1,kv=kv1,raw_headers=headers1,getOrPost=getOrpost1)

##登录
# url = "https://uc.tmooc.cn/login"
# raw_headers = """Host: uc.tmooc.cn
# Connection: keep-alive
# Content-Length: 119
# sec-ch-ua: "Chromium";v="94", "Microsoft Edge";v="94", ";Not A Brand";v="99"
# Accept: */*
# Content-Type: application/x-www-form-urlencoded; charset=UTF-8
# X-Requested-With: XMLHttpRequest
# sec-ch-ua-mobile: ?0
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38
# sec-ch-ua-platform: "Windows"
# Origin: https://www.tmooc.cn
# Sec-Fetch-Site: same-site
# Sec-Fetch-Mode: cors
# Sec-Fetch-Dest: empty
# Referer: https://www.tmooc.cn/
# Accept-Encoding: gzip, deflate, br
# Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
# Cookie: tedu.local.language=zh-CN; __root_domain_v=.tmooc.cn; _qddaz=QD.507033519332256; TMOOC-SESSION=1234; Hm_lvt_51179c297feac072ee8d3f66a55aa1bd=1633655154,1633741759,1633913221,1634002423; Hm_lpvt_51179c297feac072ee8d3f66a55aa1bd=1634002423; JSESSIONID=516ED9A99FC009FD569E19291B74B73B"""
# kv = "loginName=3172251722%40qq.com&password=e10adc3949ba59abbe56e057f20f883e&imgCode=1234&accountType=1&whetherIntranet=10121002"
# getOrpost = 1
# # result = simulation.on(url=url,kv=kv,raw_headers=raw_headers,getOrPost=getOrpost)
# # cookie = result['Set-Cookie']
# # print("cookie"+cookie)
#
# url1="https://tts.tmooc.cn/studentCenter/studentSign?studentClaId=905383"
# headers1 = """Host: tts.tmooc.cn
# Connection: keep-alive
# sec-ch-ua: "Chromium";v="94", "Microsoft Edge";v="94", ";Not A Brand";v="99"
# Accept: */*
# X-Requested-With: XMLHttpRequest
# sec-ch-ua-mobile: ?0
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38
# sec-ch-ua-platform: "Windows"
# Sec-Fetch-Site: same-origin
# Sec-Fetch-Mode: cors
# Sec-Fetch-Dest: empty
# Referer: https://tts.tmooc.cn/studentCenter/toMyttsPage
# Accept-Encoding: gzip, deflate, br
# Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
# Cookie: sessionid=23eaa34a070347599a4e76fd67612ec1|1104332666%40qq.com"""
# kv1=""
# getOrpost1 = 0
# # simulation.on(url=url1,kv=kv1,raw_headers=headers1,getOrPost=getOrpost1)

loginName="1104332666@qq.com"
password = hashlib.md5("80190923".encode(encoding="UTF-8")).hexdigest()

session = get_tommc_session()
cookie = get_jsessionid(session,loginName)
login(cookie,loginName,password)
id = cookie.split(";")[0].split("=")[1]
print(id)
sessionid = tmooc(id)
print("sessionid:",sessionid)
sign(sessionid)