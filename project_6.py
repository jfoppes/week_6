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
import turtle 
import time
import tkinter
import random     
import os  
from pathlib import Path
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
            
wokemon = {"wikachu":5,"worzard":5,"wonix":10,"wortle":5,"Wewtwo":20,"wurtterfree":3,"wattata":4}# dictionary of pokemon with health points 



def l1():
    print("Welcome to level 1!")
    pass
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
        if pname in savedGames:
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
            currentLevel = "l1"
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
        
def newGame():
    time.sleep(.25)
    print("\nProf Woke: Hello ",auth_usr," My Name is Professor Woke! Ill show you arround")
    time.sleep(1)
    print("Prof Woke: Im giving you a wokedex.")
    time.sleep(1)
    print("Prof Woke: This is where you will sore the wokemon you create along the way.")
    time.sleep(1)
    print("Prof Woke: I going to start you off with this wikachu.")
    wokeDex["wikachu"] = 5
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


        

'''Level 1: '''


'''Level 2: '''
