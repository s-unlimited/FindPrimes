#FIND PRIMES: This is a function that returns the number of prime numbers 
# that exist up to and including a given number
# By convention, 0 and 1 are not prime.
# findprime(100) --> 25

def isprime(num1):
	count=2
	if num1 == 2:
		return True
	while count < num1:
		if (count+1) == num1:
			return True
		elif (num1 % count == 0):
			return False
		
		count+=1

def findprime(num1):
	counter=2
	primecounter=0
	while counter < num1:
		if isprime(counter):
			primecounter+=1
			print(f"{counter} is a prime number")
		else:			
			pass
		
		counter+=1
#		print(f"debug count:{counter} num:{num1} mod:{num1%counter}")
	return primecounter

int1=int(input("Please enter the number to check for primes: "))
#int1 = 100000

total = findprime(int1)
print(f"\nTotal number of prime numbers within 0-{int1} is {total}")


print("\nGoodbye World")

