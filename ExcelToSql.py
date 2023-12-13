"""
テーブル定義からSQLファイルを出力
"""

import openpyxl
import os

def getSheetList(fileName):
	txtFile = open(file=fileName, mode="r")
	return txtFile.read().splitlines()

outTxt = open(file="create_sql.sql", mode="w")
tabString = "	"
newlineCode = "\n"

xlsxFiles = [file for file in os.listdir(".") if ".xlsx" in os.path.join(".", file)]
workbook = openpyxl.load_workbook(xlsxFiles[0])

for sheetName in getSheetList("sheet_list.txt"):
	pklist = []
	worksheet = workbook[sheetName]
	print("CREATE TABLE " + worksheet["C" + str(6)].value + " (")
	outTxt.write("CREATE TABLE " + worksheet["C" + str(6)].value + " (" + newlineCode)
	columnStartRow = 14
	while worksheet["C" + str(columnStartRow)].value is not None:
		columnNameCell = worksheet["C" + str(columnStartRow)]
		print(tabString + columnNameCell.value, end="")
		outTxt.write(tabString + columnNameCell.value)

		typeCell = worksheet["D" + str(columnStartRow)]
		print(tabString + typeCell.value[1:], end="")
		outTxt.write(tabString + typeCell.value[1:])

		optionCell = worksheet["E" + str(columnStartRow)]
		if optionCell.value is not None and "Yes" in optionCell.value:
			print(tabString + "NOT NULL", end="")
			outTxt.write(tabString + "NOT NULL")
		if optionCell.value is not None and "PK" in optionCell.value:
			pklist.append(columnNameCell.value)

		columnStartRow += 1

		if worksheet["C" + str(columnStartRow)].value is not None:
			print(",")
			outTxt.write("," + newlineCode)
		else:
			print("")
			outTxt.write(newlineCode)

	if not pklist == False:
		print(tabString + "PRIMARY KEY(" + ",".join(pklist) + ")")
		outTxt.write(tabString + "PRIMARY KEY(" + ",".join(pklist) + ")" + newlineCode)

	print(");")
	outTxt.write(");" + newlineCode + newlineCode)
