# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 09:15:16 2024

@author: Ngoc Anh
"""

a= float(input("Nhập quãng đường(km ) : "))
if a<=1 :
   print ("tien taxi đi được là : 15000đ")
elif 2<=a<=5:
    print ("tiền taxi đi được là : ", 15000+(a-1)*13500 ,"đ")
elif a>6 and a<=120 :
    print ("tiền taxi đi đc là : ", 15000+4*13500+(a-6)*11000, "đ")
else : 
    print("tiền taxi đi được là : ", (15000+4*13500+(a-6)*11000)-((15000+4*13500+(a-6)*11000)*(10/100)), "đ")