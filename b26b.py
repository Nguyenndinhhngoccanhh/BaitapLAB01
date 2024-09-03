# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 20:51:07 2024

@author: Ngoc Anh
"""

N=int(input("Nhập số nguyên N = "))
digits=[int(d) for d in str(N)]
digits.sort()
ketqua=int(''.join(map(str,digits)))
print("Kết quả là: ",ketqua)