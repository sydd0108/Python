#calculator
import os
os.system('cls')

def add(n1, n2):
  return n1 + n2


def sub(n1, n2):
  return n1 - n2


def mul(n1, n2):
  return n1 * n2


def div(n1, n2):
  return n1 / n2


def calculator():
  operation = {"+": add, "-": sub, "*": mul, "/": div}

  print(" \n\n !!!  Calculator For Your Ease  !!!")

  n1 = float(input("\n\n Enter the first operand :   "))

  print(" \n\n + : add \n  -  : sub  \n  * : mul \n  /  : div  ")
  symbol = input("\n Enter the operation for calculation   ")
  n2 = input("\n\n Enter the  second operand :  ")
  n2 = float(n2)
  operationss = operation[symbol]
  answer = operationss(n1, n2)
  answer = float(answer)
  print(f"\n {n1} {symbol} {n2} = {answer}")

  ans = input(
    "\n\n Wanna continue the calculation(c) or start over(s) or end(e)  (c/s/e)  "
  )

  while ans == "c":
    symbol = input("\n Enter the next operation for calculation :  ")
    n2 = input("\n\n Enter the next operand :   ")
    n2 = float(n2)
    operationss = operation[symbol]
    answer = operationss(answer, n2)
    answer = float(answer)
    print(f"\n {answer}")
    ans = input(
      "\n\n Wanna continue the calculation(c) or start over(s) or end(e)  (c/s/e)  "
    )
  else:
    if ans == "s":
      os.system('cls')
      calculator()
    elif ans == "e":
      print("\n\n Hope it helped.\n\n !!!!! Have a Good Day !!!\n\n")
      exit()
    else:
      print("\n\n Wrong input. Read the instruction again!!\n\n")

if input("\n\n      Here for calculations?? (y/n) : ") == "y":
  calculator()
else:
  print("\n\n!!!!!  Have a Good Day !!!\n\n")
  exit()
