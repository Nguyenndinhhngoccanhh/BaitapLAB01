# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:32:51 2024

@author: Ngoc Anh
"""

a = int(input("Nhập vào số nguyên n: "))
if a >0 :
    T= a * (a + 1) * (2 * a + 1) // 6
    print("Tổng bình phương dãy số là: ", T)
else:
    print("Không thỏa mãn bài toán.")