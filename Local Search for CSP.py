import random

colors = ["Red", "Green", "Blue"]

assignment = {
    "A": "Red",
    "B": "Red",
    "C": "Blue"
}

neighbors = {
    "A": ["B"],
    "B": ["A", "C"],
    "C": ["B"]
}

for i in range(10):
    conflicts = []

    for region in assignment:
        for neighbor in neighbors[region]:
            if assignment[region] == assignment[neighbor]:
                conflicts.append(region)

    if not conflicts:
        break

    region = random.choice(conflicts)
    assignment[region] = random.choice(colors)

print("Final Coloring:")
for region, color in assignment.items():
    print(region, ":", color)
