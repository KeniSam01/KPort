import argparse,socket,time, subprocess
from datetime import datetime

def clear():
    subprocess.call('clear', shell=True)

def hour():
    now = datetime.now()
    return "[" + str(now.hour) + ":" + str(now.minute) + "]"

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

def banner():
    print '\033[32m'''' 
  __  ___ .______     ______   .______      .___________.
 |  |/  / |   _  \   /  __  \  |   _  \     |           |
 |  '  /  |  |_)  | |  |  |  | |  |_)  |    `---|  |----`
 |    <   |   ___/  |  |  |  | |      /         |  |     
 |  .  \  |  |      |  `--'  | |  |\  \----.    |  |     
 |__|\__\ | _|       \______/  | _| `._____|    |__|     \n''''\033[0;0m'

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

parser = argparse.ArgumentParser()
parser.add_argument("-ip","--ip", dest="ip", help="Enter the Target IP")
parser.add_argument("-port", "--port", dest="port", help="Enter the port you want to scan", nargs=1)
parser.add_argument("-v", "--verbose", dest="verbose", help="Verbose mode (0/1)", type=int, )
args = parser.parse_args()

port_2 = range(50000)

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
        print '\033[32m' , hour() , ' [INFO] Please try again, you have entered an incorrect ip\n''\033[0;0m\n'
