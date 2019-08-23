from Chem_Equation_Balancer import *
from EmpiricalFormulas import *
from Number_Validation import *
def Chapter4_Menu(): #Submenu for Chaper 4
    print ("\nChapter 4 Menu:\n")
    while True:
        print ("Enter 0 to find total mass of a compound")
        print ("Enter 1 to test whether an equation is balanced")
        print ("Enter 2 to get the percent of a compund by mass")
        print ("Enter 3 to get the Emperical formula by mass % of each element")
        print ("Enter 4 to return to the main Menu")

        inp = input('\n')

        while inp not in ["1", "2", "3", "0", "4"]:
            inp = input("Enter either 0, 1, 2, 3, or 4 please! ")
            


        
        if inp == '0':
            Total_Mass_Menu()
        if inp == '1':
            Balanced_Check_Menu()
        if inp == '2':
            Perc_Mass_Menu()
        if inp == '3':
            GetEP_Menu()
        if inp == '4':
            return ()

    
        print ("\n")


def Total_Mass_Menu(): # Finds the total mass per mol of a substance
    equation = input("Please input a chemical compund (Letters that are not chemicals will be equal to 0) ")

    try:
        print ("One mol of", equation,'is',get_total_mass(equation), "g")
    except:
        print ("This is not a valid compound")
        Total_Mass_Menu()
    



def Balanced_Check_Menu(): # Checks to see if a chemical equation is balanced
    #Example of balanced equation- NO2 + H2O -> HNO3
    equation = input("Please input a chemical equation ")

    try: # Equations without 2 sides will result in a failure
        if is_balanced_equ(equation):
            print ("The equation is balanced")
        else:
            print ("The equation is not balanced")
    except ValueError: # Catches this Error
        print ("You must have exactly 1 recactant and exactly 1 product")

def Perc_Mass_Menu(): # Gets each elements mass percentage in the compound 
    equation = input("Please input a chemical compund to calculate the percent of each element by mass ")

    try: # Any non-elements put into the equation will result in failure
        GetPercByMass(equation)
    except:
        print ("This is not a valid compound")
        Perc_Mass_Menu() 

def GetEP_Menu(): # Inverse of the previous function  
    rem_perc = 100
    total_input = []
    while rem_perc >1: # Needs sum of percents to total 99 - 101
        ele = input("Input an element ")
        perc = input("What percent "+ele+" by mass is the compund? ").replace("%", "")
        if perc == "a" or perc == "all":
            perc = str(rem_perc)
        while valid_num(perc, domain = "(0, "+str(rem_perc)+"]") == False:
            print ("You must input a number greater than 0 and less than or equal to "+ str(rem_perc) + " because you cannot have more than 100% total")
            if perc == "a" or perc == "all":
                perc = rem_perc
            perc = input("What percent "+ele+" by mass is the compund? ").replace("%", "")
        total_input.append([ele, float(perc)])
        rem_perc -= float(perc)
    try:
        print ("The emperical formula of this compound is "+GetEP(total_input))
    except:
        print ("One or more of the inputted elements were not actual elements")
        
    
