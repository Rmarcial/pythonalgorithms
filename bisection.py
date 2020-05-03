"""
Bissection Search Algorithm to guess a number
"""

from sqrt import average


guess_counter = 1
lower = 0
higher = 1000
print("Think of a number between", lower, "and", higher)

while True:
    guess = int(average(lower, higher))
    print("My guess is:", guess)

    reply = input("Is it right? Type 'yes' or 'no'")

    if reply == 'yes':
        print("BINGO !")
        break

    else:
        guess_counter += 1
        hint = input("Well... is it bigger or smaller? Type 'bigger' or 'smaller'")

        if hint == 'bigger':
            lower = guess
        else:
            higher = guess

print("Too easy... only",  guess_counter, "attempts!")

