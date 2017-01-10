store = {}

def fib(n):
	for k in range(1, n+1):
		if (k <= 2):
			f = 1
		else:
			f = store[k-1] + store[k-2]
		store[k] = f
	print(store[n])
	return store[n]	

i = input("Choose a number: ")
fib(int(i))
print("The fibonacci for: " + i)