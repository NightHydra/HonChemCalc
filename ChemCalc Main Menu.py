from Chapter_1_4_Menu import *
from Gas_Laws_Menu import Gas_Menu
from Chapter_6_Menu import Thermo_Menu
from Chapter_7_Menu import Chapter_7_Menu
import sys


def main(): #Runs entire program
    print ("Hello, Welcome to ChemCalc, a program to help solve problems throughout Chemistry Honors")
    print ("Warning: It is reccomended that you run the program in full screen")
    print ("For scientific notation: 4 * 10^7, should be inputted as 4e7")
    print ("Menu:\n")

    #Program runs some probelms from chapters 1-4, most from chapter 5, most from chapter 6, and some from chapter 7
    
    while True:
        print ("Enter 0 to solve problems between chapters 1-4 - Element mass problems")
        print ("Enter 1 to solve chapter 5 problems - Gas problems")
        print ("Enter 2 to solve chapter 6 problems - Thermochemistry")
        print ("Enter 3 to solve chapter 7 problems - Electron configurations and wavelengths")
        print ("Enter 4 to end the program")

        option = input("\n")

        while option not in ['0', '1', '2', '3', '4']:
            print ("You must enter either 0, 1, 2, 3, or 4")
            option = input()

        if option == "0":
            Chapter4_Menu() # Leads to a Submenu
        if option == "1":
            print ("\nChapter 5 Menu:\n") # Extra text is due not having a true submenu for Gas Laws
            print ("Rules\n")
            print ("Enter all pressure in atm")
            print ("Enter all volume in Liters")
            print ("Enter all Temperature in Kelvin\n")
            Gas_Menu() # Doesn't lead to menu like the rest
        if option == "2":
            Thermo_Menu() #Leads to a Submenu
        if option == "3":
            Chapter_7_Menu() # Leads to a Submenu
        if option == '4':
            print ("Bye!")
            exit()
            

                
        
    
    
main()
