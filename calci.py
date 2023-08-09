def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"
def option():
  print("Select operation:")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Exit")
  choice = input("Enter choice (1/2/3/4/5): ")
  
  
  
  if choice == '1':
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
      print("Result:", add(num1, num2))
      option()
  elif choice == '2':
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
      print("Result:", subtract(num1, num2))
      option()
  elif choice == '3':
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
      print("Result:", multiply(num1, num2))
      option()
  elif choice == '4':
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
      print("Result:", divide(num1, num2))
      option()
  elif choice =='5':
    print("Thankyou!!")
    exit()
  else:
      print("Invalid input")
option()
