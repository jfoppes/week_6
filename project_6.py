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
currentLevel = ""

with open("accounts.txt","r+") as users:
    games = users.read()
    savedGames = games.split("\n")
print(savedGames)
            
wokemon = {"Wikachu":10,"Worzard":5,"Wonix":10,"Wortle":5,"Wewtwo":20,"Wurtterfree":3,"Wattata":4}# dictionary of pokemon with health points 
waterWokemon = {"Wyaradose":21, "Wlastoise":8, "Wampert": 10, "Wagicarp":4}
fireWokemon = {}
def print_slow(str):# Credit : Sebastian - Stack overflow https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.0005)
def input_slow(str): # Credit: https://www.101computing.net/python-typing-text-effect/
  for character in str:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.0005)
  value = input()  
  return value  
def battle(randWokemon):# take 
    rwok = randWokemon[0] # extract just the name 
    rwokhealth = randWokemon[1] #extract the health 
    wok = input_slow("\nChoose your Wokemon:\n"+str(wokeDex)+"\n")
    if wok in wokeDex:
        global cwokhealth
        global pwokhealth
        pwokhealth = int(wokeDex[wok])
        print_slow("\nYour HP: " + str(pwokhealth) + "\n") #print player helath 
        cwokhealth = int(rwokhealth)
        print_slow("Oponent HP: " + str(cwokhealth) + "\n")# print oponent helath 
        print_slow("\nLooks like its " + wok + " vs " + rwok + "\n")
        def attack():
            global cwokhealth
            global pwokhealth
            phit1 = random.randrange(0,5,1)#randomly genreated player dammage to compouter 
            cwokhealth -= phit1 #subtract hit points form health 
            print_slow(wok + " Strikes!\nIt does " + str(phit1) + " dammage!\n\n")
            chit1 = random.randrange(0,5,1)#randomly genereated compouter dammage to play
            pwokhealth -= chit1#subtract hit points form health 
            print_slow(rwok + " Strikes!\nIt does " + str(chit1) + " dammage!\n\n")
            print_slow("Oponent HP: " + str(cwokhealth) + "\n")
            print_slow("Your HP: " + str(pwokhealth) + "\n")
        attack()
        while pwokhealth > 0 and cwokhealth > 0:
            attack()
        if pwokhealth <= 0 and cwokhealth >= 0: #if comoputer wins
            print_slow("Dang..., Thats tough boss. \nLooks like you lost this one.\nTime to head home and heal your wokemon\n ")
            loby()
        elif pwokhealth >= 0 and cwokhealth <= 0: # if player wins
            print_slow("You won!!\n you now have " + rwok + " added to your wokedex!!\nYou will now move on to level 2!\n\n")
            wokeDex[rwok] = rwokhealth
            global currentLevel
            currentLevel = "l2"
            savel()
            loby()
        
def l1():
    sav = open("saveG.txt", "r+") # open save file
    wd = open("wokedex.txt", "r+") # create save file
    global wokemon
    print_slow("Welcome to level 1!\n")
    path1 = input_slow("You are wlaking down the street and you encounter a set a of 2 trail heads:\n 'Elk Road', and 'Spoon Drive' which do you take \n Enter 'Elk' or 'Spoon'\n").lower()
    while True:
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
            rwokhealth = randWokemon[1] #extract the health 
            fight1 = input_slow("A wild " + rwok + " appears!!\n Do you battle? or Run away?\n Enter 'Battle', or n'Run\n").lower()
            if fight1 == "run":
                print_slow("You got away just in time")
                continue 
            elif fight1 == "battle":
                wok = input_slow("\nChoose your Wokemon:\n"+str(wokeDex)+"\n")
                if wok in wokeDex:
                    global cwokhealth
                    global pwokhealth
                    pwokhealth = int(wokeDex[wok])
                    print_slow("\nYour HP: " + str(pwokhealth) + "\n") #print player helath 
                    cwokhealth = int(rwokhealth)
                    print_slow("Oponent HP: " + str(cwokhealth) + "\n")# print oponent helath 
                    print_slow("\nLooks like its " + wok + " vs " + rwok + "\n")
                    def attack():
                        global cwokhealth
                        global pwokhealth
                        phit1 = random.randrange(0,5,1)#randomly genreated player dammage to compouter 
                        cwokhealth -= phit1 #subtract hit points form health 
                        print_slow(wok + " Strikes!\nIt does " + str(phit1) + " dammage!\n\n")
                        chit1 = random.randrange(0,5,1)#randomly genereated compouter dammage to play
                        pwokhealth -= chit1#subtract hit points form health 
                        print_slow(rwok + " Strikes!\nIt does " + str(chit1) + " dammage!\n\n")
                        print_slow("Oponent HP: " + str(cwokhealth) + "\n")
                        print_slow("Your HP: " + str(pwokhealth) + "\n")
                    attack()
                    while pwokhealth > 0 and cwokhealth > 0:
                        attack()
                    if pwokhealth <= 0 and cwokhealth >= 0: #if comoputer wins
                        print_slow("Dang..., Thats tough boss. \nLooks like you lost this one.\nTime to head home and heal your wokemon\n ")
                    elif pwokhealth >= 0 and cwokhealth <= 0: # if player wins
                        print_slow("You won!!\n you now have " + rwok + " added to your wokedex!!\nYou will now move on to level 2!\n\n")
                        wokeDex[rwok] = rwokhealth
                        global currentLevel
                        currentLevel = "l2"
                        savel()
                        loby()
                    break
                else: 
                    print_slow('Choose an availble Wokemon')
                    continue
                    
        elif path1 == "spoon":
            print_slow("\nYour walking down the Spoon Path and you come to a fork in the path\n The left looks like it leads to a river, and the right looks to be more forrest.\n ")
            lefRig = input_slow("Do you Turn left or right\n").lower()
            if lefRig == "left":
                print_slow("\nWhile Crossing the shallow end of the river, you see some splashing...")
                time.sleep(.75)
                print_slow(".")
                time.sleep(.75)
                print_slow(".")
                randWokemon = random.choice(list(waterWokemon.items())) #chose random Wokemon from dict of wokemon
                rwok = randWokemon[0] # extract just the name 
                fight2 = input_slow("\n\nA wild " + rwok + " appears!!\n Do you battle? or Run away?\n Enter 'Battle', or n'Run\n").lower()
                if fight2 == "battle":
                    battle(randWokemon)
                elif fight2 == "run":
                    print_slow("You got away just in time")
                else:
                    print_slow("Choose battle, or Run.")
            elif lefRig == "right":
                continue
            else:
                print_slow("Please choose left or right")
                continue
                

def l2():
    print("Welcome to Level 2!")
    pass
def l3():
    print("Welcome to Level 3!")
    pass
levels = {"l1":l1,"l2":l2,"l3":l3}

def loby(): # lobby is where the player once logged in, can either view thier Wokedex, or continue playing at the start of thier current  level 
    sav = open("saveG.txt", "r+") # open save file
    wd = open("wokedex.txt", "r+") # create save file
    while True:
        lchoice = input("Hello "+auth_usr+" Welcome to the lobby! Say 'start' to resume your game, 'view' to view your wokedex."+"\n").lower()
        if lchoice == "start":
            level = open("saveG.txt","r").read()# save game file
            levels[level]()# read savegame file and call level finciton based on the text in the file. this text is used as a key in a dictionary of all levels where the values are the fucntions that start the levels 
        elif lchoice == "view":
            print("\n"+str(wokeDex)+"\n")
            time.sleep(.5)
        elif lchoice == "exit":#exit loby and return to welocme/ main directory 
            os.chdir(owd) 
            welcome()
        else:
            print("Select a valid choice")

def mkuser(): # if the user does not have an account they can make one
    breaker = True
    while breaker ==True:
        print("Prof. Woke: Wecome to WokeyWorld!")
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
    lvl.write(currentLevel)
def savel():## this fuction can be called to save the game durring play by typing save 
    dex = open("wokedex.txt","w")
    for key, value in wokeDex.items():
        dex.write('%s %s\n' % (key, value))
    lvl = open("saveG.txt","w")
    lvl.write(currentLevel)
        
def newGame():
    time.sleep(.25)
    print("\nProf Woke: Hello ",auth_usr," My Name is Professor Woke! Ill show you arround")
    time.sleep(1)
    print("Prof Woke: Im giving you a wokedex.")
    time.sleep(1)
    print("Prof Woke: This is where you will sore the wokemon you create along the way.")
    time.sleep(1)
    print("Prof Woke: I going to start you off with this wikachu.")
    wokeDex["wikachu"] = 10
    print("\n",auth_usr,"'s Wokedex:",wokeDex,"\n")
    time.sleep(1)
    global currentLevel
    currentLevel = "l1"
    saveg()
    loby()
    pass

def welcome():
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
