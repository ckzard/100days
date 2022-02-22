def ave_heights(heights):

    total = 0

    for n in heights:
        total += n

    for n in range(len(heights)):
        print(n)
    # This will print the index

    print(round(total / len(heights)))

ave_heights([180, 124, 165, 173, 189, 169, 146])