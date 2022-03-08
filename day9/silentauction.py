import os


def silent_auction():
    f = open ('day9\devil.txt','r')

    print(''.join([line for line in f]))
    print("\n")
    print("WELCOME TO HELL'S SILENT AUCTION")


    bidders = {}

    bidder = input("Please enter your name: \n")
    bid_amount = input("Please enter your bid: \n")

    bidders[bidder] = bid_amount

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no': \n")

    while more_bidders == 'yes':
        os.system("clear")
        bidder = input("Please enter your name: \n")
        bid_amount = int(input("Please enter your bid: \n"))

        bidders[bidder] = bid_amount

        more_bidders = input("Are there any other bidders? Type 'yes' or 'no': \n")

    highest_bid = 0
    highest_bidder = ''
    ties = []

    for bidder in bidders:
        if int(bidders[bidder]) > highest_bid:
            highest_bidder = bidder
            highest_bid = int(bidders[bidder])
            
    print("The winner is", highest_bidder, "with a bid of $" + str(highest_bid))

silent_auction()
