# -*- coding: UTF-8 -*-

import argparse
import socket
import time
import subprocess
from datetime import datetime


def starting():
    if args.port:
        port()

    else:
        try:
            clear()
            if args.verbose:
                verbose()

            else:
                escopo()
                connection()

        except TypeError:
            print hour(), " [INFO] Please try again, you have entered an incorrect ip\n"


def banner():
    print ''' 
`7MMF' `YMM' `7MM"""Mq.                      mm    
  MM   .M'     MM   `MM.                     MM    
  MM .d"       MM   ,M9  ,pW"Wq.  `7Mb,od8 mmMMmm  
  MMMMM.       MMmmdM9  6W'   `Wb   MM' "'   MM    
  MM  VMA      MM       8M     M8   MM       MM    
  MM   `MM.    MM       YA.   ,A9   MM       MM    
.JMML.   MMb..JMML.      `Ybmd9'  .JMML.     `Mbmo     \n'''


def escopo():

    time.sleep(1)
    banner()
    time.sleep(1)
    print hour(), " [INFO] The tool is starting"
    time.sleep(1)
    print hour(), " [INFO] Scanning the IP"
    time.sleep(1)
    print hour(), " [INFO] Getting information from: " + args.ip
    time.sleep(1)
    print hour(), " [INFO] Show port's and status:\n"
    time.sleep(1)


def connection():
    try:
        for port in port_2:
            cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cliente.settimeout(0.15)
            code = cliente.connect_ex((args.ip, int(port)))

            if code == 0:
                print " Port ", int(port), " Open"
                time.sleep(0.75)
        print "\n", exit()
    except KeyboardInterrupt:
        print "\n", hour(), " [INFO] The tool was interrupted by the user\n", exit()


def verbose():
    try:
        escopo()

        for port in port_2:
            cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cliente.settimeout(0.15)
            code = cliente.connect_ex((args.ip, int(port)))

            if code == 0:
                time.sleep(0.75)
                print "  Port ", int(port), " Open"
            else:
                time.sleep(0.75)
                print " Port ", int(port), " Closed"
        print "\n", exit()

    except KeyboardInterrupt:
        print "\n", hour(), " [INFO] The tool was interrupted by the user \n"
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
            print "  Port ", int(value), " Open"
        else:
            time.sleep(0.75)
            print " Port ", int(value), " Closed"
        print "\n", exit()
    except KeyboardInterrupt:
        print hour(), " [INFO] The tool was interrupted by the user\n", exit()


def clear():
    subprocess.call('clear', shell=True)


def hour():
    now = datetime.now()
    return "[" + str(now.hour) + ":" + str(now.minute) + "]"


parser = argparse.ArgumentParser()
parser.add_argument("-ip", "--ip", dest="ip", help="Enter the Target IP")
parser.add_argument("-port", "--port", dest="port", help="Enter the port you want to scan", nargs=1)
parser.add_argument("-v", "--verbose", dest="verbose", help="Verbose mode (0/1)", type=int)
args = parser.parse_args()

port_2 = range(50000)

starting()
