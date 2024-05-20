from art import logo,vs
from game_data import data
import random
print(logo)
count =0

def randomm():
  index = random.randint(0, len(data)-1)
  return data[index]

final_result =True
while final_result:
  first = randomm()
  second = randomm()
  print(f'Compare A: {first["name"]}, a {first["description"]}, from {first["country"]}.')
  print(vs)
  print(f'Against B: {second["name"]},  {second["description"]}, {second["country"]}.')
  
  result = input("Who has more followers? Type 'A' or 'B': ")
  
  if result == "A":
    if first["follower_count"] > second["follower_count"]:
      final_result = True
    else:
      final_result = False
  
  if result == "B":
    if first["follower_count"] < second["follower_count"]:
      final_result = True
    else:
      final_result = False
  
  if final_result:
    print(logo)
    count +=1
    print(f"You are right. Your current score is {count}.")    
  else:
    print(f"Sorry, that is wrong. Final score is: {count}")
    