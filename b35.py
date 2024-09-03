# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:28:47 2024

@author: Ngoc Anh
"""

a = int(input("Nhập vào số nguyên n: "))
if a>0 :
    S = a*(a+1)//2
    print("Tổng dãy số là: ", S)
else:
    print("Không thỏa mãn bài toán.")