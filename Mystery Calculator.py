def Mystery_Calculator():
  number = 0
  print ("Pick a number between 1 and 127")
  print ("\n")
  print ("I will now guess your number")
  print ("\n")

  First_Question_Answer = input("Is your number in this list? " + "1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95 97 99 101 103 105 107 109 111 113 115 117 119 121 123 125 127? ")
  if First_Question_Answer == "Yes" or "yes" or "y":
    number = number + 1
    print ("Thank You!")
  else:
    print ("Thank You!")
  
  print ("\n")

  Second_Question_Answer = input("Is your number in this list? " + "2 3 6 7 10 11 14 15 18 19 22 23 26 27 30 31 34 35 38 39 42 43 46 47 50 51 54 55 58 59 62 63 65 67 70 71 74 75 78 79 82 83 86 87 90 91 94 95 98 99 102 103 106 107 110 111 114 115 118 119 122 123 126 127? ")

  if Second_Question_Answer == "Yes" or "yes" or "y":
    number = number + 2
    print ("Thank You!")
  else:
    print ("Thank You!")

  print ("\n")

  Third_Question_Answer = input("Is your number in this list? " + "4 5 6 7 12 13 14 15 20 21 22 23 28 29 30 31 36 37 38 39 44 45 46 47 52 53 54 55 60 61 62 63 68 69 70 71 76 77 78 79 84 85 86 87 92 93 94 95 100 101 102 103 108 109 110 111 116 117 118 119 124 125 126 127? ")

  if Third_Question_Answer == "Yes" or "yes" or "y":
    number = number + 4
    print ("Thank You!")
  else:
    print ("Thank You!")

  print ("\n")

  Fourth_Question_Answer = input("Is your number in this list? " + "8 9 10 11 12 13 14 15 24 25 26 27 28 29 30 31 40 41 42 43 44 45 46 47 56 57 58 59 60 61 62 63 72 73 74 75 76 77 78 79 88 89 90 91 92 93 94 95 104 105 106 107 108 109 110 111 120 121 122 123 124 125 126 127? ")

  if Fourth_Question_Answer == "Yes" or "yes" or "y":
    number = number + 8
    print ("Thank You!")
  else:
    print ("Thank You!")

  print ("\n")

  Fifth_Question_Answer = input("Is your number in this list? " + "16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127? ")

  if Fifth_Question_Answer == "Yes" or "yes" or "y":
    number = number + 16
    print ("Thank You!")
  else:
    print ("Thank You!")

  print ("\n")
  
  Sixth_Question_Answer = input("Is your number in this list " + "32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127? ")

  if Sixth_Question_Answer == "Yes" or "yes" or "y":
    number = number + 32
    print ("Thank You!")
  else:
    print ("Thank You")

  print ("\n")

  Seventh_Question_Answer = input("Is your number in this list " + "64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127? ")

  if Seventh_Question_Answer == "Yes" or "yes" or "y":
    number = number + 64
    print ("Thank You!")
  else:
    print ("Thank You")

  print ("\n")

  print ("Your number is:")
  print (number)

  print ("\n")

  Again_Question = input("Hit A and then Enter to play again! ")
  print ("\n")

  if Again_Question == "A" or "a":
     Mystery_Calculator()

Mystery_Calculator()
