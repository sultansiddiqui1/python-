#a simple hangman game in python using sets and join


import random
import string
from words import words



def getword(words):
    global word
    word=random.choice(words)#randomly choooses something from the list

    while '-' in word or ' ' in word:
        #some words in our list has a dash or space in between,hence chossing a valid list:

        word = random.choice(words)

    return word.upper()



def hangman():
    lives=6
    word=getword(words)
    wordletters=set(word)#stores all the letters of a word as a set.
    alphabet=set(string.ascii_uppercase)# set of already defined alphabets in the english dictionary
    usedletters=set()#set of used letters by the user.
    
    while len(wordletters)>0 and lives>0:
        print("")

        print("the letters you have used are: ",' '.join(usedletters))# .join  turns any iterable into a string seperated by whatever the string is before the .join, space in our case.
        print("")

        print(f"you have {lives} lives left")

        wordlist=[x if x in usedletters else'-' for x in word]
        print("current word:"," ".join(wordlist))
        userinput=input('enter a letter:').upper()
        if userinput in alphabet- usedletters: 
            usedletters.add(userinput)
            if userinput in wordletters:
               wordletters.remove(userinput)
            else:
                lives=lives-1
                
                print("incorrect, you lost one life!!!!")

    
        elif userinput in usedletters:
            print("you already guessed that charactger. please try again")
    
        else:
           print("invalid character")

    

    if(lives==0):
        print("sorry you lost")
    else:
        print("you won!!!!!")


    print(f"the word is {word}")







hangman()









