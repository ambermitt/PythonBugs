def live_neighbor_counter(grid):

    ncount = [] # this list will store the number of True neighbors each cell in the input grid has

    # make ncount the same size as input grid
    for i in range(0, len(grid):
        ncount.append([])
        for j in range (0, len(grid[i])):
            ncount[i].append(0)
    
    # count up each cell's True neighbors
    for y in range(0, len(grid)):
        for x in range (0, len(grid[i])):
            if (grid[y-1][x-1] == True):
                ncount[y][x] += 1
            if (grid[y-1][x] == True):
                ncount[y][x] += 1
            if (grid[y-1][x+1] == True):
                ncount[y][x] += 1
         
            if (grid[y][x-1] == True):
                ncount[y][x] += 1
            if (grid[y][x+1] == True):
                ncount[y][x] += 1

            if (grid[y+1][x-1] == True):
                ncount[y][x] += 1
            if (grid[y+1][x] == True):
                ncount[y][x] += 1
            if (grid[y+1][x+1] == True):
                ncount[y][x] += 1

    return ncount
