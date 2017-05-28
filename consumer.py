import pyinotify
import pdb
import subprocess
import re
import sys
import time
import requests
import json
from multiprocessing import Process

class MyEventHandler(pyinotify.ProcessEvent):
    def my_init(self, file_object=sys.stdout):
        self._file_object = file_object

    def process_IN_MODIFY(self, event):
        file = open('/home/ahalatian/Desktop/lala.txt')
        # line = tail(file, 1)
        pdb.set_trace()
        print(line.decode('utf-8'))

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
      print("--------> MAC ADDRESS SE FUE: " + mac_address)
      break

# TENER EN CUENTA PARA LA DEMO QUE SI INTENTO CONECTAR DOS VECES EL MISMO DISPOSITIVO, NO VA A FUNCIONAR PORQUE ESTA EL LAST_MAC_CONNECTED
def main(mac_connected, router_mac):
    # wm = pyinotify.WatchManager()
    # notifier = pyinotify.Notifier(wm, MyEventHandler())
    # wm.add_watch('/home/ahalatian/Desktop/lala.txt', pyinotify.IN_MODIFY)
    # notifier.loop()

    # command = ['tshark', '-r', '/home/ahalatian/Desktop/lala.txt', '-T', 'fields', '-e', 'wlan.da', '-e', 'wlan.sa']
    # last_mac_connected = ''
    # while True:
    #     run_tshark = subprocess.Popen(
    #         command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #     output, nothing = run_tshark.communicate()
    #     line = output.decode('utf-8').split('\n')[0]
    #     if line == '':
    #         continue
    #     mac_connected = line.split('\t')[0]
    #     router_mac = line.split('\t')[1]
    if router_mac == 'f4:f2:6d:af:41:76':
        print('--------------> MAC CONNECTED: ' + mac_connected)
        print('--------------> FROM ROUTER: ' + router_mac)
        p = Process(target=verifyConnection, args=(mac_connected,))
        p.start()

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
