#Discord Webhook Spammer by tempie: https://github.com/imTempie
#Don't use for malicious intent, this is meant for EDUCATIONAL PURPOSES ONLY

import pyfiglet
from dhooks import Webhook

potato = pyfiglet.figlet_format("POTATO")
print(potato)

print("~   Welcome To Potato Spammer   ~")
MSG = input("Insert Spam Message:  ")
URL = input("Enter Webhook URL:  ")
hook = Webhook(URL)
num = 0  

potatospam = 1
while potatospam==1:
  hook.send(f"{MSG}")
  num = num + 1
  print(num, " Spamming: " + URL + " With: " + MSG)
