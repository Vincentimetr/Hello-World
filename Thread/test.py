import threading
import time

count=0

def loop1():
	global count
	while True:
		time.sleep(1)
		count+=1
		print("loop1: "+str(count))
	return
def loop2():
	
	while True:
		time.sleep(1)
		count+=1
		print("loop2: "+str(count))
	return


threading.Thread(target=loop1).start()
time.sleep(1)
threading.Thread(target=loop2).start()