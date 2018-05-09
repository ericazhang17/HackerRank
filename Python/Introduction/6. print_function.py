#HackerRank Print function
#Author: Erica Zhang
#Date: 5/9/18

#Solution#1 as required by instruction to use print function from py3
from __future__ import print_function

n = int(raw_input())
# values =[]
# for i in range(1,n+1):
#     values.append(i)
values = [i for i in range(1,n+1)]  #list comprehension
print(*values, sep='')    #as required by instruction

#Solution#2 good old py2 using .join() method

n = int(raw_input())

values = [str(i) for i in range(1,n+1)]
print (''.join(values))