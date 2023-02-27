<<<<<<< HEAD



print("Welcome to the Health Management System")

log = 1
retrieve = 2
diet = 1
exercise = 2
Suhas = 1
Pavan = 2
Vaishnavi = 3
Vaibhav = 4

def getdate():
    import datetime
    return datetime.datetime.now()
time = str(getdate())

a = int(input("Enter your choice\n" + "Press 1 for log and 2 for retrieve\n"))
b = int(input("Choose diet by pressing 1 and exercise by pressing 2\n"))
c = int(input("Enter the name\n" + "1 for Suhas, 2 for Pavan, 3 for Vaishnavi and 4 for Vaibhav\n"))

if a == log and b == diet and c == Suhas:
    with open("Suhas Diet", "a") as f1:
        f1.write(" \n")
        f1.write(time + "   - ")
        print(f1.write(input("\nwrite what you want to add in your diet\n")))

if a == log and b == diet and c == Pavan:
    with open("Pavan Diet.txt", "a") as f2:
        f2.write(" \n")
        f2.write(time + "   - ")
        print(f2.write(input("\nwrite what you want to add in your diet\n")))

if a == log and b == diet and c == Vaishnavi:
    with open("Vaishnavi Diet.txt", "a") as f3:
        f3.write(" \n")
        f3.write(time + "   - ")
        print(f3.write(input("\nwrite what you want to add in your diet\n")))

if a==log and b==diet and c==Vaibhav:
    with open("Vaibhav Diet.txt","a") as f4:
        f4.write(" \n")
        f4.write(time +"   - ")
        print(f4.write(input("\nwrite what you want to add in your diet\n")))

if a == log and b == exercise and c == Suhas:
    with open("Suhas Exercise", "a") as f1:
        f1.write(" \n")
        f1.write(time + "   - ")
        print(f1.write(input("\nwrite what you want to add in your exercise\n")))

if a == log and b == exercise and c == Pavan:
    with open("Pavan Exercise.txt", "a") as f2:
        f2.write(" \n")
        f2.write(time + "   - ")
        print(f2.write(input("\nwrite what you want to add in your exercise\n")))

if a == log and b == exercise and c == Vaishnavi:
    with open("Vaishnavi Exercise.txt", "a") as f3:
        f3.write(" \n")
        f3.write(time + "   - ")
        print(f3.write(input("\nwrite what you want to add in your exercise\n")))

if a==log and b==exercise and c== Vaibhav:
    with open("Vaibhav Exercise.txt","a") as f4:
        f4.write(" \n")
        f4.write(time + "   - ")
        print(f4.write(input("\nwrite what you want to add in your exercise\n")))

if a == retrieve and b == exercise and c == Suhas:
    with open("Suhas Exercise", "rt") as f5:
        print(f5.read())

if a == retrieve and b == exercise and c == Pavan:
    with open("Pavan Exercise.txt", "rt") as f6:
        print(f6.read())

if a == retrieve and b == exercise and c == Vaishnavi:
    with open("Vaishnavi Exercise.txt", "rt") as f7:
        print(f7.read())

if a == retrieve and b == exercise and c == Vaibhav:
    with open("Vaibhav Exercise.txt", "rt") as f8:
        print(f8.read())

if a == retrieve and b == diet and c == Suhas:
    with open("Suhas Diet", "rt") as f5:
        print(f5.read())

if a == retrieve and b == diet and c == Pavan:
    with open("Pavan Diet.txt", "rt") as f6:
        print(f6.read())

if a == retrieve and b == diet and c == Vaishnavi:
    with open("Vaishnavi Diet.txt", "rt") as f7:
        print(f7.read())

if a == retrieve and b == diet and c == Vaibhav:
    with open("Vaibhav Diet.txt", "rt") as f8:
=======
<<<<<<< HEAD



print("Welcome to the Health Management System")

log = 1
retrieve = 2
diet = 1
exercise = 2
Suhas = 1
Pavan = 2
Vaishnavi = 3
Vaibhav = 4

def getdate():
    import datetime
    return datetime.datetime.now()
time = str(getdate())

a = int(input("Enter your choice\n" + "Press 1 for log and 2 for retrieve\n"))
b = int(input("Choose diet by pressing 1 and exercise by pressing 2\n"))
c = int(input("Enter the name\n" + "1 for Suhas, 2 for Pavan, 3 for Vaishnavi and 4 for Vaibhav\n"))

if a == log and b == diet and c == Suhas:
    with open("Suhas Diet", "a") as f1:
        f1.write(" \n")
        f1.write(time + "   - ")
        print(f1.write(input("\nwrite what you want to add in your diet\n")))

if a == log and b == diet and c == Pavan:
    with open("Pavan Diet.txt", "a") as f2:
        f2.write(" \n")
        f2.write(time + "   - ")
        print(f2.write(input("\nwrite what you want to add in your diet\n")))

if a == log and b == diet and c == Vaishnavi:
    with open("Vaishnavi Diet.txt", "a") as f3:
        f3.write(" \n")
        f3.write(time + "   - ")
        print(f3.write(input("\nwrite what you want to add in your diet\n")))

if a==log and b==diet and c==Vaibhav:
    with open("Vaibhav Diet.txt","a") as f4:
        f4.write(" \n")
        f4.write(time +"   - ")
        print(f4.write(input("\nwrite what you want to add in your diet\n")))

if a == log and b == exercise and c == Suhas:
    with open("Suhas Exercise", "a") as f1:
        f1.write(" \n")
        f1.write(time + "   - ")
        print(f1.write(input("\nwrite what you want to add in your exercise\n")))

if a == log and b == exercise and c == Pavan:
    with open("Pavan Exercise.txt", "a") as f2:
        f2.write(" \n")
        f2.write(time + "   - ")
        print(f2.write(input("\nwrite what you want to add in your exercise\n")))

if a == log and b == exercise and c == Vaishnavi:
    with open("Vaishnavi Exercise.txt", "a") as f3:
        f3.write(" \n")
        f3.write(time + "   - ")
        print(f3.write(input("\nwrite what you want to add in your exercise\n")))

if a==log and b==exercise and c== Vaibhav:
    with open("Vaibhav Exercise.txt","a") as f4:
        f4.write(" \n")
        f4.write(time + "   - ")
        print(f4.write(input("\nwrite what you want to add in your exercise\n")))

if a == retrieve and b == exercise and c == Suhas:
    with open("Suhas Exercise", "rt") as f5:
        print(f5.read())

if a == retrieve and b == exercise and c == Pavan:
    with open("Pavan Exercise.txt", "rt") as f6:
        print(f6.read())

if a == retrieve and b == exercise and c == Vaishnavi:
    with open("Vaishnavi Exercise.txt", "rt") as f7:
        print(f7.read())

if a == retrieve and b == exercise and c == Vaibhav:
    with open("Vaibhav Exercise.txt", "rt") as f8:
        print(f8.read())

if a == retrieve and b == diet and c == Suhas:
    with open("Suhas Diet", "rt") as f5:
        print(f5.read())

if a == retrieve and b == diet and c == Pavan:
    with open("Pavan Diet.txt", "rt") as f6:
        print(f6.read())

if a == retrieve and b == diet and c == Vaishnavi:
    with open("Vaishnavi Diet.txt", "rt") as f7:
        print(f7.read())

if a == retrieve and b == diet and c == Vaibhav:
    with open("Vaibhav Diet.txt", "rt") as f8:
=======



print("Welcome to the Health Management System")

log = 1
retrieve = 2
diet = 1
exercise = 2
Suhas = 1
Pavan = 2
Vaishnavi = 3
Vaibhav = 4

def getdate():
    import datetime
    return datetime.datetime.now()
time = str(getdate())

a = int(input("Enter your choice\n" + "Press 1 for log and 2 for retrieve\n"))
b = int(input("Choose diet by pressing 1 and exercise by pressing 2\n"))
c = int(input("Enter the name\n" + "1 for Suhas, 2 for Pavan, 3 for Vaishnavi and 4 for Vaibhav\n"))

if a == log and b == diet and c == Suhas:
    with open("Suhas Diet", "a") as f1:
        f1.write(" \n")
        f1.write(time + "   - ")
        print(f1.write(input("\nwrite what you want to add in your diet\n")))

if a == log and b == diet and c == Pavan:
    with open("Pavan Diet.txt", "a") as f2:
        f2.write(" \n")
        f2.write(time + "   - ")
        print(f2.write(input("\nwrite what you want to add in your diet\n")))

if a == log and b == diet and c == Vaishnavi:
    with open("Vaishnavi Diet.txt", "a") as f3:
        f3.write(" \n")
        f3.write(time + "   - ")
        print(f3.write(input("\nwrite what you want to add in your diet\n")))

if a==log and b==diet and c==Vaibhav:
    with open("Vaibhav Diet.txt","a") as f4:
        f4.write(" \n")
        f4.write(time +"   - ")
        print(f4.write(input("\nwrite what you want to add in your diet\n")))

if a == log and b == exercise and c == Suhas:
    with open("Suhas Exercise", "a") as f1:
        f1.write(" \n")
        f1.write(time + "   - ")
        print(f1.write(input("\nwrite what you want to add in your exercise\n")))

if a == log and b == exercise and c == Pavan:
    with open("Pavan Exercise.txt", "a") as f2:
        f2.write(" \n")
        f2.write(time + "   - ")
        print(f2.write(input("\nwrite what you want to add in your exercise\n")))

if a == log and b == exercise and c == Vaishnavi:
    with open("Vaishnavi Exercise.txt", "a") as f3:
        f3.write(" \n")
        f3.write(time + "   - ")
        print(f3.write(input("\nwrite what you want to add in your exercise\n")))

if a==log and b==exercise and c== Vaibhav:
    with open("Vaibhav Exercise.txt","a") as f4:
        f4.write(" \n")
        f4.write(time + "   - ")
        print(f4.write(input("\nwrite what you want to add in your exercise\n")))

if a == retrieve and b == exercise and c == Suhas:
    with open("Suhas Exercise", "rt") as f5:
        print(f5.read())

if a == retrieve and b == exercise and c == Pavan:
    with open("Pavan Exercise.txt", "rt") as f6:
        print(f6.read())

if a == retrieve and b == exercise and c == Vaishnavi:
    with open("Vaishnavi Exercise.txt", "rt") as f7:
        print(f7.read())

if a == retrieve and b == exercise and c == Vaibhav:
    with open("Vaibhav Exercise.txt", "rt") as f8:
        print(f8.read())

if a == retrieve and b == diet and c == Suhas:
    with open("Suhas Diet", "rt") as f5:
        print(f5.read())

if a == retrieve and b == diet and c == Pavan:
    with open("Pavan Diet.txt", "rt") as f6:
        print(f6.read())

if a == retrieve and b == diet and c == Vaishnavi:
    with open("Vaishnavi Diet.txt", "rt") as f7:
        print(f7.read())

if a == retrieve and b == diet and c == Vaibhav:
    with open("Vaibhav Diet.txt", "rt") as f8:
>>>>>>> 0e54dd0e67c09eccf698fc7be2d0d33abecc3787
>>>>>>> fb2a9a655635d4907ed8dbf2020f15273f21afcc
        print(f8.read())