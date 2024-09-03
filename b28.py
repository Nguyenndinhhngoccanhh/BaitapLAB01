# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 21:03:42 2024

@author: Ngoc Anh
"""
N = int(input("Nhập số nguyên dương N: "))
for i in range(1, N + 1):
    if N % i == 0:
        print(i)
    