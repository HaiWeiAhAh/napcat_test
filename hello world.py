import requests

url = "http://172.17.0.1:8099/send_private_msg"
payload = {
    "user_id": 3525843539,
    "message": "你好，NapCatQQ！"
}
resp = requests.post(url, json=payload)
print(resp.json())