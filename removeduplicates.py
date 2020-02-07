#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 17:42:46 2020

@author: root
"""

num = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 4]
uniques = []
for number in num:
    if number not in uniques:
        uniques.append(number)
print(uniques)