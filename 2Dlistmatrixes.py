#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 05:54:12 2020

@author: root
"""

matrix = [
        
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        
        ]
print(matrix[1])
matrix[0][1] = 20
print(matrix[0][1])
#we can use nested loops to iterate over every item in the list
for row in matrix:#in each row it will contain one list one item
    for item in row:#used to loop over eacch row that is a list items
        print(item)

numbers = [5, 2, 1, 7, 4]
numbers.append(20)#append is used to add item to a list
print(numbers)
numbers.insert(0, 10)#used when one wants to insert a value to the where one desires and the first digit is the index and the second digits is the number you want to add
print(numbers)
numbers.remove(10)# if you want to remove an item in the list
print(numbers)
numbers.pop()#removes the last item on the list
print(numbers)
print(numbers.index(54))#is used tocheck the index of a given value in the list and also the existence of the given value
print(50 in numbers)


