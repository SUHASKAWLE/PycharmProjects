""" Welcome to Pattern Printer System.
Please enter an integer whose sized pattern you want to see.
also enter a either 0 or 1 to control the visibility of pattern
for ex:- if 0 is entered then it will show reversed pattern else it will show normal pattern..
"""


print("How Many Row You Want To Print")
one = int(input())
print("Type 1 Or 0")
two = int(input())
new = bool(two)
if new == True:
    for i in range(1, one+1):
        for j in range(1, i+1):
            print("*", end=" ")
        print()
elif new ==False:
    for i in range(one, 0,-1):
        for j in range(1, i+1):
            print("*", end="")
        print()

