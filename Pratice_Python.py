# -*- coding: utf-8 -*-
"""
Created on Thu May 11 14:14:03 2023

@author: Chig_al
"""
#%% EX1
this_year=2023
name=input ("write your name: ")
age=(int)(input ("wirte your age: "))
birthday100=this_year+99-age

print(f"Dear {name} you are going to turn 100 in {birthday100}")

#%% EX2

num=int(input ("insert a number: "))
if (num%2):
 print("dispari")
else:
 print("pari")
 if not(num%4):
     print("...e divisibile per 4")
#%% EX3
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for v in a:
    if v!=5:
        print (v) 
        
l=[]
"""
for v in a:
    if v != 5:
        l.append(v)
"""
l=[v for v in a if v != 5]
print (l)        

     
     
#%% EX4
num=int(input ("insert a number: "))
l=[n for n in range(2,int(num/2)+1) if (num % n) ==0 ]
if (len(l) !=0): 
    print (l)
else: 
    print ("Prime number")
#%% EX5

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

l=list(set([x for x in a if x in b]))

print (l)

#%% EX6

name=input ("write a string name: ")
nameR=name[::-1]
if (name == nameR):
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")
#%% EX7
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
l=[v for v in a if (v%2 == 0)]
print (l)

#%% EX8
values = ["Rock","Scissors","Paper"]
def check_val (s):
    val = -1
    if s == "R" or  s == "r":
        val  = 0 
    if s == "S" or  s == "s":
        val  = 1
    if s == "P" or  s ==  "p":
        val = 2 
    return  val
    

P1 = P2 = 0
while (True):
    print("\n\n-------------------------------------")
    print("insert R,S,P or something else to end")
    P1 = check_val(input("player 1: "))
    P2 = check_val(input("player 2: "))
    print(f"{values[P1]} ({P1}) <---> {values[P2]}({P2})\n")
    if (P1 == -1 or P2 == -1):
        break
    if (P2-P1 == 1):
        print ("      ** player 1 wins **")
    elif (P1==P2):
        print ("           ** tie **")
    else:
        print ("** player 2 wins **")
    print("-------------------------------------")# with this line it is really fancy now!
    

    

  
