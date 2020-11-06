number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9], 
    [0]
]

print(number_grid)
for out_index in range(len(number_grid)) :
    for in_index in range(len(number_grid[out_index])) :
        print(number_grid[out_index][in_index])