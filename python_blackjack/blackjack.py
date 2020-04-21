import random
# Dealer Cards 
dealer_cards = []

# Player Cards
player_cards = []

# Dealer Cards Selection
while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1, 11))
    if len(dealer_cards) == 2:
        print("Dealer has: X &", dealer_cards[1])

# Player Cards Selection
while len(player_cards) != 2:
    player_cards.append(random.randint(1, 11))
    if len(player_cards) == 2:
        print("Player has: ", player_cards)

# Sum Of Dealer's Cards
if sum(dealer_cards) == 21:
    print("BLACKJACK")
elif sum(dealer_cards) > 21:
    print("Dealer has a total greater than 21 and loses")

# Sum Of Player's Cards
while sum(player_cards) < 21:
    action_taken = str(input("Do You Want To Stay Or Hit ?"))
    if action_taken == "hit":
        player_cards.append(random.randint(1, 11))
        print("You have a total of " + str(sum(player_cards)) + " with these cards", player_cards)
    else:
        print("The dealer has a total of " + str(sum(dealer_cards)) + "with these cards", dealer_cards)
        print("You have a total of " + str(sum(player_cards)) + " with these cards", player_cards)
        if sum(dealer_cards) > sum(player_cards):
            print("Dealer's sum is close to 21 and he wins!!!")
        else:
            print("You have a sum that is close to 21 and you win!!!")
            break

if sum(player_cards) == 21:
    print("BLACKJACK")
elif sum(player_cards) > 21:
    print("You have a total greater than 21 and you lose")