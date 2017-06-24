# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 15:38:24 2017

@author: Sam
"""

a = 1
vertAndHorizPaths = 0
allOtherPaths = 0
totalSum = 0
n = a - 1

for i in range(int((a*a-a)/2)):
    if i == 0:
        totalSum = totalSum + 1
    elif i == 1:
        totalSum = totalSum + i
    elif i == 2:
        totalSum = totalSum + i
    else:
        totalSum = totalSum + n
            
print(totalSum + 1)
