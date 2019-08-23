# Electron Calculations

class Electron_Configurations: # Sets up a class used for getting electron configurations
    def __init__(self):
        pass
    
    def Get_Info(line): # Helper function for the rest of the functions
        data = line.split() 
        data[1] = data[1][1:-1]
        data[3] = " ".join(data[3:])
        return data # Returns Name, then atomic number, then the configuration

    def get_config(search): # Gets the full electron configuration
        with open("Electron Configurations.txt", "r") as file:
            for line in file:
                broken = Electron_Configurations.Get_Info(line)
                if broken[2] == search or broken[1] == search or broken[0] == search:
                    return broken[3]
                    break
    def get_outer(search): # Just gets the outer energy level
        with open("Electron Configurations.txt", "r") as file:
            for line in file:
                broken = Electron_Configurations.Get_Info(line)
                if broken[2] == search or broken[1] == search or broken[0] == search:
                    outer = []
                    x = broken.pop()
                    outer.append(x)
                    while "s" not in x:
                        x = broken.pop()
                        outer.append(x)
                    outer.reverse()
                    return " ".join(outer)
                    break
    def get_total_outer(search): # returns the total number of electrons in the outermost energy level
        outer_levels = Electron_Configurations.get_outer(search)
        total = 0

        for i in range(len(outer_levels)):
            if outer_levels[i] == "s" or outer_levels[i] == "p":
                total += int(outer_levels[i+1])
        return total

            
