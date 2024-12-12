import random

print("Welcome to hangman! Try not to kill Bob :)")

wordchoices = ["apple", "dog", "banana", "glue", "america", "ranger", "juice", "phone", "shoes", "lion", "zebra", "computer", "lunch", "mango", "cupcake", "dog", "fish", "santa", "christmas", "goldfish", "tree", "mobile", "car", "train", "lights", "sleigh"]

word = random.choice(wordchoices)
wordlength = str(len(word))
wordfill = []

def game():    
    print("The word is "+wordlength+" letters long!! After 10 mistakes, Bob dies...")
    i = 0
    lives = 10

    for c in range(int(wordlength)):
        wordfill.append("_")

    while i <= 10:
        print(" ".join(wordfill))
        userguess = input("Guess a letter or a word! (PS: You have "+str(lives)+ " mistakes left...) \n")

        if len(userguess) == 1:
            if userguess in word:
                wordplace = word.rfind(str(userguess))
                print("Yes!! There is an "+ str(userguess)+ " in the word!!")
                wordfill[wordplace]=str(userguess)
            if userguess not in word:
                print("There is no "+ str(userguess)+ " in the word...")
                i = i+1
                lives = lives-1
        if len(userguess) == int(wordlength):
            if userguess == word:
                print("YOU SAVED BOB!!!11!1!")
            if userguess is not word:
                print("The word is not "+ userguess+"...")
                i = i+1
                lives = lives-1
        if 1<len(userguess)<int(wordlength):
            print("You cant guess "+ str(len(userguess))+ " letters at a time, silly")
            i=i+1
            lives = lives-1
        if len(userguess)>int(wordlength):
            print("Bro... its "+ wordlength + " letters long, not "+ str(len(userguess)) +" letters ... silly")
            i = i+1
            lives = lives-1
        if i==10:
            print("you killed bob...")
            quit()

game()
        

