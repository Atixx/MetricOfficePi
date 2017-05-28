#! /usr/bin/python

import subprocess
import re
import sys
import time
import requests
import json



def post(mac_address):
  print("This MAC has left: "+mac_address)
  headers = {'content-type': 'application/json'}
  url = 'http://posttestserver.com/post.php'
  payload = { 'MAC Address' : mac_address }
  response = requests.post(url, data = json.dumps(payload), headers = headers)
  # print(response.text)

def verifyConnection(mac_address):

  # print mac_address
  # flag = True
   subnet = '192.168.'

   while True:

    output = subprocess.check_output(['tshark', '-I', '-i', 'wlan1', '-f',  'ether src host '+ mac_address +' and tcp', '-c', '1', '-a', 'duration:30'])
    p = re.compile(subnet+'[0-9]{0,3}\.[0-9]{0,3}')
    subnet+r"[0-9]{0,3}\.[0-9]{0,3}"
    ip = p.search(output)
    if ip:
      print(ip.group())
      time.sleep(30)
    else:
      post(mac_address)
      break

if __name__ == '__main__':
  verifyConnection(sys.argv[1])

 # tiempo o registro a tshark (si encontro, entra de nuevo pero despeus de un timeout de 60 sec)

