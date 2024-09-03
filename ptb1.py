# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 14:04:06 2024

@author: Ngoc Anh
"""

print("Giả và biện luận phương trình")
a=float(input("Hệ số a= "))
b=float(input("Hệ số b= "))
if a!=0:
    x= -b/a
    print("x=%.3f"%x)
elif b!=0:
    print("Phương trình vô nghiệm ")
else:
    print("Phương trình vô số nghiệm ")