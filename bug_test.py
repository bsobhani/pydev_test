import time

count = 5
def trigger(p):
	time.sleep(5)
	global count
	print("here "+p+"A")
	pydev.iointr(p+"A", count)
	pydev.iointr(p+"B", count)
	pydev.iointr(p+"C", count)
	pydev.iointr(p+"D", count)
	print("interrupt: "+p+"A")
	#count += 1
