arr = [[3, 15, -1200000, -2, 22],
[-9, 18, -13, -17, -5],
[19, 8, -7, 25, -23],
[20, -11, -10, -24, -4],
[-14, -21, -16, 12, 6]]

summ = 0
for row in arr:
    for num in row:
        if num >= 0:
            summ += num


print(summ)