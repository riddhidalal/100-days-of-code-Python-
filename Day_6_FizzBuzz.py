#Write a program that prints the numbers from 1 to 100 BUT 
#1. For multiples of three, print "Fizz" instead of the number, and for the multiples of five, print "Buzz".
#2. For numbers which are multiples of both three and five, print "FizzBuzz".

for i in range(1,101):
  if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz") 
  else:
    print(i)

'''
Time Complexity:
Here the iteration of the numbers goes around 100 which is fixed number . 
Hence the time complexity here is O(n) i.e the time complexity is linear!
Space Complexity:
Here , the memory allocated takes constant memory space and is NOT dependent on the input .
Hence, it is O(1).
'''
  
