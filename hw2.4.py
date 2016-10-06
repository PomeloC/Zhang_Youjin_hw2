# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 16:55:21 2016

@author: youjin
"""
"""
Question 4
"""

def f(n, d):
    x = n * 9
    z = x
    k = 1
    while z % d:
        z = z * 10 + x
        k += 1
    return k, z / d

print(f(555,31))