import turtle as tk
import threading
import math
import time
import random as rd

tk.speed(0)

r2=math.sqrt(2)

def ret(l):
	l=rd.random()*l
	tk.pencolor((0,1,0))
	tk.pensize(l/2)
	tk.fd(l)
	tk.lt(180)
	tk.up()
	tk.fd(l)
	tk.lt(180)
	tk.down()
	return

def rec(l,min):
	if l<=min:
		ret(l)
		tk.rt(2*a)
		ret(l)
		tk.lt(a)
	else:
		tk.pencolor(color)
		tk.pensize(l/r)
		tk.fd(l)
		tk.lt(a)
		rec(l/r2,min)
		tk.pencolor(color)
		tk.pensize(l/r)
		tk.lt(180)
		tk.up()
		tk.fd(l)
		tk.lt(180-2*a)
		tk.down()
		tk.fd(l)
		tk.lt(a)
		rec(l/r2,min)
		tk.pencolor(color)
		tk.pensize(l/r)
		tk.lt(180)
		tk.up()
		tk.fd(l)
		tk.rt(180-a)
		tk.down()

l=100
min=5
a=45
r=5
color=(88/255,41/255,0)
tk.pencolor(color)
tk.pensize(l/r)
tk.tracer(False)
tk.up()

tk.down()

rec(l,min)
tk.lt(a)
tk.lt(180)
rec(l,min)
