#Every 5xth day, we will be solving DSA questions . 
#Today is ARRAYYYYS day!
#Short intro about ARRAY
#ARRAY is a good friend of Lists but ARRAY doesn't allow multiple data types in a single array.
#Question 1] Create an ARRAY --> [1,2,1,4,5] and reverse the array without using reverse() function . 

import array
new_arr = array.array('i',[1,2,1,4,5])
rev_arr = new_arr[-1::-1]
print(rev_arr)

''' 
Time Complexity:
It takes O(n) time complexity for initiation of an array . 
It takes O(n) time complexity for reversing the array
It takes constant time complexity for printing . 
t = n + n + 1 = 2n+1
O(n) is the resulting time complexity for the entire algorithm . 

Space Complexity:
It takes O(n) space complexity for creating an array .
O(n) space complexity for storing reversed array in a new variable . 
s = n + n
O(n) is the resulting space complexity of the algorithm . 
'''
