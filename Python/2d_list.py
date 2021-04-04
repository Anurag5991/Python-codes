number_grid = [[1,2,3],
    [4,5,6],
    [7,8,9],
    [0]]
list1 = [3,4]
number_grid.append(list1)
print(number_grid)
print (number_grid[3][0])

for row in number_grid:
    for col in row:
        print(col)
