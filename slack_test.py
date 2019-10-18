import requests,json

WEB_HOOK_URL = "https://hooks.slack.com/services"
TOKEN = "------slack token------"
CHANNEL = "-----channel name-----"

requests.post(WEB_HOOK_URL, data = json.dumps({
        'text': u'Hello1 From Python.'
                    }))
