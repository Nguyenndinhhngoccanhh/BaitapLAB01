# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 14:14:58 2024

@author: Ngoc Anh
"""


a = float(input("Nhập số thực a: "))
b = float(input("Nhập số thực b: "))
tử = a + b 
mẫu = a**(1/3) + b**(1/3)
m = (a*b)**(1/3)
n = a**(1/3)
p = b**(1/3)
bt1 = tử/mẫu - m
bt2 = (n - p)**2
bieu_thuc = bt1/bt2 
if a > 0 and b > 0 and a != b:
    print("Kết quả biểu thức: ", bieu_thuc)
else:
    print("Không thỏa mãn")