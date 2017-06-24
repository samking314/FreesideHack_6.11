# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 15:38:24 2017

@author: Sam
"""


a = 1           //the number of squares in the big square
totalSum = 0
n = a - 1       //a constant that represents the number of
                //duplicate paths at each iteration given its size

//run through all possible combos of paths
for i in range(int((a*a-a)/2)):
    """here i is just the number of squares under the path
    and above the bottom of the square.
    (for ex: i == 1 is the case where the path goes all the way right
    and at the second to last square goes up and right and then
    all the way up until it reaches the top.)"""
    if i == 0:
        totalSum = totalSum + 1
    elif i == 1:
        totalSum = totalSum + i
    elif i == 2:
        totalSum = totalSum + i
    else:
        totalSum = totalSum + n
            
//print total sum plus trivial path that hugs the diag
print(totalSum + 1)
