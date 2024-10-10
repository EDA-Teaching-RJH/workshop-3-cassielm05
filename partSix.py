age = int(input("How old are you? "))
student = (input("Are you a student? "))

if age >= 65 or age <= 12 :
    print("Tickets cost £5")

elif student == "yes" and (age > 12 or age < 65):
    print("Tickets cost £8")

else:
    print("Tickets cost £10")
