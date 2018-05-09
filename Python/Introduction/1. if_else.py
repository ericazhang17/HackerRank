#HackerRank if-else problem
#Author: Erica Zhang 
#Date: 5/9/18

n = int(raw_input())
while n>=1 and n<=100:
    if n%2 !=0 or n%2==0 and n in range(6,21):
        print "Weird"
    elif n%2 ==0 and n in range(2,6) or n%2 ==0 and n>20:
        print "Not Weird"
    break
    
