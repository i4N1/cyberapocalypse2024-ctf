import requests

url = "http://94.237.55.185:39864/api/options"
HEADERS = {
    'Content-Type': 'application/json'
}
DATA = {
    'message': 'HTB{',
    'command': 'HEAD NORTH'
}

r = requests.get(url)
#r = requests.post(url, headers=HEADERS, data=DATA, )
print(r.text)