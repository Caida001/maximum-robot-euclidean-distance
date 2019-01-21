# maximum-robot-euclidean-distance

### summary

Given a file containing information regarding the direction and distance a robot has to travel, calculate the maximum euclidean distance from the starting position to any position the robot could been.

### main logic of the algorithm 

```Python
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
```
