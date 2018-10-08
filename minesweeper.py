import random

sz = 20 # global variable, the size of the board

# This function, given a 2D list of bools, outputs a 2D list where each element
# contains the number of adjacent squares that have a land mine!
def count_nearby_mines(mines_list):
    ncount = []

    # make ncount the same size as input mines_list
    for i in range(0, sz):
        ncount.append([])
        for j in range (0, sz):
            ncount[i].append(0)
    
    # count up each cell's True neighbors
    for y in range(0, len(mines_list)):
        for x in range (0, len(mines_list[i])):
            if (mines_list[y-1][x-1] == True):
                ncount[y][x] += 1
            if (mines_list[y-1][x] == True):
                ncount[y][x] += 1
            if (mines_list[y-1][x+1] == True):
                ncount[y][x] += 1
         
            if (mines_list[y][x-1] == True):
                ncount[y][x] += 1
            if (mines_list[y][x+1] == True):
                ncount[y][x] += 1

            if (mines_list[y+1][x-1] == True):
                ncount[y][x] += 1
            if (mines_list[y+1][x] == True):
                ncount[y][x] += 1
            if (mines_list[y+1][x+1] == True):
                ncount[y][x] += 1

    return ncount


def print_board(mines_list, ncount):
    for i in range (0, sz):
        for j in range (0, sz):
            if (mines_list[i][j] = True):
                print('X', end='')
            else:
                print(ncount[i][j], end='')

        print('') # new line


def main():
    # initialize mines_list
    mines_list = []
    for i in range(0, sz):
        mines_list.append([])
        for j in range (0, sz):
            mines_list[i].append(False)

    # randomly place 5 mines   
    for k in range (0, 5):
        y = random.randint(0, sz)
        x = random.randint(0, sz)
        mines_list[y][x] = True

    ncount = count_nearby_mines(mines_list)

    print_board(mines_list, ncount)

main()
