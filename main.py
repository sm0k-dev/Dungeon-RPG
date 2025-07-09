import os, msvcrt
from functions import *

while True:
    #Screen
    os.system('cls')
    print(screen)
    option = input("Option: ")
    os.system('cls')
    #Screen

    #Player_Options
    if option == '1':   #Attack
        pass
    elif option == '2': #Block
        pass
    elif option == '4': #Flee
        pass
    else:               #Invalid_Option
        pass
    #Player_Options

    #Enemy_Consequence
    #Insert here enemy logic
    msvcrt.getch()
    #Enemy_Consequence