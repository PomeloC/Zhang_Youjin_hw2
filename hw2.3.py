# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 16:51:03 2016

@author: youjin
"""

"""Question 3
The purpose of this program is to create Collatz Chain for a given integer N.
We will also find which number (N), under one thousand, produces the longest chain"""

#First we ask for the user to input a value for N

N=int(input('Guess the longest Collatz Chain by entering a value for N: '))

#Next we define a function called CollatzChain
def CollatzChain(N,count=1):    #We assign the parameter N to the functions
    while N!=1:
        print(N)
        count+=1
        if N %2==0: #This means that N is an even number since there is no remainder
            N=N//2
        else:
            N=N*3+1 #This is the formula when N is an odd number
    print(N,'\n')
    
    return count-1

def ChainLength():    
    print(CollatzChain(N))    
    if N==97:
        print('This is the longest chain under one thousand!')
    else:
        print('This is not the longest chain under one thousand. Try again.')

    
print(ChainLength())

