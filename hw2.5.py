# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 16:49:01 2016

@author: youjin
"""

'''QUESTION 5
In England the currency is made up of pound, £, and pence, p, and there are 
eight coins in general circulation: 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p)
then,calculates how many different ways £2 can be made using any number of coins
'''
ways = [0]*201  
ways[0] = 1  
for x in [1,2,5,10,20,50,100,200]:  
    for i in range(x, 201):  
        ways[i] += ways[i-x]  
print (ways[200])