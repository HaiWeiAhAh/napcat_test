


def send_group_message(group_id, message):
    payload = {
   "group_id": group_id,
   "message": [
      {
         "type": "text",
         "data": {
            "text": message
         }
      }
   ]
}
    return payload

def send_private_message(private_id, message):
    payload = {
   "user_id": private_id,
   "message": [
      {
         "type": "text",
         "data": {
            "text": message
         }
      }
   ]
}
    return payload