from random import randint
x = randint(0, 30)
a = 0
r = 0
r = int(input("I thought of a number between 0 and 30. Can you guess it? "))
while True:
  try:
    a += 1
    if r == x:
      print("You got it!")
      break
    elif r > x:
      print("Too high")
      r = int(input("Try again: "))
      a += 1
    else:
      print("Too low")
      r = int(input("Try again: "))
      a += 1
  except ValueError:
    print("Please enter a valid integer.")
    r = int(input("Try again: "))
