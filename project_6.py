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
savedGames = [] 
auth_usr = ""
save = ""
owd = os.getcwd()

auth = open("accounts.txt",).read().splitlines()
for line in auth:
    savedGames.append(line)

def mkuser(): # if the user does not have an account they can make one
    global breaker 
    breaker = True
    while breaker == True:
        print("Prof. Woke: Wecome to WokeyWorld!")
        pname = input("What shall I call you?\n")   
        if pname in savedGames:
            print("User already exists. Try again ")
            continue
        else:
            auth_usr = pname
            savedGames.append(pname)
            auth = open("accounts.txt","a")
            auth.write('%s\n' % pname)
            #auth.write(pname)
            p = Path(pname)
            os.chdir("savedGames") # changes dir to the user foer so that a new game can be saved
            p.mkdir()
            os.chdir(pname)
            global save
            save = open("saveG.txt", "x") # create save file
            os.chdir(owd)
            print("Account creation sucessfull. Logged in as:", pname,"\n")
            print(savedGames) 
            print("auth usr",auth_usr)  
            
            breaker == False 
            newGame()
            break
        
def newGame():
    time.sleep(.25)
    print("Prof Woke: Hello ",auth_usr," My Name is Professor Woke! Ill show you arround")
    print("Prof Woke: Im giving you a wokedex ")
    pass

def welcome():
    print("\n\nWokemon Gotta Snatch em' all!")
    game = input("To start a new game, say 'New', to continue a game, enter 'cont'\n").lower()
    while True:
        if game == "new":
            mkuser()
        else:
            while True:
                print("Available saved Games:",savedGames,"\n")
                un = input("Enter your username or type 'Exit to return to main menue\n")
                print(un)
                print(savedGames)
                with open("accounts.txt") as users:
                    for line in users:
                        usr = line.split()
                        savedGames.append(usr)
                if un == "exit":
                    welcome()
                    break
                elif un not in savedGames:
                    print("\n User not found. Try agian. OR Type Exit to return to the main screen \n")
                    time.sleep(1)
                elif un in savedGames: #checks username agains list of saved games
                    global auth_usr
                    auth_usr = un
                    print("\n Found Your Game!\n")
                    print(" Lets Get to it ", auth_usr,"\n")
                    users.close() # close saved games file
                    break
        break
welcome()            
# dictionary of pokemon with health points 

wokemon = {"weekachu":5,"worzard":5,"wonix":10,"wortle":5,"Wewtwo":20,"wurtterfree":3,"wattata":4}
'''Level 1: '''


'''Level 2: '''
