# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:44:45 2024

@author: Ngoc Anh
"""

a = int(input("Nhập vào số nguyên n: "))
if a % 2 == 0 and a >0:
    T = (a/ 2) * ((a / 2)+ 1)
    print("Tổng dãy số chẵn là: ", T)
else:
    print("Không thỏa mãn bài toán.")