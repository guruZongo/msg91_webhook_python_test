import http.client
import json

# ----------------  GLOBALS: configuration - change these for your environment -------------------------
MSG_URL = "api.msg91.com"
SEND_TEMPLATE_TEXT_URL = "/api/v5/whatsapp/whatsapp-outbound-message/"
SEND_SIMPLE_TEXT_URL = "/api/v5/whatsapp/whatsapp-outbound-message/"
AUTHKEY = "383383AQzgXrY4LQnz633eb26eP1"
INTEGRATED_NUM = "919611731040"
WEBHOOK_ADMIN_NUM="919886378222"
# ----------------------------------------------------------------------------------------------------------

# initiator
def send_template_message(num,name,msg):
    """
     BUSINESS-INITIATED
     Bot can initiate conversation when using templates
    """
    conn = http.client.HTTPSConnection(MSG_URL)

    toNumber = "919886378222"
    toName = "Leslie"
    # num = toNumber
    # name = toName
    print(num)
    print(name)

    payload_obj = {
        "integrated_number": INTEGRATED_NUM,
        "content_type": "template",
        "payload": {
            "to": toNumber,
            "type": "template",
            "template": {
                "name": "zv_welcome",
                "language": {
                    "code": "en",
                    "policy": "deterministic"
                },
                "components": [
                    {
                        "type": "body",
                        "parameters": [
                            {
                                "type": "text",
                                "text": toName
                            }
                        ]
                    }
                ]
            },
            "messaging_product": "whatsapp"
        }
    }

    payload = json.dumps(payload_obj)

    headers = {
        'content-type': "application/json",
        'authkey': AUTHKEY
    }

    conn.request("POST", SEND_TEMPLATE_TEXT_URL, payload, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))
    return 'success', 200
    # return data.decode("utf-8")

# continuer
def send_simple_message(num, name, msg):
    """
     USER-INITIATED
     Can only be used after user initiates a conversation.
    """
    conn = http.client.HTTPSConnection(MSG_URL)
    print(name)
    # if (name === '')
    #     name = "friend"
    payload_obj = {
      "integrated_number": INTEGRATED_NUM,
      "recipient_number": num,
      "content_type": "text",
      "text": f'Hi {name}, {msg}'
    }
    payload = json.dumps(payload_obj)

    headers = {
        'content-type': "application/json",
        'authkey': AUTHKEY
    }

    conn.request("POST", SEND_SIMPLE_TEXT_URL, payload, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))
    return'success', 200

# receiver
def notify_WH_message(from_num, msg_recieved):

    conn = http.client.HTTPSConnection(MSG_URL)
    botAdmin = "919886378222"

    payload_obj = {
      "integrated_number": INTEGRATED_NUM,
      "recipient_number": botAdmin,
      "content_type": "text",
      "text": f'Hi ZVbot just recieved this message : {msg_recieved} . From {from_num}'
    }
    payload = json.dumps(payload_obj)

    headers = {
        'content-type': "application/json",
        'authkey': AUTHKEY
    }

    conn.request("POST", SEND_SIMPLE_TEXT_URL, payload, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))
    return 'Webhook received!', 200


def notify_WH_message_Template(from_num, msg):
    """
       BUSINESS-INITIATED
       Bot can initiate conversation when using templates
      """
    conn = http.client.HTTPSConnection(MSG_URL)

    toNumber = "918123836393"
    # toNumber = WEBHOOK_ADMIN_NUM
    # toName = "Leslie"

    payload_obj = {
        "integrated_number": INTEGRATED_NUM,
        "content_type": "template",
        "payload": {
        "to": toNumber,
        "type": "template",
        "template": {
            "name": "zv_notifier",
            "language": {
                "code": "en",
                "policy": "deterministic"
            },
            "components": [
                {
                    "type": "body",
                    "parameters": [
                        {
                            "type": "text",
                            "text": msg
                        },
                        {
                            "type": "text",
                            "text": from_num
                        }
                    ]
                }
            ]
        },
        "messaging_product": "whatsapp"
    }
    }

    payload = json.dumps(payload_obj)

    headers = {
        'content-type': "application/json",
        'authkey': AUTHKEY
    }

    conn.request("POST", SEND_TEMPLATE_TEXT_URL, payload, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))
    return 'success', 200


def send_admin_reply(to_num, to_msg):
    # if (name === '')
   name = "friend"
   send_simple_message(to_num, name, to_msg)
   return 'success', 200


def checkWaAvailabilty():
    return 'success', 200