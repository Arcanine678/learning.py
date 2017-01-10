import time

def fib(n):
	if (n <= 2):
		f = 1
	else:
		f = fib(n-1) + fib(n-2)
	print (f)
	time.sleep(0.5)
	return f

i = input("Choose a number : ")
fib(int(i))
print("The fibonacci for : " + i)

