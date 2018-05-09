#HackerRank Write a function 
#Author: Erica Zhang
#Date: 5/9/18

def is_leap(year):
    leap = False
    while year >=1900 and year<= 10**5:
        return year%4==0 and year%100!=0 or year%100==0 and year%400==0
    return leap

year = int(raw_input())
print is_leap(year)