
import os

alphabet = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'x', 'y', 'z'
   ]

def decode(text, shift, alphabet):
  decoded = ''
  for letter in text:
    if letter == ' ':
      decoded += ' '
    else:
      position = alphabet.index(letter)
      newposition = position - shift
      if newposition < 0:
        newposition = 27 + newposition
      decoded += alphabet[newposition]

  return decoded
  

def encode(text, shift, alphabet):
  encoded = ''
  for letter in text:
    if letter == ' ':
      encoded += ' '
    else:
      position = alphabet.index(letter)
      newposition = position + shift
      if newposition > 27:
        newposition = newposition - 27
      encoded += alphabet[newposition]

  return encoded

def go(ans):
       while ans == "y":
            direction = input("\n\n Enter encode for encrypting and decode for decrypting : \n").lower()
            if direction == 'decode':
                message = input("\nEnter the message : \n").lower()
                shift = int(input("\n enter the no of shifts : \n"))
                decodedd = decode(message, shift, alphabet)
                print(f"\n The decoded message is : {decodedd}\n\n")
                ans = input("Wanna continue with it ?? (y/n) :  ")
                
            if direction == 'encode':
                message = input("\nEnter the message : \n").lower()
                shift = int(input("\n enter the no of shifts : \n"))
                encodedd = encode(message, shift, alphabet)
                print(f"\n The encoded message is : {encodedd}\n\n")
                ans = input("Wanna continue with it ?? (y/n) :  ")
       else:
        print("\n\n Have a Good Day!!!\n\n")
        exit()


os.system('cls')
print("    !!!Welcome to encode and decode program !!!!\n\n")
ans = input("Wanna do somce encoding decoding ?? (y/n) :  ")
if ans == "y":
  go(ans)
else:
   print("\n!!!Have a Good Day!!!\n\n")
   exit()


# direction = input(
#   "Enter encode for encrypting and decode for decrypting : \n").lower()


# if direction == 'encode':
#   message = input("\nEnter the message : \n").lower()
#   shift = int(input("\n enter the no of shifts : \n"))
#   encodedd = encode(message, shift, alphabet)
#   print(f"\n The encoded message is : {encodedd}\n\n")
#   ans = input("Wanna continue with it ?? (y/n) :  ")
#   go(ans)


# if direction == 'decode':
#   message = input("\nEnter the message : \n").lower()
#   shift = int(input("\n enter the no of shifts : \n"))
#   decodedd = decode(message, shift, alphabet)
#   print(f"\n {decodedd}\n\n")
#   ans = input("Wanna continue with it ?? (y/n) :  ")
#   go(ans)
