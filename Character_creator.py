import random

def roll_d6():
    rolled_number = random.randint(1,6)
    return rolled_number

stats = [
"strength",
"charisma",
"intelligence",
"wisdom",
"constitution",
"dexterity"
]

points = []
for i in stats:
    rolls = []
    for j in range(4):
        rolls.append(roll_d6())
    rolls.sort(reverse=True)
    point = 0
    for j in rolls:
        point += j
    points.append(point)
print(points)
