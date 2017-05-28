import pyinotify
import pdb
import subprocess
import re
import sys
import time
import requests
import json
import time
import threading


# tshark -I -i wlan1 -f "type mgt subtype assoc-resp or type mgt subtype deauth" -e wlan.da -e wlan.sa -T fields -l | ./test.sh

base_url = 'http://10ebde14.ngrok.io/hall_connections/'
disconnect_endpoint = base_url+'disconnect'
connect_endpoint = base_url+'connect'

def post(url, mac_address):
  # print("This MAC has left: "+mac_address)
  headers = {'content-type': 'application/json'}
  payload = { 'mac_address' : mac_address }
  response = requests.post(url, data = json.dumps(payload), headers = headers)
  return(response.text)
  #f = open('/home/pi/Desktop/outfile', 'a')
  #f.write("URL: "+url+", mac address: "+mac_address+'\n')
  #f.close

def verifyConnection(mac_address):
   subnet = '192.168.'
   while True:
	output = subprocess.check_output(['tshark', '-I', '-i', 'wlan1', '-f',  'ether src host '+ mac_address +' and tcp', '-c', '1', '-a', 'duration:30'])
	p = re.compile(subnet+'[0-9]{0,3}\.[0-9]{0,3}')
	subnet+r"[0-9]{0,3}\.[0-9]{0,3}"
	ip = p.search(output)
	if ip:
	  time.sleep(30)
	else:
          post(disconnect_endpoint, mac_address)
	  break

def main(mac_connected, router_mac):
    if router_mac == 'f4:f2:6d:af:41:76':
        # print('MAC CONNECTED: ' + mac_connected)
        post(connect_endpoint, mac_connected)
        th = threading.Thread(target=verifyConnection,args= mac_connected)
        th.daemon = True
        th.start()

    if mac_connected == 'f4:f2:6d:af:41:76':
       # print('MAC DISCONNECTED: ' + router_mac)
        post(disconnect_endpoint, router_mac)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
