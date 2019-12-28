import random

print ("This is a simple, text based Dungeons and Dragons dice roller!")
print ("Simply enter the die you wish to roll, and this program will take care of the rest.")
print ("Choose to roll a d2, d4, d6, d8, d10, d12, d20, or d100 by entering the die below.")
print ("Please enter the die you wish roll. Type 'Done' to end the program.")

d2 = random.randint(1,2)
d4 = random.randint(1,4)
d6 = random.randint(1,6)
d8 = random.randint(1,8)
d10 = random.randint(1,10)
d12 = random.randint(1,12)
d20 = random.randint(1,20)
d100 = random.randint(1,100)

while True:
    choice = input("Enter die choice: ")
    if choice == "d2":
        print(d2)
    elif choice == "d4":
        print(d4)
    elif choice == "d6":
        print(d6)
    elif choice == "d8":
        print(d8)
    elif choice == "d10":
        print(d10)
    elif choice == "d12":
        print(d12)
    elif choice == "d20":
        print(d20)
    elif choice == "d100":
        print(d100)
    elif choice == "Done":
        break
    else:
        print("That is not a valid input.")