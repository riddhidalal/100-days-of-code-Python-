#palindrome _check
#Write a program that checks whether a given string is a palindrome or not.

string = str(input("Please enter the word : "))
string_rev = string[-1::-1]   #slicing

if string == string_rev:
  print("Yes! Its a palindrome!")
else:
  print("No, this is not a palindrome!")
  print("Try with a different word")

'''
Time Complexity:
Hi! Let's calculate the time complexity of the code.
Let's go stepwise:
1. Reading input :
Reading input takes O(n) time where n is the length of the string . 
2. String reversal :
When we reverse the string we are traversing from 1st letter of the string to the last letter .
Hence , this also takes O(n) time complexity.
3. String comparison :
In string comparison , we traverse from first string to last . It also takes O(n) complexity .

Hence T = n+n+n = 3n
But since constants can be neglected , Time complexity becomes O(n).

Space complexity - O(1) i.e constant size is used by the program .
'''




