import fileinput
import copy

fileinput.close()
filename = 'Jour4\\input.txt'
f = open(filename, 'r')

DIRECTIONS = [(0,1),(1,1),(1,0),(1,-1),(-1,0),(-1,-1),(0,-1),(-1,1)]

grid = []

for line in f.readlines():
    array = [i for i in str(line[0:-1])]
    grid.append(array)

numrow = len(grid)
numcolumn = len(grid[0])

def checkadja(row,column):
    for dirrow, dircolumn in DIRECTIONS:
        potrow, potcolumn = row + dirrow, column + dircolumn
        if 0 <= potrow < numrow and 0 <= potcolumn < numcolumn:
            yield grid[potrow][potcolumn]



def removerolls(gridtoremove):
    totalroll = 0
    newgrid = copy.deepcopy(gridtoremove)
    for row in range(numrow):
        for col in range(numcolumn):
            if(grid[row][col] == '@'):
                if(list(checkadja(row,col)).count('@') < 4):
                    totalroll += 1
                    newgrid[row][col] = '.'
    return newgrid, totalroll


totalroll = 0

while True :
    grid, onceroll = removerolls(grid)
    totalroll += onceroll
    if(onceroll == 0):
        break

print(totalroll)