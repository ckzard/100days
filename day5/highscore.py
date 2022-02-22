def high_score(scores):

    highest_score = 0

    for x in scores:
        if x > highest_score:
            highest_score = x

    print("The highest score in that list is", highest_score)

high_score([78, 65, 89, 86, 55, 91, 64, 89])