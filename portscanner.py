import socket
from typing import final

print("Made By")
print("""
  ######                             ######                
 #     # #####  #    #  ####  ###### #     # ###### ###### 
 #     # #    # #    # #    # #      #     # #      #      
 ######  #    # #    # #      #####  ######  #####  #####  
 #     # #####  #    # #      #      #       #      #      
 #     # #   #  #    # #    # #      #       #      #      
 ######  #    #  ####   ####  ###### #       ###### ###### """)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("[+]Type In The IP Address : ")
thing = int(input("[+]Which Number Do You Want To Start Port Scanning From : "))
sthing = int(input("[+]Which Number Do You Want To End Port Scanning To : "))

def portscanner(port):
    try:
        sock.connect((host, port))
        print("[+]Port " + str(port) + " Is Open For " + host)
    except:
        print("[-]Port " + str(port) + " Is Closed For " + host)
        

for port in range(thing, sthing):
    portscanner(port)
