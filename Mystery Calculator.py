def Mystery_Calculator():
  number = 0
  print ("Pick a number between 1 and 63")
  print ("I will now guess your number")

  First_Question_Answer = input("Is your number in this list? " + "1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63? ")

  if First_Question_Answer == "Yes" or "yes":
    number = number + 1
    print ("Thank You!")
  else:
    print ("Thank You!")

  Second_Question_Answer = input("Is your number in this list? " + "2 3 6 7 10 11 14 15 18 19 22 23 26 27 30 31 34 35 38 39 42 43 46 47 50 51 54 55 58 59 62 63? ")

  if Second_Question_Answer == "Yes" or "yes":
    number = number + 2
    print ("Thank You!")
  else:
    print ("Thank You!")

  Third_Question_Answer = input("Is your number in this list? " + "4 5 6 7 12 13 14 15 20 21 22 23 28 29 30 31 36 37 38 39 44 45 46 47 52 53 54 55 60 61 62 63? ")

  if Third_Question_Answer == "Yes" or "yes":
    number = number + 4
    print ("Thank You!")
  else:
    print ("Thank You!")

  Fourth_Question_Answer = input("Is your number in this list? " + "8 9 10 11 12 13 14 15 24 25 26 27 28 29 30 31 40 41 42 43 44 45 46 47 56 57 58 59 60 61 62 63? ")

  if Fourth_Question_Answer == "Yes" or "yes":
    number = number + 8
    print ("Thank You!")
  else:
    print ("Thank You!")

  Fifth_Question_Answer = input("Is your number in this list? " + "16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63? ")

  if Fifth_Question_Answer == "Yes" or "yes":
    number = number + 16
    print ("Thank You!")
  else:
    print ("Thank You!")
  
  Sixth_Question_Answer = input("Is your number in this list " + "32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63? ")

  if Sixth_Question_Answer == "Yes" or "yes":
    number = number + 32
    print ("Thank You!")
  else:
    print ("Thank You")

  print ("Your number is:")
  print (number)

  

Mystery_Calculator()
