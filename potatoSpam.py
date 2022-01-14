#Discord Webhook Spammer by tempie: https://github.com/imTempie
#Don't use for malicious intent, this is meant for EDUCATIONAL PURPOSES ONLY

import pyfiglet
from dhooks import Webhook

potato = pyfiglet.figlet_format("POTATO")
print(potato)

MSG = input("Insert Spam Message:  ")
URL = input("Enter Webhook URL:  ")
hook = Webhook(URL)

def spam():
  hook.send(f"{MSG}")

potatospam = 1
while potatospam==1:
  spam()
