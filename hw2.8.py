# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 17:14:50 2016

@author: youjin
"""

def result1(x,n):
    '''
    the function, result1, caculates the function f(x)=3.95*（x-x**2）through n times recursion
    
    parameters:
    x- a number in [0,1] as input
    n- the times of recursion 
    '''
    if n==1:
        return 3.95*(x-x**2) #the end of recursion，also is the first time to cacalute the result
    else:
        return result1(result1(x,1),n-1) # then take the value from last caculation into the next caculation
print('the result(.9,100) of function f(x)=3.95*（x-x**2）is %f' %result1(.9,100))
#the result1 is  0.3078187619897856

def result2(x,n):
    '''
    the function, result1, caculates the function f(x)=3.95*x*(1-x）through n times recursion
    
    parameters:
    x- a number in [0,1] as input
    n- the times of recursion 
    '''
    if n==1:
        return 3.95*x*(1-x) #the end of recursion，also is the first time to cacalute the result
    else:
        return result2(result2(x,1),n-1) # then take the value from last caculation into the next caculation
print('the result(.9,100) of function f(x)=3.95*x*(1-x) is %f' %result2(.9,100)) 
#the result2 is 0.9230225584410336

def result3(x,n):
    '''
    the function, result1, caculates the function f(x)=3.95*x-3.95*(x**2) through n times recursion
    
    parameters:
    x- a number in [0,1] as input
    n- the times of recursion 
    '''
    if n==1:
        return 3.95*x-3.95*(x**2) #the end of recursion，also is the first time to cacalute the result
    else:
        return result3(result3(x,1),n-1) # then take the value from last caculation into the next caculation
print('the result(.9,100) of function f(x)=3.95*x-3.95*(x**2) is %f'%result3(.9,100)) 
# the result3 is 0.28783086903250865
