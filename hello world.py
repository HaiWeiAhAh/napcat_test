# -*- coding: utf-8 -*-
import requests
import http.client
import json

"""url = "http://172.17.0.1:8099/send_private_msg"
payload = {
    "user_id": 3525843539,
    "message": "你好，NapCatQQ！"
}"""
#resp = requests.post(url, json=payload)
#print(resp.json())



conn = http.client.HTTPSConnection("172.17.0.1，",9099)
payload = json.dumps({
   "user_id": 3525843539,
})
headers = {
   'Content-Type': 'application/json'
}
conn.request("POST", "/send_poke", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))