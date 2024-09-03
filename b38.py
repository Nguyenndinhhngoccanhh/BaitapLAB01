# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:51:59 2024

@author: Ngoc Anh
"""

n = int(input("Nhập n: "))
S = 1

for i in range(1, n+1):
    S *= i

print("Giá trị của S là:", S)