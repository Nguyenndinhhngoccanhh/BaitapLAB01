# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 20:48:22 2024

@author: Ngoc Anh
"""
a=int(input("Nhập a = "))
b=int(input("Nhập b = "))
c=int(input("Nhập c = "))
if a>b:
    a,b=b,a
elif a>c:
    a,c=c,a
elif b>c:
    b,c=c,b
print("Thứ tự tăng dần của các số: ",a,b,c)
