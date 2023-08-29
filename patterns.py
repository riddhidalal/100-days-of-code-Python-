#pattern questions
#1] Create a variable rows which takes an integer as input for the number of rows
#print the following pattern
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

rows = int(input())
for i in range(rows+1):
  for j in range(i):
    print(i , end=' ')
  print(" ")
