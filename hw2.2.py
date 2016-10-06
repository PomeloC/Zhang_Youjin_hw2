# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 16:40:17 2016

@author: youjin
"""

'''
question 2   
   the function is that By starting at the top of the triangle below and moving 
to adjacent numbers on the row below, and we need to find the maximum total from 
top to bottom of the triangle in file"triangle.txt"
    '''


pyramid=[[75],
         [95, 64],
         [17, 47, 82],
         [18, 35, 87, 10],
         [20,  4, 82, 47, 65],
         [19,  1, 23, 75,  3, 34],
         [88,  2, 77, 73,  7, 63, 67],
         [99, 65,  4, 28,  6, 16, 70, 92],
         [41, 41, 26, 56, 83, 40, 80, 70, 33],
         [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
         [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
         [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
         [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
         [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
         [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]]


for i in range(1,len(pyramid))   :
    pyramid[i][i] +=pyramid[i-1][i-1]  

for a in range(1,len(pyramid)):
    for b in range(0, a): 
        if b<1:
                pyramid [a][b] += pyramid[a-1][b]
                
        elif a>b:
                pyramid[a][b]+=max(pyramid [a-1][b-1], pyramid [a-1][b])
        
   
                
print (max(pyramid[14][0:14]))
    
