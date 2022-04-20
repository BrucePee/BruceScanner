import socket

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
host = input("[+]Type In The Website Name : ")
while True: 
    try:
        web = socket.gethostbyname(host)
        print("[+] "+host + " IP Address Is " + web)
    except:
        print("[-]An Error Has Occured Or The WebSite Name Isn't Valid")
        break
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    thing = int(input("[+]Which Number Do You Want To Start Port Scanning From : "))
    sthing = int(input("[+]Which Number Do You Want To End Port Scanning To : "))
    def portscanner(port):
        try:
            sock.connect((web, port))
            print("[+]Port " + str(port) + " Is Open For " + web)
        except:
            print("[-]Port " + str(port) + " Is Closed For" + web)
            

    for port in range(thing, sthing):
        portscanner(port)
