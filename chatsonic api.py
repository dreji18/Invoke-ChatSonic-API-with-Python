# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 21:05:13 2022

@author: dreji18
"""

import requests

url = "https://api.writesonic.com/v2/business/content/chatsonic?engine=premium"

question = "is the company 'Rheinmetall AG' has a Board or leadership commitment to the importance of strong business ethics and integrity, give details"

payload = {"input_text": question}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "X-API-KEY": "xxxxxxx-xxxxxxxxx-xxxxxx-xxxxxxx-xxxxxxxxxx"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)