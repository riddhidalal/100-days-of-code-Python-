#Factorial Calculation:
#Write a function to calculate the factorial of a given positive integer.
n = int(input())
fact = 1
for i in range(1,n+1):
  fact *= i

print(fact)
  
