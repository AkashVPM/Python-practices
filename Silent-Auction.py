import os
def winner(bidder_details):
      highest_bid = 0
      winner =""
      for bidder in bidder_details:
            bidding_price = bidder_details[bidder]
            if bidding_price > highest_bid:
                  highest_bid = bidding_price
                  winner = bidder
      print(f"the winner is {winner} highest bid is {highest_bid}")




bidder_data = {}

while (True):
      customer_name = str(input("Enter Your Name: "))
      bidding_amount = int(input("Enter the bidding amount: "))
      bidder_data[customer_name] = bidding_amount
      more_bidders = str(input("Is there anyone willing to bid 'Yes' or 'No'")).lower()
      if more_bidders == "no":   
            break
      if more_bidders == "yes":
            os.system('cls')

winner(bidder_data)

