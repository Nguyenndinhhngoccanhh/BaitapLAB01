# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 13:34:23 2024

@author: Ngoc Anh
"""

input_str = input("Nhập một chữ cái: ")
if input_str.islower():
    output_str = input_str.upper()
else:
    output_str = input_str.lower()
print("Chữ cái đầu ra:", output_str)