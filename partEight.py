print("Welcome to the decision game. You are in a forest and your decisions are all yours.")
lives = 5
print("You have 5 lives")
inventory = []


def left():
    print("You have turned left. You are walking through the woods")
    print("You have reached a treasure box.")
    box = input("Will you open the box? (Y/N)")
    if box == "Y":
        print ("You have gained a life")
        lives = lives + 1
        print ("You currently have", {lives}, "lives. We will proceed.")
    else:
        print("You have not chosen a box. We will proceed.")

def straight():
    print("You have continued forward.")
    print("You have come across a puzzle")
    import random
    secret_number = random.randint(1,10)
    attempt = int(input("Guess the number between 1 and 10: "))
    if attempt == secret_number:
        print("Congratulations. You have won a food pack to restore stamina!")
        inventory.append("Food pack")
    else:
        print("Unfortunately, you didn't guess the number so I will take a life.")
        lives = lives - 1
        print("You currently have", {lives}, "lives. We will proceed.")


def right():
    print("You have turned right. You are walking through the woods")
    print("You see a shiny thing in the bushes.")
    shiny = input("Will you pick up the shiny thing? (Y/N)")
    if shiny == "Y":
        print ("You have added a knife to your inventory.")
        inventory.append("Knife")
    else:
        print("We will proceed")


def right2():
    print("You have turned right. You are walking through the woods")
    print("You hear a noise in the bushes.")
    nosy = input("Will look at the noise? (Y/N)")
    if nosy == "Y":
        print ("You have fallen into a hole. Your inventory will be emptied")
        inventory.clear()
    else:
        print("We will proceed")

print("You have now entered the depths of the forest.")
direction1 = input("Which direction do you want to go? (Left/Right)")
if direction1 == "Left":
    left()
else:
    right()

print("You have now entered the swamps of the forest.")
direction2 = input("Which direction do you want to go? (Straight/Right)")
if direction2 == "Right":
    right2()
else:
    straight()


