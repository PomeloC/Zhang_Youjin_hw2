# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 16:36:14 2016

@author: youjin
"""

'''Question 1'''
def fibonacci (n):
    '''
    The function,fibonacci(n), calculates nth the term of the Fibonacci sequence

    parameters:
    n- a number represents nth term of fibonacci sequence
    
    returns
    the number of nth fibonacci sequence
    '''
    if n==1 or n==2:
        return 1  #set the end of recursion 
    else:
        return fibonacci(n-1)+fibonacci(n-2)#use recursion function to caculate fibonacci(n)


def index_first(n):
    '''
    The function, index_first(n), caculates the index of the first term in the 
    Fibonacci sequence to contain n digits
    
    parameters:
    n- the number of digits
    
    return
    a number that is the index of the first term in the Fibonacci sequence to contain n digits
    '''
    i=1
    j=1 #initialize two numbers of the adjacent Fibonacci sequence 
    k=1 #initialize the index of fibonacci sequence with 1
    while True: # create a loop always runnings until break
        if len(list(map(int, str(i))))==n: #as long as the number of digits is n, break the loop           
            break
        else:
            k=k+1 #every loop the index need to plus 1
            t=i
            i=j
            j=j+t #every loop i and j need to move to the next
    return k
print('the first number with 100 digits appears in %d th postion'%index_first(100))

 
