#
# #Factorial method
# def factorial_iterative(n):
#     fact=1
#     for i in range(n):
#         fact=fact * (i+1)
#     return fact
#
#
# number=int(input("Enter number:"))
# print("using factorial method",factorial_iterative(number))
#
#
# #Recursive method
# def factorial_recursive(n):
#     if n==1:
#         return 1
#     else:
#         return n * factorial_recursive(n-1)
#
# number=int(input("Enter number:"))
# print("Using recursivemethod", factorial_recursive(number))



# def fibonacci(n):
#     if n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
# number=int(input("Enter number:"))
# print("fibonacci number", fibonacci(number))



# import turtle
# t=turtle.Turtle()
# t.color("red")
# t.begin_fill()
# t.fillcolor("red")
# t.left(140)
# t.forward(180)
# t.circle(-90,200)
# # t.left(120)
#
#
# t.setheading(60)
# t.circle(-90,200)
# t.forward(180)
# t.end_fill()


# import pyperclip
# pyperclip.copy('data copied from clipboard')
# result = pyperclip.paste()
# print(result)

# import wikipedia
# result = wikipedia.page("king kohli")
# print(result.summary)


# import pyperclip
# text = 'Hi there! I am using Pyperclip'
# pyperclip.copy(text)
# text2 = pyperclip.paste()
# print(text2)