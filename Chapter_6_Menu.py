from Thermochemistry import *
from Number_Validation import *
def Thermo_Menu(): # Main menu for chapter 6
    print ("\nChapter 6 Menu:\n")
    print ("Rules:\n")
    print ("Please input all mass in grams")
    print ("Please input all temperature in Celcius")
    print ("Please input all specific heat values in cal/gC\n")

    while True:
        print ("Enter 0 to just calculate energy lost/gained")
        print ("Enter 1 to solve equations without a calorimeter")
        print ("Enter 2 to solve equations using a calorimeter")
        print ("Enter 3 to return to the main menu")
        

        option = input()

        while option not in ['0', '1', '2', '3']:
            option = input("You must enter either 0, 1 , or 2 ")

        if option == '0':
            Enthalpy_Menu()
        if option == '1':
            No_Calorimeter_Equation_Menu()
        if option == '2':
            Calorimeter_Equation_Menu()
        if option == '3':
            return ()

def Enthalpy_Menu(): # Finds heat lost or gained
    variables = []
    mass = get_others("What is the mass of the object? (enter u is this is your unknown) ")
    heat = get_temp("What is the intital temperature of the object? (this cannot be an unknown) ", accepts_u = False)
    sph = get_others("What is the specific heat value of the object? (enter u is this is your unknown) ")
    cal = get_others("How many calories did the object lose/gain? (enter u is this is your unknown) ")
    fin_H = get_temp("What is the final temperature of the object? (this cannot be an unknown) ", accepts_u = False)

    variables = [mass, heat, sph, cal, fin_H]

    while (variables.count("u")+variables.count("unknown")) != 1: #Input Validation
        print ("You need to have exactly one unknown!")
        mass = get_others("What is the mass of the object? (enter u is this is your unknown) ")
        heat = get_temp("What is the intital temperature of the object? (this cannot be an unknown) ", accepts_u = False)
        sph = get_others("What is the specific heat value of the object? (enter u is this is your unknown) ")
        cal = get_others("How many calories did the object lose or gain? (enter u is this is your unknown) ")
        fin_H = get_temp("What is the final temperature of the object? (this cannot be an unknown) ", accepts_u = False)

        variables = [mass, heat, sph, cal, fin_H]

    if "u" in variables:
        variables.remove("u")
    if "unknown" in variables:
        variables.remove("unknown")

    u = ["u", "unknown"]

    #Gets the answer
    if mass in u:
        print ("The mass of the object is",Enthalpy.Get_Mass(*variables),"g") 
    elif sph in u:
        print ("The SPH of the object is",Enthalpy.Get_SPH(*variables),"cal/gC")
    elif cal in u:
        print ("The object gained or lost",Enthalpy.Get_Total_Enthalpy(*variables), "cal")




def No_Calorimeter_Equation_Menu(): # Solves equations that do not use a calorimeter

    # Very similar in code to the last one except more variables

    mass_obj = get_others("What is the mass of the object? (enter u is this is your unknown) ")
    heat_obj = get_temp("What is the intital temperature of the object? (enter u is this is your unknown) ")
    sph_obj = get_others("What is the specific heat value of the object? (enter u is this is your unknown) ")

    mass_l = get_others("What is the mass of the liquid? (enter u is this is your unknown) ")
    heat_l = get_temp("What is the intital temperature of the liquid? (enter u is this is your unknown) ")
    sph_l = get_others("What is the specific heat value of the liquid? (enter u is this is your unknown) ")
        
    fin_H = get_temp("What is the final temperature of everything? (enter u is this is your unknown) ")

    variables = [mass_obj, mass_l, heat_obj, heat_l, sph_obj, sph_l,  fin_H]

    gain_loss = False

    if fin_H != "u" and heat_obj != "u" and heat_l != "u":
        gain_loss = (fin_H < heat_obj == fin_H < heat_l)


    
    while (variables.count("u")+variables.count("unknown")) != 1 or (gain_loss): # One unknown is required and one side must gain heat while the other side loses it
        if gain_loss == True:
            print ("One part must gain heat and the other must lose heat")
        else:
            print ("You must have exactly one unknown in your equation")
        mass_obj = get_others("What is the mass of the object? (enter u is this is your unknown) ")
        heat_obj = get_temp("What is the intital temperature of the object? (enter u is this is your unknown) ")
        sph_obj = get_others("What is the specific heat value of the object? (enter u is this is your unknown) ")

        mass_l = get_others("What is the mass of the liquid? (enter u is this is your unknown) ")
        heat_l = get_temp("What is the intital temperature of the liquid? (enter u is this is your unknown) ")
        sph_l = get_others("What is the specific heat value of the liquid? (enter u is this is your unknown) ")
        
        fin_H = get_temp("What is the final temperature of everything? (enter u is this is your unknown) ")

        variables = [mass_obj, mass_l, heat_obj, heat_l, sph_obj, sph_l,  fin_H]


        if fin_H != "u" and heat_obj != "u" and heat_l != "u":
            gain_loss = (fin_H < heat_obj == fin_H < heat_l)

    u = ["u", "unknown"]

    unknown_type = ""
    
    for i in variables[0:5:2]:
        if i in u:
            unknown_type = "object"
            variables = [mass_l, mass_obj, heat_l, heat_obj, sph_l, sph_obj, fin_H] # Flips around variables if the unknown is about the object
    if unknown_type == "":
        for i in variables[1:2]:
            if i in u:
                unknown_type = "liquid"
    
    if "u" in variables:
        variables.remove("u")
    if "unknown" in variables:
        variables.remove("unknown")
    
    if mass_obj in u or mass_l in u:
        print ("The mass of the",unknown_type,"is",No_Calorimeter_Equations.get_mass(*variables), "g")
    elif sph_obj in u or sph_l in u:
        print ("The SPH of the", unknown_type, "is",No_Calorimeter_Equations.get_SPH(*variables), "cal/gC")
    elif heat_obj in u or heat_l in u:
        print ("The initial heat of the", unknown_type, "is",No_Calorimeter_Equations.get_init_heat(*variables), "C")
    elif fin_H in u:
        print ("The final heat of everything is",No_Calorimeter_Equations.get_final_heat(*variables), "C")
        


def Calorimeter_Equation_Menu(): # Finds Equations using a calorimeter
    # Calorimeter - What the liquid and object are in.  It absorbs heat as well.
    
    mass_obj = get_others("What is the mass of the object? (enter u is this is your unknown) ")
    heat_obj = get_temp("What is the intital temperature of the object? (enter u is this is your unknown) ")
    sph_obj = get_others("What is the specific heat value of the object? (enter u is this is your unknown) ")

    mass_l = get_others("What is the mass of the liquid? (enter u is this is your unknown) ")
    heat_liqCal = get_temp("What is the intital temperature of the liquid and calorimeter? (enter u is this is your unknown) ") # Calorimeter and Liquid are same temp
    sph_l = get_others("What is the specific heat value of the liquid? (enter u is this is your unknown) ")

    mass_calor = get_others("What is the mass of the calorimeter (enter u is this is your unknown) ")
    sph_calor = get_others("What is the SPH of the calorimeter (enter u is this is your unknown) ")

    
    fin_H = get_temp("What is the final temperature of everything? (enter u is this is your unknown) ")

    variables = [mass_obj, sph_obj, heat_obj, mass_l, sph_l, heat_liqCal, mass_calor, sph_calor, fin_H]

    gain_loss = False

    if fin_H != "u" and heat_obj != "u" and heat_liqCal != "u":
        gain_loss = fin_H < heat_obj == fin_H < liqCal
    
    while (variables.count("u")+variables.count("unknown")) != 1 or (gain_loss):
        
        if gain_loss == True:
            print ("One side of the equation must gain heat and the other must lose heat")
        else:
            print ("You must have exactly 1 unknown")
        mass_obj = get_others("What is the mass of the object? (enter u is this is your unknown) ")
        heat_obj = get_temp("What is the intital temperature of the object? (enter u is this is your unknown) ")
        sph_obj = get_others("What is the specific heat value of the object? (enter u is this is your unknown) ")

        mass_l = get_others("What is the mass of the liquid? (enter u is this is your unknown) ")
        heat_liqCal = get_temp("What is the intital temperature of the liquid and calorimeter? (enter u is this is your unknown) ") 
        sph_l = get_others("What is the specific heat value of the liquid? (enter u is this is your unknown) ")

        mass_calor = get_others("What is the mass of the calorimeter (enter u is this is your unknown) ")
        sph_calor = get_others("What is the SPH of the calorimeter (enter u is this is your unknown) ")

    
        fin_H = get_temp("What is the final temperature of everything? (enter u is this is your unknown) ")

        variables = [mass_obj, sph_obj, heat_obj, mass_l, sph_l, heat_liqCal, mass_calor, sph_calor, fin_H]

        if fin_H != "u" and heat_obj != "u" and heat_liqCal != "u":
            gain_loss = fin_H < heat_obj == fin_H < liqCal


    u = ["u", "unknown"]

    unknown_type = ""
    

    for i in variables[3:5]:
        if i in u:
            unknown_type == "liquid"
    for i in variables[6:]:
        if i in u:
            unknown_type == "calorimeter"
    
    if "u" in variables:
        variables.remove("u")
    if "unknown" in variables:
        variables.remove("unknown")

    
    
    if mass_obj in u:
        print ("The mass of the object is",Calorimeter_Equations.get_Mass_Obj(*variables), "g")
    elif sph_obj in u:
        print ("The SPH of the object is",Calorimeter_Equations.get_SPH_Obj(*variables), "cal/gC")
    elif heat_obj in u:
        print ("The initial heat of the object is",Calorimeter_Equations.get_Heat_Obj(*variables), "C")

    elif mass_l in u or mass_calor in u:
        print ("The mass of the", unknown_type, "is",Calorimeter_Equations.get_Mass_Liquid(*variables),"g")
    elif sph_l in u or sph_calor in u:
        print ("The SPH of the", unknown_type, "is", Calorimeter_Equations.get_SPH_Liquid(*variables),"g")

    elif heat_liqCal in i:
        print ("The initial heat of the liquid and calorimeter is", Calorimeter_Equations.get_Heat_LiqCal(*variables))


    elif fin_H in u:
        print ("The final heat of everything is",Calorimeter_Equations.get_final_heat(*variables), "C")





def get_temp(message, accepts_u = True): # Function that gets the input for a temperature, will sometimes not accept u (Can be positive)
    temp = input(message)
    while valid_num(temp, domain = "(-inf, inf)") == False:
        if accepts_u == True and temp in ["u", "unknown"]:
            break
        print ("You need to input a number")
        temp = input(message)
    if temp not in ["u", "unknown"]:
        temp = float(temp)
    return temp

def get_others(message): # Makes sure input is posivie
    val = input(message)
    while valid_num(val, domain = "(0, inf)") == False and val not in ["u", "unknown"]:
        print ("You need to input a positive number")
        val = input(message)
    if val not in ["u", "unknown"]:
        val = float(val)
    return val
