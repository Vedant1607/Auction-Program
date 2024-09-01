from art import logo
print(logo)

price = {}
bidding = True

def find_highest_bidder(bidding_dictionary):
    highest_bidder = max(bidding_dictionary, key=bidding_dictionary.get)
    highest_bid = bidding_dictionary[highest_bidder]
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")

while bidding:
    name = input("What is your name?")
    bid = int(input("What is your bid?: $"))

    price[name] = bid
    more_bidders = input("Are there any other bidders ? Type 'yes' or 'no'")
    if more_bidders == "no":
        bidding = False
        find_highest_bidder(price)
    elif more_bidders == "yes":
        print("\n" * 20)
