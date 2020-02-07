#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 05:26:40 2020

@author: root
"""
#the largest number in a list
numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]#setting the max number to 0
for number in numbers:
    if number > max:#checks to see if number is greater than max
        max = number#resetting max to the new number
        print(max)