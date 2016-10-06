# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 16:56:40 2016

@author: youjin
"""

'''Question 6'''								
from math import sqrt

def Isprime(n,k):
     '''
     the function, Isprime(n,k), checks whether n is prime given the scope of divisor [1,k]
     
     parameters:
     n- a number waiting to be checked whether is prime or not
     k- a number giving the divisor's scope
     
     returns:
     1- if n is prime
     0- if n is not prime
     '''
     if k == 1:# the end condition of recursion
    		return 1
     if n%k ==0:# if n could be divided by k, n is not prime
    		return 0
     else:
    		return Isprime(n,k-1)# the recursion body

def main():
     '''
     the main function is to input a number and then check it if it's prime
     '''
     number = eval(input('Please input a POSITIVE INTEGER:'))#input a number		
     K = int(sqrt(number)) #prime test divisor can only up to square root of n
     if Isprime(number,K) == 1:
         print ('%d is a prime number!' %number)  
     else:
         print('%d is NOT a prime number!' %number)	   		
main()
