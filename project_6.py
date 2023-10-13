#!usr/bin/env python3
#Jacob Foppes Project 6 Game



#game like pokenmon where you go down differnent paths and can run into pokemon on the way. 
# Uses random to randomly slect a pokemon from a list for you to fight 
# you fight the poken nad it cna wither be cought or run away attacks are effective or ineffective 
# differnt color texts for diffenrt poeple or actions 
#   ie prof oak one color 
#   you heard a rumble in the busehd another 
# for random path lengths: print ... in differnt ammouns based on list of []"......","..",".","..................."]
#use turtle to visualize map
#use tkinter to pupup new window when a fight is happeneing. 
import time
import random     
import os  
from pathlib import Path
import sys
'''Intro: Welocme to the game baisic tutorial.
    Choose your name, color '''
    
# GLOBAL VARIABLES 
savedGames = [] #list of all saved games 
auth_usr = ""
save = "" # users current location in the game  game
owd = os.getcwd()
wokeDex = {} #authenitcated users wokedex 
currentLevel = 0

with open("accounts.txt","r+") as users:
    games = users.read()
    savedGames = games.split("\n")


wokemon = []# list of wokemon-----each poekemon is a list of the pokemon features 
basicWokemon = []
electricWokemon = []
waterWokemon = []
fireWokemon = []
earthWokemon = []
with open("wokemon.txt","r") as allWok:
    for line in allWok:
        

class Wokemon:
    def __init__(self,name,type,hp,strenght,weakness,attack1,attack2):
        self.name = name
        self.type = type
        self.hp = hp
        self.strenght = strenght
        self.weakness = weakness
        self.attack1 = attack1
        self.attack2 = attack2
        
    def getHP(self,hp): # this fucntion will Determin  a random hp number for wild wokemon witin 5 points of the default HP 
        pass
    
        
        
        


def print_slow(str):# Credit : Sebastian - Stack overflow https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
def input_slow(str): # Credit: https://www.101computing.net/python-typing-text-effect/
  for character in str:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()  
  return value  
def battle(randWokemon):# take the pokemon generated orivouse and perfom a battle 
    rwok = (randWokemon[0],randWokemon[1]) # extract name and healktgh
    while True:
        wok = input_slow("\nChoose your Wokemon:\n"+str(wokeDex)+"\n")
        if wok in wokeDex:
            global cwokhealth
            global pwokhealth
            pwokhealth = int(wokeDex[wok])
            print_slow("\nYour HP: " + str(pwokhealth) + "\n") #print player helath 
            cwokhealth = int(rwok[1])
            print_slow("Oponent HP: " + str(cwokhealth) + "\n")# print oponent helath 
            print_slow("\nLooks like its " + wok + " vs " + rwok[0] + "\n")
            time.sleep(1)
            def attack():
                global cwokhealth
                global pwokhealth
                phit1 = random.randrange(0,5,1)#randomly genreated player dammage to compouter 
                cwokhealth -= phit1 #subtract hit points form health 
                print_slow(wok + " Strikes!\nIt does " + str(phit1) + " dammage!\n\n")
                chit1 = random.randrange(0,5,1)#randomly genereated compouter dammage to play
                pwokhealth -= chit1#subtract hit points form health 
                print_slow(rwok[0] + " Strikes!\nIt does " + str(chit1) + " dammage!\n\n")
                print_slow("Oponent HP: " + str(cwokhealth) + "\n")
                print_slow("Your HP: " + str(pwokhealth) + "\n\n")
            attack()
        else:
            print("Please choose a Wokemon from your Wokedex")
            continue
            
        while pwokhealth > 0 and cwokhealth > 0: # while both players health greate than 0 comntinue the attack function 
            attack()
        if pwokhealth <= 0 and  pwokhealth <= cwokhealth: #if comoputer wins
            print_slow("Dang..., Thats tough boss. \nLooks like you lost this one.\nTime to head home and heal your Wokemon\n ")
            loby()
        elif cwokhealth <= 0 and pwokhealth >= cwokhealth: # if player wins
            global currentLevel
            currentLevel += 1
            print_slow("You won!!\nYou now have " + rwok[0] + " added to your wokedex!!\nYou will now move on to "+ str(currentLevel)+"!\n\n")
            wokeDex[rwok[0]] = rwok[1]
            savel()
            loby()
        
def l1():#game level 1
    global wokemon
    print_slow("Welcome to level 1!\n")
    while True:
        path1 = input_slow("You are wlaking down the street and you encounter a set a of 2 trail heads:\n 'Elk Road', and 'Spoon Drive' which do you take \n Enter 'Elk' or 'Spoon'\n").lower()
        if path1 == "elk":
            print_slow("Your walking down the elk path when you spot something in the bushes...\n")
            time.sleep(.75)
            print_slow(".")
            time.sleep(.75)
            print_slow(".")
            time.sleep(.75)
            print_slow(".")
            randWokemon = random.choice(list(wokemon.items())) #chose random Wokemon from dict of wokemon 
            rwok = randWokemon[0] # extract just the name 
            while True:
                fight1 = input_slow("\nA wild " + rwok + " appears!!\n Do you battle? or Run away?\n Enter 'Battle', or 'Run\n").lower()
                if fight1 == "run":
                    print_slow("You got away just in time! Better head back.\n\n")
                    time.sleep(2)
                    break 
                elif fight1 == "battle":
                    battle(randWokemon)
                else:
                    print_slow("Please choose run or battle\n")
                    continue
                
        elif path1 == "spoon":
            print_slow("\nYour walking down the Spoon Path and you come to a fork in the path\n The left looks like it leads to a river, and the right looks to be more forrest.\n ")
            while True:
                lefRig = input_slow("Do you Turn left or right\n").lower()
                if lefRig == "left":
                    print_slow("\nWhile Crossing the shallow end of the river, you see some splashing...")
                    time.sleep(.75)
                    print_slow(".")
                    time.sleep(.75)
                    print_slow(".")
                    randWokemon = random.choice(list(waterWokemon.items())) #chose random Wokemon from dict of wokemon
                    rwok = randWokemon[0] # extract just the name 
                    fight2 = input_slow("\n\nA wild " + rwok + " appears!!\n Do you battle? or Run away?\n Enter 'Battle', or 'Run'\n").lower()
                    if fight2 == "battle":
                        battle(randWokemon)
                    elif fight2 == "run":
                        print_slow("You got away just in time, better head back to that fork in the path...\n\n")
                        continue
                    else:
                        print_slow("Choose battle, or Run.\n")
                elif lefRig == "right":
                    print_slow("Your take a right on Spoon Path when you spot something in the bushes...\n")
                    time.sleep(.75)
                    print_slow(".")
                    time.sleep(.75)
                    print_slow(".")
                    time.sleep(.75)
                    randWokemon = random.choice(list(wokemon.items())) #chose random Wokemon from dict of wokemon 
                    rwok = randWokemon[0] # extract just the name 
                    fight1 = input_slow("\nA wild " + rwok + " appears!!\n Do you battle? or Run away?\n Enter 'Battle', or n'Run\n").lower()
                    if fight1 == "run":
                        print_slow("You got away just in time! Better head back to that fork in the path.\n\n")
                        time.sleep(2)
                        continue 
                    elif fight1 == "battle":
                        battle(randWokemon)
                    else: 
                        print_slow("Choose battle, or Run.\n")
                else:
                    print_slow("Please choose left or right\n")
                    continue
                

def l2():#game level 2
    print_slow("Welcome to Level 2!\n\n")
    print_slow("You have entered a new area now...\n")
    time.sleep(.25)
    print_slow("You see new kinds of terrain ready to explore!\n")
    time.sleep(.25)
    while True:
        print_slow("To your left you see a massive volcano, and to your right you see a vast rocky desert.\n")
        time.sleep(.15)
        path3 = input_slow("Do you visit the desert or the volcano?\nsay 'Desert', or 'Volcano'\n").lower()
        if path3 == "desert":
            print_slow("You begin to wander the desert.\nThe Sun is beating down on you\n")
            time.sleep(.5)
            print_slow("You see something in the distance....\n")
            time.sleep(.5)
            print_slow("You walk closer......\n")
            time.sleep(.75)
            randWokemon = random.choice(list(earthWokemon.items())) #chose random Wokemon from dict of wokemon 
            rwok = randWokemon[0] # extract just the name 
            while True:
                fight1 = input_slow("\nA wild " + rwok + " appears!!\n Do you battle? or Run away?\n Enter 'Battle', or n'Run\n").lower()
                if fight1 == "run":
                    print_slow("You got away just in time! Better head back.\n\n")
                    time.sleep(2)
                    continue 
                elif fight1 == "battle":
                    battle(randWokemon)
                else: 
                    print_slow("Choose battle, or Run.\n")
        elif path3 == "volcano":
            print_slow("You start walking towards the volcano.\n")
            time.sleep(.75)
            print_slow("Suddenly a creature rushes twords you!")
            randWokemon = random.choice(list(fireWokemon.items())) #chose random Wokemon from dict of wokemon 
            rwok = randWokemon[0] # extract just the name 
            while True:
                fight1 = input_slow("\nA wild " + rwok + " appears!!\n Do you battle? or Run away?\n Enter 'Battle', or n'Run\n").lower()
                if fight1 == "run":
                    print_slow("You got away just in time! Better head back.\n\n")
                    time.sleep(2)
                    continue 
                elif fight1 == "battle":
                    battle(randWokemon)
                else: 
                    print_slow("Choose battle, or Run.\n")
        else:
            print_slow("Please choose desert, or volcano.\n")
            continue
def l3(): #Game level 3
    print("Level 3 Comming Soon!")
    time.sleep(3)
    pass
levels = {1:l1,2:l2,3:l3}

def loby():# lobby is where the player once logged in, can either view thier Wokedex, or continue playing at the start of thier current  level 
    global wokeDex
    global currentLevel
    lvl = open("saveG.txt","r")
    currentLevel = int(lvl.read())
    while True:
        lchoice = input("Hello "+auth_usr+" Welcome to the lobby!\n Your Currently at Level: " + str(currentLevel) + "\nSay 'start' to resume your game, 'view' to view your wokedex, 'Prev' to redo a previos level, or 'Exit' to retun to the main screen."+"\n").lower()
        if lchoice == "start":
            level = open("saveG.txt","r").read()# save game file
            level = int(level)
            levels[level]()# read savegame file and call level finciton based on the text in the file. this text is used as a key in a dictionary of all levels where the values are the fucntions that start the levels 
        elif lchoice == "prev":
            if currentLevel == 1:
                print_slow("\nYou have not completed any levels yet!. Come back here after you have progressed.\n")
                time.sleep(1)
                continue
            elif currentLevel == 2:
                try:
                    lev = int(input("You can Visit the Following Levels:\nLevel 1, Level 2\nType the number of the level you want to visit\n"))
                    if lev > currentLevel:
                        print("You can not access this yet.")
                    else:
                        levels[lev]()
                except ValueError:
                    print("Level does not exist.\n")
                    continue
            elif currentLevel == 3:
                try:
                    lev = int(input("You can Visit the Following Levels:\nLevel 1, Level 2, Level 3\nType the number of the level you want to visit\n"))
                    if lev > currentLevel:
                        print("You can not access this yet.\n\n")
                    else:
                        levels[lev]()
                except ValueError:
                    print("Level does not exist.\n")
                    continue
            
        elif lchoice == "view":
            print("\n"+str(wokeDex)+"\n")
            time.sleep(1)
        elif lchoice == "exit":#exit loby and return to welocme/ main directory
            os.chdir(owd)
            wokeDex = {}
            currentLevel = 0
            welcome()
        else:
            print("Select a valid choice\n")
            time.sleep(.5)

def mkuser(): # if the user does not have an account they can make one
    breaker = True
    while breaker ==True:
        print_slow("Prof. Woke: Wecome to WokeyWorld!")
        pname = input("What shall I call you?\n")   
        if pname in savedGames or os.path.exists(pname+"/"):
            print("User already exists. Try again ")
            continue
        else:
            global auth_usr
            global wokeDex
            auth_usr = pname
            savedGames.append(pname) # ad new name to the saved games list 
            auth = open("accounts.txt","r+") 
            auth.write("\n".join(str(line) for line in savedGames))# write easch line of the saved gmaes list  to the accouts file
            auth.close()
            p = Path(pname)
            os.chdir("savedGames") # changes dir to the users folder so that a new game can be saved
            p.mkdir() # make play direcotry 
            os.chdir(pname) # enter player direcotry 
            global save
            global wokeDex
            sav = open("saveG.txt", "x") # create save file
            wd = open("wokedex.txt", "x") # create save file
            os.chdir(owd)
            print("Account creation sucessfull. Logged in as:", pname,"\n")
            breaker == False 
            newGame()
            break
def saveg():## this fuction can be called to save the game durring play by typing save 
    os.chdir("savedGames/" + auth_usr)
    dex = open("wokedex.txt","w")
    for key, value in wokeDex.items():
        dex.write('%s %s\n' % (key, value))
    lvl = open("saveG.txt","w")
    lvl.write(str(currentLevel))
def savel():## this fuction can be called to save the game durring play by typing save 
    dex = open("wokedex.txt","w")
    for key, value in wokeDex.items():
        dex.write('%s %s\n' % (key, value))
    dex.close()
    lvl = open("saveG.txt","w")
    lvl.write(str(currentLevel))
    lvl.close()
    print("Game Saved. Your currnet level: "+str(currentLevel))
            
def newGame():# First Sequence in game after user amkes account
    time.sleep(.25)
    print_slow("\nProf Woke: Hello "+auth_usr+" My Name is Professor Woke! Ill show you arround\n")
    time.sleep(.1)
    print_slow("Prof Woke: Im giving you a wokedex.\n")
    time.sleep(.1)
    print_slow("Prof Woke: This is where you will store the wokemon you catch along the way.\n")
    time.sleep(.1)
    print_slow("Prof Woke: I going to start you off with this Wikachu.\n")
    wokeDex["Wikachu"] = 11
    print("\n",auth_usr,"'s Wokedex:",wokeDex,"\n")
    time.sleep(1)
    global currentLevel
    currentLevel = 1
    saveg()
    loby()
    pass

def welcome():# where user logs in to contine or creates new game
    while True:
        print("\n\nWokemon Gotta Snatch em' all!")
        game = input("To start a new game, say 'New', to continue a game, enter 'cont'\n").lower()
        if game == "new":
            mkuser()
        elif game == "cont":
            while True:
                print("Available saved Games:",savedGames,"\n")
                un = input("Enter your username or type 'Exit to return to main menue\n")
                if un == "exit":
                    welcome()
                    break
                elif un not in savedGames:
                    print("\n User not found. Try agian. OR Type Exit to return to the main screen \n")
                    time.sleep(1)
                elif un in savedGames: #checks username agains list of saved games
                    global auth_usr
                    auth_usr = un
                    global wokeDex
                    os.chdir("savedGames/")
                    os.chdir(auth_usr)
                    with open("wokedex.txt", "r+") as wd:
                        for line in wd:
                            (wok,pow) = line.split()# Create tuple of wokemon/powerlevels
                            wokeDex[(wok)] = pow #break the tuple in to doctiuonary key,value
                
                    print("\n Found Your Game!\n")
                    
                    print(" Lets Get to it ", auth_usr,"\n")
                    loby()
                    break
        else: print("Please select a valid choice")
welcome()            
