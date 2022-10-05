import random
randomint = random.randint(1,100)
guess = True
tries = 0
while guess == True:
    num = int(input("Guess the number: "))
    if ( randomint > num):
        n = randomint - num
        if (n>=25):
          print("Way too low!")
        elif (n >= 7 and n < 25):
          print("Too low!")
        elif (n >= 1 and n < 7):
          print("A little too low!")
    elif ( randomint < num):
      j = num - randomint
      if (j>=25):
        print("Way too high!")
      elif (j >= 7 and j < 25):
        print("Too high!")
      elif (j >= 1 and j < 7):
        print("A little too high!")
    else:
      if (tries == 1):
        print("Are you a psychic?!")
        guess = False
        break
      elif (tries > 1):
        print("Correct!")
        guess = False
        break
    tries+=1