import requests
import json

webhook_url = "http://127.0.0.1:5000/webhook"

# data = {'name': 'Zongovita Webhook',
#         'URL': 'TestUrl'}
data = {'name': 'Les Webhook',
        'URL': "api.msg91.com/api/v5/whatsapp/whatsapp-outbound-message/",
        'Message': 'Testing Webhook local',
        'Number': '9886378222',
        }


r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})