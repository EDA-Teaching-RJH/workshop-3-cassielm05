score = int(input("What is the numerical score out of 100? :"))
if score >= 90:
    print("You have achieved an A")
elif score >= 80:
    print("You have achieved a B")
elif score >= 70:
    print("You have achieved a C")
elif score >= 60:
    print("You have achieved a D")
elif score < 0 or score > 100:
    print("Error. Try again.")
else:
    print("You have achieved a F")
 

