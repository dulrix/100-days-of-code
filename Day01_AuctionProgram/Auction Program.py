print('''  ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                   jgs/_______________\'''')



print("WELCOME TO THE AUCTION")

bids = {}
bidding_finished = False
while not bidding_finished:
    name = input("Please enter your name: ")
    bid = int(input("Enter bid amount: $"))
    bids[name] = bid

    repeat = input("Are there any more bidder? Type 'yes' or 'no': ").lower()
    
    if repeat == 'no':
        bidding_finished = True
    else:
        print("\n" * 20)


highest_bid = 0
winner = ""

for bidder in bids:
    if bids[bidder] > highest_bid:
        highest_bid = bids[bidder]
        winner = bidder 

print(f"The winner is {winner} with a bid of ${highest_bid}. ")
