import turtle as tk
import threading

tk.speed(0)

def trace(l,min):
	if (l<=min):
		return tk.fd(l)
	else:
		trace(l/3,min)
		tk.rt(60)
		trace(l/3,min)
		tk.lt(120)
		trace(l/3,min)
		tk.rt(60)
		trace(l/3,min)
	return

def triangle(l,min):
	trace(l,min)
	tk.lt(120)
	trace(l,min)
	tk.lt(120)
	trace(l,min)
	tk.lt(120)
	
l=400
min=l
while True:
	triangle(l,min)
	min=min/3