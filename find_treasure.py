import random
import os
os.system('cls')

row1 = ["🟦","🟦","🟦"]
row2 = ["🟦","🟦","🟦"]
row3 = ["🟦","🟦","🟦"]
map = [row1,row2,row3]
print(f"\n\n{[row1]}\n{[row2]}\n{[row3]}")

mainl_h = random.randint(1,3)
mainl_v = random.randint(1,3)

tmap = map[mainl_h - 1]
tmap[mainl_v - 1] = "🎁"



mainl_h = str(mainl_h)
mainl_v = str(mainl_v)

mainl = mainl_h + mainl_v
print("\n")
l = input("\n Enter the location of the treasure (row column): ")
l = str(l)
if l == mainl:
  print("\n\ncongratulations !! you have found the treasure 🤝 !! \n\n")
  print(f"{[row1]}\n{[row2]}\n{[row3]}")
else :
  print(f"\nTry again with the hint below : \n the horizental line is {mainl_h} \n ")
  l = input("\n Enter the location of the treasure now : ")
  l = str(l)
  if l == mainl:
    print("\n\ncongratulations !! you have found the treasure 🤝 !! \n")
    print(f"{[row1]}\n{[row2]}\n{[row3]}")
  else :
    print("\n\n close enough!! try again...")
    l = input("\n Enter the location of the treasure now : ")
    l = str(l)
    if l == mainl :
      print("\ncongratulations !! you have found the treasure 🤝 !! \n")
      print(f"{[row1]}\n{[row2]}\n{[row3]}")
    else :
       print(f"\n close enough!! the treasure was in {mainl}\n\n")
       print(f"{[row1]}\n{[row2]}\n{[row3]}")
