import requests as r
import json

name = input("Enter your name: ")
print("start chatting with bot now!\n")

while(1):
   msg = input(name+": ")
   res = r.get('https://api.simsimi.net/v1/?text={}&lang=en&cf=true'.format(msg)) 
   res = json.loads(res.text)
   resp = res['messages'][0]['response']
   print('🤖 : '+resp)
