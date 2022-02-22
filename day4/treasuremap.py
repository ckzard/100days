def treasure_map():
    row1 = ["⬜", "⬜", "⬜"]
    row2 = ["⬜", "⬜", "⬜"]
    row3 = ["⬜", "⬜", "⬜"]

    spot = "❌"

    map = [row1, row2, row3]
    print(f"{row1}\n{row2}\n{row3}")

    picked_spot = input("Please enter the coordinate for the treasure spot (e.g 31 is the top right corner) ")

    coords = []

    for char in picked_spot:
        coords.append(int(char))

    if coords[1] == 1:
        row1[coords[0] - 1] = spot
    elif coords[1] == 2:
        row2[coords[0] - 1] = spot
    else:
        row3[coords[0] - 1] = spot


    print(f"{row1}\n{row2}\n{row3}")

treasure_map()