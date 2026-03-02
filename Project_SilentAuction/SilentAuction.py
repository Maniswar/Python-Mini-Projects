import os
def find_winner(bidder_details):
    # winner = max(bidder_details, key=bidder_details.get)
    # print(f"The winner is {winner} with a bid of {bidder_details[winner]}")
    highest_bid= 0
    for bidder in bidder_details:
        bidding_price = bidder_details[bidder]
        if bidding_price>highest_bid:
            highest_bid=bidding_price
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")

print("***** Welcome to the bid!!!! *****")
bidder_data={}
end_of_bidding = False
while not end_of_bidding:

    bidder_name = input("what is your name?: ")
    bid= int(input("what is your bid?: "))
    bidder_data[bidder_name]= bid
    check_another_bidder = input("Are there any other bidders? Type 'yes' or 'no':\n")
    yes_no = check_another_bidder.lower()

    if yes_no == "no":
        end_of_bidding = True
        os.system("cls")
        print(bidder_data)
        find_winner(bidder_data)
        # print(bidder_data)
    elif yes_no == "yes":
        os.system("cls")
