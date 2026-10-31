colors = ["Red", "Green", "Blue"]

regions = ["A", "B", "C"]

neighbors = {
    "A": ["B", "C"],
    "B": ["A", "C"],
    "C": ["A", "B"]
}

assignment = {}

def color_map(region):
    if region == len(regions):
        return True

    current = regions[region]

    for color in colors:
        valid = True

        for neighbor in neighbors[current]:
            if assignment.get(neighbor) == color:
                valid = False

        if valid:
            assignment[current] = color

            if color_map(region + 1):
                return True

            del assignment[current]

    return False

if color_map(0):
    print("Map Coloring:")
    for region, color in assignment.items():
        print(region, ":", color)
