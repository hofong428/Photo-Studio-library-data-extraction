# coding: utf-8
# @Time: 4/22/2023 11:21 AM
# @Uer: user
# @Author: Codebat_Raymond
# @File: by-lx-page.py

import requests
import time
import execjs

params = {
    'keyword': '火车呼啸而过',
    'page': '1',
    'limit': '12',
    '_platform': 'web',
    '_versioin': '0.2.5',
    '_ts': round(time.time()*1000),
}

ctx = execjs.compile(open('01.js', 'r', encoding='utf-8').read()).call('d123', params)
print(ctx)

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Origin': 'https://fse.agilestudio.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://fse.agilestudio.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'X-Signature': ctx['Signature'],
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}



response = requests.get('https://fse-api.agilestudio.cn/api/search', params=ctx['param'], headers=headers).text
print(response)

