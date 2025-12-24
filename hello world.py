# -*- coding: utf-8 -*-
import http.client
import json
import payload_templates

def post_request(url_api,raw_payload,method:str = "POST"):
    try:
        init_payload = json.dumps(raw_payload)
        headers = {
            'Content-Type': 'application/json'
        }
        conn.request(method, url_api, init_payload, headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))
    except Exception as e:
        print(e)

if __name__ == '__main__':
    conn = http.client.HTTPConnection("172.17.0.1", 9099)
    while True:
        raw_input = input("选择功能【1.发送群聊消息】【2.发送私聊消息】:")
        if raw_input == "1":
            group_id = input("发送到群：")
            msg = input(":")
            payload = payload_templates.send_group_message(group_id, msg)
            url_api = "/send_group_msg"
            #
            post_request(url_api,payload)
        elif raw_input == "2":
            private_id = input("发送到人：")
            msg = input(":")
            payload = payload_templates.send_private_message(private_id, msg)
            url_api = "/send_private_msg"
            #
            post_request(url_api, payload)
        else:
            continue