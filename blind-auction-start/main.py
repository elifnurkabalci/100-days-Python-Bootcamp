from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program.")
answer = "yes"
bidders = {}
while answer=="yes":
  name = input("What is your name?:")
  bid = input("What is your bid?:")
  bidders[name] = bid
  answer = input("Are they any bidders?:")
  clear()

temp_bid = 0
for i in bidders:
  if int(temp_bid) < int(bidders[i]):
    temp_bid = bidders[i]
    temp_name = i

print(f"{temp_name} is win with {temp_bid}.")