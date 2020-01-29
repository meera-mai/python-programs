import random
n=5
while n>0:
  num= random.randrange(0,10)
  guess =input("enter the guess number")
  if guess==num:
        print "the number is crt"
        break
  else:
        print "lost"
           

