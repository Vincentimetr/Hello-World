import subprocess
import os
import threading
import socket

IP=(socket.gethostbyname(socket.gethostname())).split(".")
mask=""
for i in range(len(IP)-1):
    mask+=IP[i]+"."

def REZAL_ping(IP):
    if (int(os.system("ping -n 2 -w 1 "+str(IP))==0)):
        return True
    else:
        return False

for i in range(256):
    IP=mask+str(i)
    threading.Thread(target=REZAL_ping,args=[IP]).start()
print("ok")
result=[]

arp=str((subprocess.check_output("arp -a"))).replace("\\r","").replace("     ","|").split("\\n")
for i in range(3,len(arp)-1):
    machine=((str(arp[i]).replace(" ","").replace("||","|").replace("-",":").split("|")))
    result.append(machine+[REZAL_ping(machine[0])])
    print("\n")
    print("Apareils du DHCP")
    for i in range(len(result)):
        print(result[i])