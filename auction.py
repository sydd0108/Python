import os
os.system('cls')
bidders = {}
print("Welcome to the auction.\n")
print("          Try your best!!        \n")
n = input("Enter your name :  ")
amt = input("\nEnter the amount you want to bid for ths product :  ")
bidders[n] = amt
max = amt
name = n
check = input("\n\n Are there ant other bidders (y/n):  ")
while check == "y":
  os.system('cls')
  n = input("Enter your name :  ")
  amt = input("\nEnter the amount you want to bid for ths product :  ")
  bidders[n] = amt
  check = input("\n\n Are there ant other bidders (y/n):  ")
print("\n The auction result is : \n")
print(bidders)

for thing in bidders:
  if int(bidders[thing]) > int(max):
    max = bidders[thing]
    name = thing

print(f"\n\nThe winner of the auction is {name} with price {max}")
