

import json
from pmHelpers import *
from datetime import datetime, date
from time import strftime, sleep
import os
#import nmap


ca25_ip = '198.54.132.140'
localHo = '127.0.0.1'


def networkReport(currentIp):

    hostPorts = os.system('nmap -p 80,443 -Pn ' + str(currentIp))
    hostPing = os.system('ping -c 5 ' + str(currentIp))

    print(hostPorts)
    print(hostPing)


nr0 = networkReport(localHo)

#nr1 = networkReport(ca25_ip)


