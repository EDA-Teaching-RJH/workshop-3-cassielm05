import random
secret_number = random.randint(1,10)
attempt = int(input("Guess the number between 1 and 10: "))
if attempt > secret_number:
    print("Too high")
else:
    print("Too low")
