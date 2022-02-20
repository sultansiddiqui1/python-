#making the opposite of the number guessing game where we make the computer guess the number that we input:
import random

def computer_guess(x):
     lowerbound= 1
     upperbound=x
     feedback=" "
     tries=0

     while(feedback!='c'):
         if lowerbound!=upperbound:
             guess=random.randint(lowerbound, upperbound)
         else:
             guess=lowerbound
             #could also be upperbound but does not matter as they are same.
         tries=tries+1
         feedback=input(f"is {guess} two high (h), too low(l) or correct(c)?").lower()
         if feedback=='h':
            upperbound=guess-1
         elif feedback=='l':
            lowerbound=guess+1
    
     print(f'yay, the compuer guessed the number {guess} correctly.')
     print(f"it took {tries} number of tries")
     



computer_guess(100)



