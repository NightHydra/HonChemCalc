from Number_Validation import *
from Gas_Laws import *




class equation_variables: # Sets up the variables needed for each equation
    Boyles = ["P", "V"]
    Charles = ["V", "T"]
    Avogadros = ["V", "N"]
    Combined = ["P", "V", "T"]
    Ideal = ["P", "V","N", "T"]

    req_vars = {"Boyles":["P1", "V1"], "Charles":["V1", "T1"], "Avogadros":\
                  ["V1", "n1"], "Combined Gas":["P1", "V1", "T1"], "Ideal Gas": []}
    solvable_vars = {"Boyles":["P2", "V2"], "Charles":["V2", "T2"], "Avogadros":\
                  ["V2", "n2"], "Combined Gas":["P2", "V2", "T2"], "Ideal Gas": ["P", "V", "n", "T"]}


    
    laws_vars = [Boyles, Charles, Avogadros, Combined, Ideal]
    law_names = ['Boyles', 'Charles', 'Avogadros', 'Combined Gas', 'Ideal Gas']

    law_inst = [Boyles_Law, Charles_Law, Avogadros_Law, \
                Combined_Gas_Law, Ideal_Gas_Law] # Puts instances of the law classes into a list
    

    
def get_law(): # Asks the user what law they would like to use
    law = input("What Law would you like to use")
    

def Gas_Menu(): # Semi-Main menu    

    print ("What would you like to solve for? ")
    print ("Enter P for pressure") # Needs to be inputted in atm
    print ("Enter V for volume") # Needs to be inputted in liters
    print ("Enter n for number of moles") 
    print ("Enter T for temperature") # Needs to be inputted in Kelvin (Celcius + 273)
    print ("Enter 0 to return to main menu")

    var = input("\n")

    while var.lower() not in "pvnt, 0":
        print ("You must enter P, V, n, T, or 0")
        var = input("What would you like to solve for? ")
    if var == '0':
        return ()
    possible_equ = [] # List of all equations the user can use
    for i in range (5): # Loop actually puts it into a list
        if var.upper() in equation_variables.laws_vars[i]:
            print ("Enter "+str(len(possible_equ))+" to use "+equation_variables.law_names[i]+" Law?")
            possible_equ.append(i)
    print ()
    print_equ(possible_equ)

    
    variables = []

    law = input("\nInput the number of the law you would like to use? ") # Asks user what law they want to sue


    while law not in list(map(str, range(len(possible_equ)))): # Input validation
        print ("You need to input a number from 0 to "+str(len(possible_equ)-1))
        law = input("\nInput the number of the law you would like to use? ")
    
    law = possible_equ[int(law)] # Gets the law the user wants to use

    for i in equation_variables.req_vars[equation_variables.law_names[law]]: # Gets a value for every required variable
        variables.append(get_var("Enter a value for "+i+" "))
    
    for i in equation_variables.solvable_vars[equation_variables.law_names[law]]: # Gets a value for every variable that could be unknown but is not
        if var.lower() != i[0].lower():
            variables.append(get_var("Enter a value for "+i+" "))
    # Solves for the unknown
    if var.lower() == "v":
        print ("The volume is",equation_variables.law_inst[law].get_Volume(*variables),"Liters.")
    if var.lower() == "p":
        print ("The pressure is",equation_variables.law_inst[law].get_Pressure(*variables),"atm.")
    if var.lower() == "n":
        print ("You have",equation_variables.law_inst[law].get_moles(*variables),"moles of gas.")
    if var.lower() == "t":
        print ("The temperature is",equation_variables.law_inst[law].get_Temperature(*variables),"K")
    Gas_Menu()
    
def get_var(message): # Simple validation function (Makes sure all input for numbers can become a float and that they are positive")
    val = input(message)
    while valid_num(val, domain = "(0, inf)") == False:
        print ("You need to input a positive number")
        val = input(message)
    return float(val)

def print_equ(nums): # Prints all the equations the person can use
    if 0 in nums:
        print ("Boyles Law - P1*V1 = P2*V2")
    if 1 in nums:
        print ("Charles Law - V1/T1 = V2/T2")
    if 2 in nums:
        print ("Avogadros Law - V1/n1 = V2/n2")
    if 3 in nums:
        print ("Combined Gas Law - P1*V1/T1 = P2*V2/T2")
    if 4 in nums:
        print ("Ideal Gas Law - PV = nRT (R = rate constant = 0.0821 atm-L/mol-K)")
    print () # Spacing
    






