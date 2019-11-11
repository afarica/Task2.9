# In mathematics, the factorial of an integer n, denoted by n! is the following
# product:
# n!=1×2×...×n
# For the given integer n
# calculate the value n!. Don't use math module in this exercise.
a=int(input("Enter your number:"))
i=1 
b=1
while i <= a: 
	b*=i
	i+=1 
print(a,b)
