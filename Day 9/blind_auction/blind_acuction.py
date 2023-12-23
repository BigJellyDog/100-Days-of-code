auction_list = []
auction_bets = []
auction_winner = []


def add_new_participant(the_name, money_amount):
    auction_list.append({"name": the_name, "bet": money_amount})


def choose_winner():
    winner_name = ""
    for participant in auction_list:
        auction_bets.append(participant["bet"])

    auction_winner.append(max(auction_bets))
    for participant in auction_list:
        if auction_winner[0] == participant["bet"]:
            winner_name = participant["name"]
    if auction_bets.count(auction_winner[0]) > 1:   # counting if there are more than 1 winner
        auction_winner.clear()  # clear the list and restart
        print("Two people bet the same amount, the auction will restart \n")
    else:
        print(f"The winner is {winner_name} with a bid of {auction_winner[0]}")


# add_new_participant("Chis", 1000)
# add_new_participant("Chis2", 3000)
# add_new_participant("Chis3", 3000)
# add_new_participant("Chis4", 5000)
# add_new_participant("Chis5", 5000)

bidders = "yes"
while bidders == "yes":     # while loop to add all the bidders to the auction

    name = input("What is your name?: ")
    bet = int(input("What is your bid? "))
    add_new_participant(the_name=name, money_amount=bet)    # adding people to auction list, need to redo until all
    # ready
    bidders = input("Are there any other bidders? Type 'yes' or 'no'. \n")
    choose_winner()
    if len(auction_winner) == 0:
        bidders = "yes"













