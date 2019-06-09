
import socket
import os
import threading

IP=(socket.gethostbyname(socket.gethostname())).split(".")
mask=""
for i in range(len(IP)-1):
    mask+=IP[i]+"."

def REZAL_ping(IP):
    try:
        if (int(os.system("ping -w 5 "+str(IP))==0)):
            IPS.append(IP)
        else:
            return
    except:
        return

global IPS
IPS=[]
for i in range(255):
    IP=mask+str(i)
    threading.Thread(target=REZAL_ping,args=[IP]).start()
print(IPS)