# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 09:18:16 2024

@author: Ngoc Anh
"""

a =  int(input("Nhập số nguyên a: "))
b =  int(input("Nhập số nguyên b: "))
tong = a + b
hieu = a - b 
tich = a * b
thuong = a / b
du  = a % b
nguyen = a // b
print("Tổng của a và b là: ",tong)
print("Hiệu của a và b là: ", hieu)
print("Tích của a và b là: ",tich)
print("Thương của a và b là: ",round(thuong,3))
print("Dư của a và b là: ",du)
print("Chia lấy nguyên của a và b là: ",nguyen)
