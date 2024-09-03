# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 09:42:38 2024

@author: Ngoc Anh
"""

a = int(input("Nhập năm sinh: "))
if 1900 <= a < 2024:
    tuoi = 2024 - a
    print("Tuổi của bạn là: ", tuoi)
elif a == 2024:
    print("Bạn chưa tròn 1 tuổi")
else:
    print("Năm sinh không hợp ")
    
 
