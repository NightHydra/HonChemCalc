from Chem_Equation_Balancer import *

def GetPercByMass(equ): # Gets each element by it's percentage of the total mass
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
    each = []
    for i in range (len(atoms_to_test)):
        mass += atom_count[i] * atom_weights[i]
        each.append(atom_count[i] * atom_weights[i])

    if 0 in each:
        print ("This is not a valid compound")
        return None
    for i in range(len(atoms_to_test)):
        print (atoms_to_test[i] , ": " , str(round(each[i]*100/mass, 2)) ,"%")


def GetEP(inp): # Inverse of the previous function
    masses = [0]*len(inp)

    with open("Elements.txt", "r") as file:
        for l in file:
            for i in range(len(inp)):
                if l.rstrip("\n") == inp[i][0]:
                    masses[i] = float(inp[i][1]/float(file.readline().rstrip("\n")))

    lowest_mass = masses[i]+1

    for i in masses:
        if i<lowest_mass:
            lowest_mass = i
    masses = list(map(lambda x: x/lowest_mass, masses))

    mult_by = 1
    
    for i in masses:
        if abs(i%1 - .5) <= 0.08: 
            mult_by *= 2
    for i in masses:
        if abs(i%1 - .33) <= 0.04:
            mult_by *= 3
    for i in masses:
        if abs(i%1 - .25) <= .04:
            mult_by *= 4
    for i in masses:
        if abs(i%1 - .75) <= 0.04:
            mult_by *= 4
    masses = list(map(lambda x: x*mult_by, masses))
    masses = list(map(lambda x: round(x, 0), masses))

    ans = ""
    for i in range(len(inp)):
        ans += inp[i][0]
        if masses[i] != 1:
            ans += str(int(masses[i]))
    return ans




