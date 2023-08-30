#Beginner Track 
# Q1] Write a program that takes an integer input from the user and determines whether it's odd or even.

a = int(input())
if a % 2 == 0:
  print("even")
else:
  print("odd")

'''
Time Complexity : O(1)
Time Complexity is calculated based upon the number of steps , operations and iterations in the program . 
Number of operations = 1
Number of iterations = 0
Total Number of steps = 2 (operations + conditional check)
Therefore O(2) --> O(1) which indicates that the program takes constant time for any input and is not dependent on the size of the input.

Space Complexity = O(1) which indicated that the program takes constant space and does not change with the input . 

