#coding: utf-8
import openpyxl
import os

dir = "."
files = [f for f in os.listdir(dir) if ".xlsx" in os.path.join(dir, f)]
print(files)
