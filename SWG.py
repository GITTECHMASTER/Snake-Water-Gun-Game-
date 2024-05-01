import random


for i in range(0, 3):
  You = input("Enter one from S W G: ")
  You = You.upper()
  print(You)
  y = ["S", "W", "G"]
  z = random.choice(y)
  print(z)
  if z == "S" and You == "G":
   print("You win the game")
  elif z == "S" and You == "W":
   print("Computer win the game")
  elif z == "G" and You == "W":
   print("You win the game")
  elif z == "G" and You == "S":
   print("Computer win the game")
  elif z == "W" and You == "S":
   print("You win the game")
  elif z == "W" and You == "G":
   print("Computer win the game")
  elif z==You:
   print("Match is Draw")