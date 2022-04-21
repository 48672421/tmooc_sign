import logging

import requests

def on(url,raw_headers,kv,getOrPost):
    '''

    :param url: url
    :param raw_headers: 浏览器直接复制的headers
    :param kv:
    :param getOrPost: 0为get请求，否则为post请求
    :return: 返回headers
    '''
    # print(raw_headers)
    # 向搜索引擎进行关键词提交
    headers = dict([line.split(": ",1) for line in raw_headers.split("\n")])
    # try:
    #     if getOrPost==0:
    #         r = requests.get(url,data=kv,headers=headers)
    #     else:
    #         r = requests.post(url,data=kv,headers=headers)
    #     print(r.headers)
    #     print(r.text)
    #     return r.headers
    # except:
    #     print("产生异常")
    if getOrPost == 0:
        r = requests.get(url, data=kv, headers=headers)
    else:
        r = requests.post(url, data=kv, headers=headers)
    print("headers:",r.headers)
    print("text:",r.text)
    return r.headers
