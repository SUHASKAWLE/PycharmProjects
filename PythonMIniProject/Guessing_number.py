"""RULES = " \n1. YOU WILL GET HINT AFTER EVERY FAIL.\n" \
        "2. YOU WILL GET TO KNOW THAT HOW MUCH ATTEMPTS LEFT IN GAME.\n" \
        "3. THERE ARE THREE ATTEMPTS.\n" \
        "4. YOU WILL GET A BREAK AFTER YOU WON.\n" \
        "5. ENJOY."""
i = 0
while True:
    if i <= 9:
        i = i + 1
        print("no. of attempt left", 10 - i)
    x = int(input("Guess a no:"))
    if x > 35:
        print("no. you guessed number is quite larger")
    elif x < 5:
        print("no. you guessed number is quite smaller")
    elif 5 <= x <= 10:
        print("your guessed number is a bit lessor")
    elif 10 < x <= 15:
        print("you are nearby guessed number")
    elif 15 < x < 18:
        print("almost there")
    elif 18 < x < 23:
        print("a bit larger")
    elif 23 <= x <= 35:
        print("more larger")
    elif x == 18:
        print("congratulations! you guessed a correct number")
        break

    if i >= 9:
        print("Game over. Better luck next time\n")
        break
