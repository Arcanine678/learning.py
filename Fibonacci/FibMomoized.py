memo = {}

def fib(n):
	#if n is in memo: return memo
	if(n in memo):
		return memo[n]
	if (n <= 2):
		f = 1
	else:
		f = fib(n-1) + fib(n-2)
	print(f)
	#add to memo
	memo[n] = f
	return f

i = input("Choose a number : ")
fib(int(i))
print("The fibonacci for : " + i)