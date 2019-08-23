def get_total_mass(equ): # Gets the total mass of a chemical compund
    Broken = get_true_equation(equ)
    mass = 0
    atoms_to_test = list(set(Broken))
    atoms_to_test.remove("")
    atom_count = []
    atom_weights = [0]*len(atoms_to_test)

    for i in atoms_to_test:
        atom_count.append(Broken.count(i))

    with open("Elements.txt", "r") as file:
        for i in file:
            if i.rstrip("\n") in atoms_to_test:
                atom_weights[atoms_to_test.index(i.rstrip("\n"))] = float(file.readline().rstrip("\n"))

    for i in range (len(atoms_to_test)):
        mass += atom_count[i] * atom_weights[i]
    return mass





def is_balanced_equ(equ): # Checks to see if an equation is balanced
    left,right = equ.split("->")

    left = get_true_equation(left)
    right = get_true_equation(right)

    
    for i in range (left.count("")):
        left.remove("")
    for i in range (right.count("")):
        right.remove("")
    
    if sorted(left) == sorted(right):
        return True
    else:
        return False
    
    









    
def get_true_equation(equ): # Splits every part by additon and splits up every element
    
    broken_by_add = equ.replace(" ", "").split("+")
    coefficients = []
    
    for i in range (len(broken_by_add)):
        coefficients.append(get_coefficient(broken_by_add[i]))
    for i in range(len(broken_by_add)):
        broken_by_add[i] = get_true_part(broken_by_add[i])*coefficients[i]


    
    ret_list = []

    for i in range (len(broken_by_add)):
        ret_list += broken_by_add[i]
    
    
    return ret_list


def get_true_part(equ): # Helps distinguish parentheses
    elements =[]
    curr_str = ""
    curr_mult = ""
    in_parens = False
    for i in equ:
        if i == ")":
            curr_str = get_true_part(curr_str)
            in_parens = False
        elif i == "(":
            if curr_mult == "":
                curr_mult = "1"
            for l in range (int(curr_mult)):
                elements.append(curr_str)
            curr_mult = ""
            curr_str = ""
            in_parens = True
        elif in_parens == True:
            curr_str += i
        elif i.isupper():
            if curr_mult == "":
                curr_mult = "1"
            for l in range (int(curr_mult)):
                elements.append(curr_str)
            curr_mult = ""
            curr_str = i
        elif i.isdigit():
            curr_mult += i
        else:
            curr_str += i
    if curr_mult == "":
        curr_mult = "1"
    for i in range (int(curr_mult)):    
        elements.append(curr_str)
    ret_list = []

    for i in elements:
        if type(i) == list:
            ret_list += i
        if type(i) == str:
            ret_list.append(i)
    return ret_list


def get_coefficient(equ): # Gets the co-efficient of a part of the equation
    co = ""
    for i in equ:
        if i.isdigit() == True:
            co += i
        else:
            break
    if co == "":
        co = "1"
    return (int(co))
    '''copy = equ
    if copy[0].isdigit() == False:
        copy = "1"
    return (int(copy[0]))'''


    
