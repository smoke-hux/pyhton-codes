#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 21:56:54 2020

@author: root
"""

#tuples

numbers = (1, 2, 3)
print(numbers[0])


#unpacking
coordinates = (1, 2, 3)
x, y, z = coordinates
print(y)

#dictionaries
#name:huxley scott
#email:huxleyomondu@live.com
#phone:0792252829
"""

customer = {
        "name": "huxley scott",
        "age":30,
        "is_verified": True
        }
print(customer["name"])
customer["name"] = "jack smith"
print(customer.get("sex"))
print(customer["name"])

phone = input("phone: ")
digits_mapping = {
        "1" : "one",
        "2" : "two",
        "3" : "three",
        "4" : "four"
        }
output = ""
for ch in phone:
    output += digits_mapping.get(ch,  "!") + " "
print(output)
"""
# emoji converter
message = input(">")
words = message.split(" ")
emojis = {
        ":)" ; ""
        }
print(words)
