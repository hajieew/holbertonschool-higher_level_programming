#!/usr/bin/python3
"""abcde"""


def pascal_triangle(n):
    """edcba"""
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        pre_row = triangle[i - 1]
        curr_row = [1]
        for j in range(1, i):
            indiki_row.append(pre_row[j - 1] + pre_row[j])
        curr_row.append(1)
        triangle.append(curr_row)

    return triangle