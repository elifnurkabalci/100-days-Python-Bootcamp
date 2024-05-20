from art import logo

print(logo)

def adder(a,b):
  return a+b
def subtract(a,b):
  return a-b
def multiple(a,b):
  return a*b
def divide(a,b):
  return a/b

c=True
while c:
  a = int(input("What is the first number?"))
  choice ="y"
  while choice == "y":
    print("+")
    print("-")
    print("*")
    print("/")
    op = input("Pick an operation: ")
    b = int(input("What is the next number? "))
    
    result=0
    
    if op == "+":
      result = adder(a,b)
    elif op == "-":
      result = subtract(a,b)
    elif op == "*":
      result = multiple(a,b)
    elif op == "/":
      result = divide(a,b)
    else:
      print("Error")
    
    print(str(a) + op + str(b) + "=" + str(result))
    choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    
    if choice == "y":
      a = result
    else:
      c=True