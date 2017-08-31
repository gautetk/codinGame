import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in raw_input().split()]
n = int(raw_input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in raw_input().split()]
xList = [0, w - 1, x0]
yList = [0, h - 1, y0]
# game loop
while True:
    bomb_dir = raw_input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    if "R" in bomb_dir:
        closest = min(i for i in xList if i > x0)
        x0 = int(x0 + math.ceil((closest - x0) / 2.0))
    elif "L" in bomb_dir:
        closest = max(i for i in xList if i < x0)
        x0 = int(x0 - math.ceil((x0 - closest) / 2.0))
    if "U" in bomb_dir:
        closest = max(i for i in yList if i < y0)
        y0 = int(y0 - math.ceil((y0 - closest) / 2.0))
    elif "D" in bomb_dir:
        closest = min(i for i in yList if i > y0)
        y0 = int(y0 + math.ceil((closest - y0) / 2.0))
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    # the location of the next window Batman should jump to.
    xList.append(x0)
    yList.append(y0)
    print x0, y0

