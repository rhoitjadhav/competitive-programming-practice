import math


def growingPlant1(up, down, desire):
    days = 1
    height = 0
    if desire <= up:
        return 1

    while True:
        height += up
        if height >= desire:
            return days
        else:
            height -= down
            days += 1


def growingPlant(upSpeed, downSpeed, desiredHeight):
    if desiredHeight <= upSpeed:
        return 1
    return math.ceil((desiredHeight - upSpeed) / (upSpeed - downSpeed) + 1)


up = 6
down = 5
desire = 10

result = growingPlant(up, down, desire)
print(result)
