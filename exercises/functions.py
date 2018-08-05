
# Write your solution for 1.4 here!

def is_prime(x):
	a=0
	for i in range (x+1):
		i+=1
		if x%i==0:
			a+=1 

	
	if a==2:
		print("x is a prime number")
	else:
		print("x is not a prime number")

is_prime(5)
is_prime(4)
is_prime(5191)
		

