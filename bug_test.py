import time

def prime_list(n):
	if n==1:
		return [2]
	if n==2:
		return [2, 3]
	L = [2, 3]
	p = L[-1] + 2
	while len(L)<n:
		is_prime = True
		for f in L:
			if p%f==0:
				is_prime = False
				break
		if is_prime:
			L.append(p)
		p+=2
	return L
	

count = 5
def trigger(p):
	#time.sleep(5)
	global count
	print("here "+p+"A")
	print(prime_list(1800)[-1])
	pydev.iointr(p+"A", count)
	pydev.iointr(p+"B", count)
	pydev.iointr(p+"C", count)
	pydev.iointr(p+"D", count)
	print("interrupt: "+p+"A")
	#count += 1

if __name__=="__main__":
	print(prime_list(18000)[-1])
