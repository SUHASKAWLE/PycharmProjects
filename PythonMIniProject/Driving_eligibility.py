age = int(input("Enter your age:"))
if age<7 or age>100:
    print("Please enter a logical age which is b/w 7 and 100.")
elif age > 18:
    print("You are eligible for driving licence.")
elif age < 18:
    print("You are not eligible for driving licence")
else:
    print("Since your age is exactly 18, we would have to take a offline test for your driving licence.")