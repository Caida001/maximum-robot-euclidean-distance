
# open and read the file, every line is an array element
with open("input.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line.split(' '))

# get the road blocks' indexes to be a separate array.
blocks = array[1:11]
# use two dictionaries to store x-axis and y-axis pairs
blockx, blocky = {}, {}
for el in blocks:
    blockx[int(el[0])] = int(el[1])
    blocky[int(el[1])] = int(el[0])



moves = array[11:]

import math
import pdb

# initiate currentDirec which is the "L" or "R" we get from the text file. store the direction after all the intermediate changes in direction
x = 0
y = 0
direction = 'north'
currentDirec = ""
maxDis = 0

# set the direction after we get an "L" or "R" from the text file
def setDirection(direction, currentDirec):
    if direction == 'north':
        if currentDirec == "L":
            direction = "west"
        elif currentDirec == "R":
            direction = "east"
    elif direction == 'west':
        if currentDirec == "L":
            direction = "south"
        elif currentDirec == "R":
            direction = "north"
    elif direction == 'south':
        if currentDirec == "L":
            direction = "east"
        elif currentDirec == "R":
            direction = "west"
    elif direction == 'east':
        if currentDirec == "L":
            direction = "north"
        elif currentDirec == "R":
            direction = "south"

    return direction




def getDis(moves, direction, currentDirec, x, y, maxDis, blockx, blocky):
# loop through all the moves, if we get "L" or "R" then set the direction. If we get "M" then we increment or decrement the x, y axis
    for el in moves:
        if el[0][0] == "L":
            currentDirec = "L"
            direction = setDirection(direction, currentDirec)
        elif el[0][0] == "R":
            currentDirec = "R"
            direction = setDirection(direction, currentDirec)
        elif el[0] == "M":
            if direction == "north":
                # check to see if there is roadblock in the way, if there is, break out of the while loop
                if x not in blockx.keys():
                    y += int(el[1])
                else:
                    temp = int(el[1])
                    while temp > 0 and y + 1 != blockx[x]:
                        temp -= 1
                        y += 1

            elif direction == "south":
                if x not in blockx.keys():
                  y -= int(el[1])
                else:
                    temp = int(el[1])
                    while temp > 0 and y - 1 != blockx[x]:
                        temp -= 1
                        y -= 1

            elif direction == "east":
                if y not in blocky.keys():
                  x += int(el[1])
                else:
                    temp = int(el[1])
                    while temp > 0 and x + 1 != blocky[y]:
                        temp -= 1
                        x += 1

            elif direction == "west":
                if y not in blocky.keys():
                  x -= int(el[1])
                else:
                    temp = int(el[1])
                    while temp > 0 and x - 1 != blocky[y]:
                        temp -= 1
                        x -= 1
        # every time the location changes, we calculate the new euclidean ditance and compare it with the previous value we stored in maxDis, and store the bigger one
            if math.sqrt(x ** 2 + y ** 2) > maxDis: maxDis = math.sqrt(x ** 2 + y ** 2)

    return maxDis



print(getDis(moves, direction, currentDirec, x, y, maxDis, blockx, blocky))
