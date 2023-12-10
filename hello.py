#coding: utf-8
import openpyxl

def main():
    # Excel作成
    wb = openpyxl.Workbook()
    wb.save("example.xlsx")

if __name__ == "__main__":
    main()
