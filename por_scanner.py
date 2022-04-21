from socket import *
from turtle import color
import colorama
import optparse
from threading import *
from colorama import Fore ,Back ,Style

colorama.init()
print(f"{Fore.GREEN}" +"  ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄ ▄▄    ▄ ▄▄    ▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄")   
print(f"{Fore.GREEN}" +"█  ▄    █   ▄  █ █  █ █  █       █       █       █       █      █  █  █ █  █  █ █       █   ▄  █")  
print(f"{Fore.GREEN}" +"█ █▄█   █  █ █ █ █  █ █  █       █    ▄▄▄█  ▄▄▄▄▄█       █  ▄   █   █▄█ █   █▄█ █    ▄▄▄█  █ █ █")  
print(f"{Fore.GREEN}" +"█       █   █▄▄█▄█  █▄█  █     ▄▄█   █▄▄▄█ █▄▄▄▄▄█     ▄▄█ █▄█  █       █       █   █▄▄▄█   █▄▄█▄") 
print(f"{Fore.GREEN}" +"█  ▄   ██    ▄▄  █       █    █  █    ▄▄▄█▄▄▄▄▄  █    █  █      █  ▄    █  ▄    █    ▄▄▄█    ▄▄  █")
print(f"{Fore.GREEN}" +"█ █▄█   █   █  █ █       █    █▄▄█   █▄▄▄ ▄▄▄▄▄█ █    █▄▄█  ▄   █ █ █   █ █ █   █   █▄▄▄█   █  █ █")
print(f"{Fore.GREEN}" +"█▄▄▄▄▄▄▄█▄▄▄█  █▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄█ █▄▄█▄█  █▄▄█▄█  █▄▄█▄▄▄▄▄▄▄█▄▄▄█  █▄█")


def scanning(host, port):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((host, port))
        print(f"{Fore.GREEN}" + "[+]Connection For Port " + str(port) + " Is Open")
    except:
        print(f"\33[31m" + "[-]Connection For Port " + str(port) + " Is Closed")
    finally:
        sock.close()
def port_scann(host, ports):
    try:
        ip = gethostbyname(host)
        print("[+]" + host + " IP Is " + ip)
    except:
        print("[-]Unknown Host For ")
    try:
        name = gethostbyaddr(ip)
        print("[+]Scan Result For : " + name)
    except:
        print("[+]Scan Result For : " + ip)
    setdefaulttimeout(1)
    for port in ports:
        t = Thread(target=scanning , args=(host, int(port)))
        t.start()
def main():
    parser = optparse.OptionParser("Usage : " + "-H <Target Host> -p <target ports>")
    parser.add_option('-H', dest='host', type='string', help='[-]Specify Target Host')
    parser.add_option('-p', dest='port', type='string', help='[-]Specify Target Ports , Separated By Comma')
    (options, args) = parser.parse_args()
    host = options.host
    ports = str(options.port).split(',')
    if(ports == None) | (host == None):
        print(parser.usage)
        exit(0)
    port_scann(host, ports)
        
        
main()