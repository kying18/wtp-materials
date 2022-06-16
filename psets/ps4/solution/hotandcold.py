cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

count = 0

while count < 5 and count > -5:

    current_card = input("What card was played: ")
    print("")
    if current_card not in cards:
        while current_card not in cards:
            current_card = input("That is not a valid card. Please enter a valid card: ")
            print("")

    one_values = cards[1:6]
    zero_values = cards[6:9]

    if current_card in one_values:
        count += 1
    elif current_card in zero_values:
        count = count
    else:
        count -= 1

    if count >= 5:
        print("Deck is hot!")
        break
    if count <= -5:
        print("Deck is cold :(")
        break
