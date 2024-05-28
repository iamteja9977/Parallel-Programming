import time
import threading

def fib(num):
	time.sleep(0.3)
	if num==0:
		return 0
	elif num == 1:
		return 1
	else:
		return fib(num-1) + fib(num-2)
num = int(input("Enter the number: "))

for i in range(num):
        print(fib(i))
#t= time.time()
t = threading.Thread(target=fib, args=(num,))
t.start()
print("series printed ")
