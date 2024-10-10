
def maths ():
  num1 =int(input("Input a number: "))
  num2 =int(input("Input a number: "))
  operation = input("Choose an operation(+,-,*,/,^,%): ")
  
  if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
  
  elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
  
  elif operation == "/":
    if num2 == "0":
        print("Invalid")
    else:
       result = num1 / num2
       print(f"{num1} / {num2} = {result}")
  
  elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
  
  elif operation == "^":
    result = num1 ^ num2
    print(f"{num1} ^ {num2} = {result}")
    
  elif operation == "%":
    if num2 == "0":
        print("Invalid")
    else:
       result = num1 % num2
       print(f"{num1} % {num2} = {result}")

  else:
    print("Invalid operation")


maths()

command = input("Would you like to continue? ")
while command == "Yes":
     maths()
else:
     print("Quitting the application")








