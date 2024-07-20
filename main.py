"""https://leetcode.com/problems/lucky-numbers-in-a-matrix/description/?envType=daily-question&envId=2024-07-19"""
import sys

matrix = [[7,8],[1,2]]

def check_rows(rows):
	
	min_rows = []

	for row in rows:
		row = sorted(row)
		min_rows.append(row[0])

	return min_rows

def check_columns(rows):
	
	max_columns = []

	for i in range(len(rows[0])):
		column = []
		for row in rows:
			column.append(row[i])
		column = sorted(column)
		max_columns.append(column[-1])

	return max_columns

def get_result(min_rows, max_columns):
	
	for num in min_rows:
		if num in max_columns:
			return num

min_rows = check_rows(matrix)
max_columns = check_columns(matrix)
print(get_result(min_rows, max_columns))