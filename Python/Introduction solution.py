#HackerRank if-else problem

n = int(raw_input())
while n>=1 and n<=100:
    if n%2 !=0 or n%2==0 and n in range(6,21):
        print "Weird"
    elif n%2 ==0 and n in range(2,6) or n%2 ==0 and n>20:
        print "Not Weird"
    break
    
#HackerRank arithmetic operators

a = int(raw_input())
b = int(raw_input())
while a >=1 and a<= 10**10 and b>=1 and b<= 10**10:
    print a+b
    print a-b
    print a*b
    break
    
#HackerRank division 
a = int(raw_input())
b = int(raw_input())
print a/b
print a/float(b)


