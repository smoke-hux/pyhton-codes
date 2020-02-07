#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 05:02:23 2020

@author: root
"""

names = ['john', 'Bob', 'Mosh','Sarah', 'Mary']
#we can acces an individual string using  an index
print(names[0])#the first item in the list
print(names[2])#the third item in the list
#you can also use colon to select a range of items
print(names[2:])# this will print out all the names from the thid element to the last element
print(names[2:4])#you can also specify an end index
names[0] = 'jon'#you can modify the list by accessing it using the index and then changing it 
print(names)