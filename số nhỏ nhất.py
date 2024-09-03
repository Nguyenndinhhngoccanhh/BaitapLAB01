# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 14:57:19 2024

@author: Ngoc Anh
"""

a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
c = int(input("Nhập số nguyên thứ ba: "))
d = int(input("Nhập số nguyên thứ tư: "))
if b < a:
    a = b
if c < a:
    a = c
if d < a:
    a = d
print("Giá trị nhỏ nhất là:", a)