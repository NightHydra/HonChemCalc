from Wave_Calc import *
from Number_Validation import *
from Electron_Calculations import Electron_Configurations
def Chapter_7_Menu(): # Main menu for chapter 7
    print ("\nChapter 7 Menu:\n")
    print ('Rules\n')
    print ("Energy needs be given in ergs")
    print ("Wavelength needs to be given in cm")
    print ("Frequency needs to be given in s^-1\n")
    while True:
        print ("Enter 0 to calculate wavelengths")
        print ("Enter 1 to find electron configurations")
        print ("Enter 2 to return to the main menu")


        inp = input("\n")

        while inp not in ["0", "1", "2"]:
            inp = input("Enter either 0 or 1 please! ")


        if inp == "0":
            Wavelength_Menu()
        if inp == "1":
            Electron_Menu()
        if inp == "2":
            return ()


def Wavelength_Menu(): # Calculates either wave energy, frequency, or wavelength
    variables = {"wave energy":0, "frequency":1, "wavelength":2} 
    print ("Would you like to convert from wave energy, frequency, or wavelength") #Finds what to convert from
    rem_parts= ["wave energy", "frequency", "wavelength"]

    for i in range(len(rem_parts)):
        print ("Enter "+str(i)+" for "+rem_parts[i])

    starting = input("\n")

    while starting not in ["0", "1", "2"]: #Input validation
        starting = input ("You need to enter either 0, 1, or 2 ")
    starting = rem_parts[int(starting)]
    rem_parts.remove(starting)
    starting = variables[starting]
    print ("Would you like to convert to "+" or ".join(rem_parts)) # Finds what to convert to

    for i in range(len(rem_parts)):
        print ("Enter "+str(i)+" for "+rem_parts[i]) # Makes a menu

    ending = input("\n")

    while ending not in ["0", "1"]:
        ending = input ("You need to enter either 0 or 1 ")
    ending = rem_parts[int(ending)]
    ending = variables[ending]
    # Running the proper equation

    # Starting with energy
    if starting == 0 and ending == 1:
        E = get_var("What is the wave's energy(in ergs)? ")
        print("The frequency is",energy_to_frequency(E),"s^-1")
    elif starting == 0 and ending == 2:
        E = get_var("What is the wave's energy(in ev)? ")
        print ("The wavelength is",energy_to_wavelength(E), "cm")

    #Starting with frequency
    elif starting == 1 and ending == 0:
        nu = get_var("What is the wave's frequency(in s^-1)? ")
        print ("The energy of the wave is",frequency_to_energy(nu), "ergs")
    elif starting == 1 and ending == 2:
        nu = get_var("What is the wave's frequency(in s^-1)? ")
        print ("The wavelength is",frequency_to_wavelength(nu), "cm")

    #Starting with wavelength
    elif starting == 2 and ending == 0:
        lambda_ = get_var("What is the wavelength(in cm)? ")
        print ("The energy of the wave is",wavelength_to_energy(lambda_), "ergs")
    elif starting == 2 and ending == 1:
        lambda_ = get_var("What is the wavelength(in cm)? ")
        print ("The frequency is",wavelength_to_frequency(lambda_), "s^-1")
    

def get_var(message): # Makes sure everything inputted in postive
    val = input(message)
    while valid_num(val, domain = "(0, inf)") == False:
        print ("You need to input a positive number")
        val = input(message)
    return float(val)



def Electron_Menu(): # Finds the electron configuration of atoms
    print ("Enter 0 to get the full electron configuration")
    print ("Enter 1 to get just the outer electron configuration")
    print ("Enter 2 to get the number of electrons in the outer energy level")

    inp = input("\n")

    while inp not in ["0", "1", "2"]:
        inp = input("Please enter either 0, 1, or 2 please ")

    ele = input("What element would you like to search for? ")
    try: #Function fails if an element is not inputted
        if inp == '0':
            print ("Complete Electron configuration: "+Electron_Configurations.get_config(ele))
        if inp == '1':
            print ("Outer Electron configuration: "+Electron_Configurations.get_outer(ele))
        if inp == '2':
            print ("Outer shell number:",Electron_Configurations.get_total_outer(ele))
    except: # Handles the exception
        print ("'"+ele+"' is not an element")
