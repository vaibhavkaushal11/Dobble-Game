import string
import random
symbol = list(string.ascii_letters)
card1 = [0]*5
card2 = [0]*5
pos1 = random.randint(0, 4)
pos2 = random.randint(0, 4)
same_symbol = random.choice(symbol)
symbol.remove(same_symbol)
if pos1 == pos2:
    card2[pos1] = same_symbol
    card1[pos1] = same_symbol
else:
    card1[pos1] = same_symbol
    card2[pos2] = same_symbol
    card1[pos2] = random.choice(symbol)
    print(card1[pos2])
    symbol.remove(card1[pos2])
    card2[pos1] = random.choice(symbol)
    symbol.remove(card2[pos1])
i = 0
while i < 5:
    if i != pos1 and i != pos2:
        alphabet1 = random.choice(symbol)
        symbol.remove(alphabet1)
        alphabet2 = random.choice(symbol)
        symbol.remove(alphabet2)
        card1[i] = alphabet1
        card2[i] = alphabet2
    i = i+1
while True:
    print("Card 1 :", card1)
    print("Card 2 :", card2)
    ch = input("Enter the Correct Answer = ")
    if ch == same_symbol:
        print("Correct Choice!")
        break
    else:
        print("Try again!", end="\n\n")
