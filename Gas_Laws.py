
# P = Pressure(in atm)
#V = Volume(in Liters)
#n = number of moles (1 mol = 6.02 * 10^23 {Atoms or molecules})
#T = Temperature(in Kelvin)

class Boyles_Law: # Boyles Law - P1*V1 = P2*V2
    
    def get_Volume(P1, V1, P2):
        return (P1*V1)/P2
    def get_Pressure(P1, V1, V2):
        return (P1*V1)/V2


class Charles_Law: # Charles Law - V1/T1 = V2/T2

    def get_Volume(V1, T1, T2):
        return (V1*T2)/T1
    def get_Temperature(V1, T1, V2):
        return (T1*V2)/V1


class Avogadros_Law: # Avogadros Law - V1/n1 = V2/n2
    def get_Volume(V1, n1, n2):
        return (V1*n2)/n1
    def get_moles(V1, n1, V2):
        return (n1*V2)/V1


class Combined_Gas_Law: # P1*V1/T1 = P2*V2/T2
    def get_Pressure(P1, V1, T1, V2, T2):
        return (P1*V1*T2)/(T1*V2)
    def get_Volume(P1, V1, T1, P2, T2):
        return (P1*V1*T2)/(T1*P2)
    def get_Temperature(P1, V1, T1, P2, V2):
        return (P2*V2*T1)/(P1*V1)

class Ideal_Gas_Law: # PV = nRT (R = rate constant = 0.0821 atm-L/mol-K)
    def get_Pressure(V, n, T):
        return (n*0.0821*T)/(V)
    def get_Volume(P, n, T):
        return (n*0.0821*T)/(P)
    def get_moles(P, V, T):
        return (P*V)/(0.0821*T)
    def get_Temperature(P, V, n):
        return (P*V)/(n*0.0821)



