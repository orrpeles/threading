#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 09:08:27 2019
Ref: https://pythontips.com/2019/05/29/speeding-up-python-code-using-multithreading/
@author: python
"""

import requests
from time import time

url_list = [
    "https://via.placeholder.com/400",
    "https://via.placeholder.com/410",
    "https://via.placeholder.com/420",
    "https://via.placeholder.com/430",
    "https://via.placeholder.com/440",
    "https://via.placeholder.com/450",
    "https://via.placeholder.com/460",
    "https://via.placeholder.com/470",
    "https://via.placeholder.com/480",
    "https://via.placeholder.com/490",
    "https://via.placeholder.com/500",
    "https://via.placeholder.com/510",
    "https://via.placeholder.com/520",
    "https://via.placeholder.com/530",
]

def download_file(url):
    html = requests.get(url)
    return html.status_code # status code informs you of the status of the request (200, 401, etc)

start = time()

for url in url_list:
    print(download_file(url))

print(f'Time taken: {time()-start}')


