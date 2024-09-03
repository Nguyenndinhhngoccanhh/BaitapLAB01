# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 09:34:03 2024

@author: Ngoc Anh
"""

n = int(input("Nhập vào số nguyên dương n: "))
if n == 0:
 print("0 không phải là số chính phương")
elif n > 0:
 root = int(n ** 0.5)
 if root ** 2 == n:
     print(f"{n} là số chính phương")
 else:
     print(f"{n} không phải là số chính phương")
else:
 print("Số nguyên âm không xét")