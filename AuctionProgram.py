print("*** Welcome to the secret auction program ***")

# def bid_with_us(bidding_auction):
#     bidder_name = ""
#     highest_amount = 0
#     for bidder in bidding_auction:
#         bidder_amount = bidding_auction[bidder]
#         if bidder_amount > highest_amount:
#             highest_amount = bidder_amount
#             bidder_name = bidder

#     print(f"The winner is {bidder_name} with bid of ${highest_amount}")


# auction_bid = {}
# while True:
#     name = input("What is your name?: ")
#     bid = int(input("What's your bid: $"))

#     auction_bid[name] = bid
#     choose = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
#     if choose == 'yes':
#         print("\n" * 20)
#     elif choose == 'no':
#         bid_with_us(auction_bid)
#         break
#     else:
#         print("type 'yes' or 'no'.")

# print(auction_bid)

def biddingAuc(bidding):
    bidderName = ""
    highestAmount = 0
    for bidder in bidding:
        if bidding[bidder] > highestAmount:
            highestAmount = bidding[bidder]
            bidderName = bidder
    
    print(f"The winner is {bidderName} with bid of ${highestAmount}")


bidding_auction = {}
while True:
    name = input("What is your name?: ")
    bid = int(input("What's your bid: $"))

    bidding_auction[name] = bid
    choose = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    if choose == 'yes':
        print("\n" * 20)
    elif choose == 'no':
        biddingAuc(bidding_auction)
        break
    else:
        print("Please type correctly.")
        choose = input("Are there any other bidders? Type 'yes' or 'no': ").lower()