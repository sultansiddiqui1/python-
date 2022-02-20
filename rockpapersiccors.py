#a simple rock paper siccoers game in python:

import random

def game():
     user=input(" whats your choice:'r' for rock,'p' for papers,'s' for siccors ")
     computer=random.choice(['r','p','s'] )

     if user==computer :
         return ' it is a tie'
     
     if iswin(user,computer):
         return("you win")
   
     return "you lost"

        

def iswin(player, opponent):
     if(player=='r' and opponent =='s')or (player=='p' and opponent=='r') or (player=='s' and opponent=='p'):
         return True
             
 



print(game())
