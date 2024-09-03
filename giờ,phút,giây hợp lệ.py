# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 12:44:36 2024

@author: Ngoc Anh
"""

hour = int(input("Nhập giờ: "))
minute = int(input("Nhập phút: "))
second = int(input("Nhập giây: "))
if hour < 0 or hour >23:
    print("Giờ không hợp lệ!")
elif minute < 0 or minute > 59 :
    print("Phút không hợp lệ!")
elif second < 0 or second > 59:
    print("Giây không hợp lệ!")
else:
    print("Giờ,phút và giây đều hợp lệ!")