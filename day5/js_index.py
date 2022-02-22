def js_index(list, element):
    locations = []
    count = 0

    for x in list:
        if x == element:
            locations.append(count)

        count += 1

    return locations

fruits = ['apple', 'orange', 'pear', 'apple', 'cactus', 'cheese', 'apple']
