# -*- coding: UTF-8 -*-

import argparse,socket,time, subprocess
from datetime import datetime

def starting():
    if (args.port):
        port()

    else:
        try:
            clear()
            if args.verbose == True:
                verbose()

            else:
                escopo()
                connection()

        except TypeError:
            print '\033[32m', hour(), ' [INFO] Please try again, you have entered an incorrect ip\n''\033[0;0m\n'

def banner():
    print '\033[32m'''' 
`7MMF' `YMM' `7MM"""Mq.                      mm    
  MM   .M'     MM   `MM.                     MM    
  MM .d"       MM   ,M9  ,pW"Wq.  `7Mb,od8 mmMMmm  
  MMMMM.       MMmmdM9  6W'   `Wb   MM' "'   MM    
  MM  VMA      MM       8M     M8   MM       MM    
  MM   `MM.    MM       YA.   ,A9   MM       MM    
.JMML.   MMb..JMML.      `Ybmd9'  .JMML.     `Mbmo     \n''''\033[0;0m'

def escopo():

    time.sleep(1)
    banner()
    time.sleep(1)
    print '\033[32m', hour() , " [INFO] The tool is starting"'\033[0;0m'
    time.sleep(1)
    print '\033[32m', hour() , " [INFO] Scanning the IP"'\033[0;0m'
    time.sleep(1)
    print '\033[32m', hour() , " [INFO] Getting information from: " + args.ip + '\033[0;0m'
    time.sleep(1)
    print '\033[32m', hour() , " [INFO] Show port's and status:\n"'\033[0;0m'
    time.sleep(1)

def connection():
    try:
        for port in port_2:
            cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cliente.settimeout(0.15)
            code = cliente.connect_ex((args.ip, int(port)))

            if code == 0:
                print '\033[32m'" Port ", int(port), " Open"'\033[0;0m'
                time.sleep(0.75)
        print "\n"
        exit()


    except KeyboardInterrupt:
        print "\n'\033[32m'" , hour() , " [INFO] The tool was interrupted by the user\n"'\033[0;0m'
        exit()

def verbose():
    try:
        escopo()

        for port in port_2:
            cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cliente.settimeout(0.15)
            code = cliente.connect_ex((args.ip, int(port)))

            if code == 0:
                time.sleep(0.75)
                print '\033[32m'"  Port ", int(port), " Open"'\033[0;0m'
            else:
                time.sleep(0.75)
                print " Port ", int(port), " Closed"
        print "\n"
        exit()

    except KeyboardInterrupt:
        print "\n'\033[32m'" , hour() , " [INFO] The tool was interrupted by the user\n"'\033[0;0m'
        exit()

def port():
    clear()
    value = args.port[0]
    escopo()
    try:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.settimeout(0.15)
        code = cliente.connect_ex((args.ip, int(value)))

        if code == 0:
            time.sleep(0.75)
            print '\033[32m'"  Port ", int(value), " Open"'\033[0;0m'
        else:
            time.sleep(0.75)
            print " Port ", int(value), " Closed"
        print "\n"
        exit()
    except KeyboardInterrupt:
        print "\n'\033[32m'" , hour() , " [INFO] The tool was interrupted by the user\n"'\033[0;0m'
        exit()

def clear():
    subprocess.call('clear', shell=True)

def hour():
    now = datetime.now()
    return "[" + str(now.hour) + ":" + str(now.minute) + "]"

parser = argparse.ArgumentParser()
parser.add_argument("-ip","--ip", dest="ip", help="Enter the Target IP")
parser.add_argument("-port", "--port", dest="port", help="Enter the port you want to scan", nargs=1)
parser.add_argument("-v", "--verbose", dest="verbose", help="Verbose mode (0/1)", type=int, )
args = parser.parse_args()

port_2 = range(50000)

starting()
