# mass is given in grams
# Heat is given in Celcius
# Enrgy is given in calories
# SPH is given in cal/gC

# SPH - Specific heat value (example: sph of water is 1cal/gC)

class Enthalpy: # All equations for heat loss/gain
    # m * (H-HF) * sph = cal
    
    def Get_Total_Enthalpy(m, H, sph, fin_H):
        return m*abs(H-fin_H)*sph
    def Get_Mass(H, sph, cal, fin_H):
        return cal/(abs(H-fin_H)*sph)
    def Get_SPH(m, H, cal, fin_H):
        return cal/(m*abs(H-fin_H))


class No_Calorimeter_Equations(): # All equations for equations not using a calorimeter
    #m1 * (H1-HF) * sph1 = m2 * (HF-H2) * sph2
    
    def get_SPH(m1, m2, H1, H2, sph1, fin_H):

        
        return (m1*(H1-fin_H)*sph1)/(m2*(fin_H-H2))
        
    
    def get_mass(m1, H1, H2, sph1, sph2, fin_H):
        return (m1*(H1-fin_H)*sph1)/((fin_H-H2)*sph2)


    def get_init_heat(m1, m2, H1, sph1, sph2, fin_H):
        return ( -1*((  ( m1 * (H1-fin_H) *sph1)/(m2*sph2) )-fin_H))
    
    def get_final_heat(m1, m2, H1, H2, sph1, sph2):
        return ((( (m1*sph1*H1) + (m2*sph2*H2)))/( (m1*sph1)+(m2*sph2)))


class Calorimeter_Equations(): # Equations using a calorimeter
    # m1 * (H1-HF) * sph1 = (HF-H2)(m2*sph2 + m3*sph3)
    def get_Heat_LiqCal(m_S, sph_S, H_S, m_L, sph_L, m_C, sph_C, H_F):
        top = m_S*(H_S-H_F)*sph_S
        bottom = (m_L*sph_L)+(m_C*sph_C)
        return (top/bottom)+H_F

    def get_Mass_Liquid(m_S, sph_S, H_S, sph_L,H, m_C, sph_C, H_F):
        return ( ( (m_C*sph_C*H_F) - (m_C*sph_C*H) +\
                 (m_S*sph_S*H) - (m_S*sph_S*H_S)) / (sph_L*H-sph_L*H_F))

    def get_SPH_Liquid(m_S, sph_S, H_S, m_L,H, m_C, sph_C, H_F):
        return ( ( (m_C*sph_C*H_F) - (m_C*sph_C*H) +\
                 (m_S*sph_S*H) - (m_S*sph_S*H)) / (m_L*H-m_L*H_F))

    def get_Heat_Final(m_S, sph_S, H_S, m_L,sph_L, H, m_C, sph_C):
        top = (m_S*sph_S*H_S)+(m_L*sph_L*H)+(m_C*sph_C*H)
        bottom = (m_S*sph_S)+(m_L*sph_L)+(m_C*sph_C)
        return (top/bottom)

    def get_Heat_Obj(m_S, sph_S, m_L, sph_L, H, m_C, sph_C, H_F):
        top = (H-H_F)*( (m_L*sph_L) + (m_C*sph_C))
        bottom = (m_S*sph_S)
        return (top/bottom)+H

    def get_Mass_Obj(sph_S, H_S, m_L, sph_L, H, m_C, sph_C, H_F):
        top = (H-H_F)*( (m_L*sph_L) + (m_C*sph_C))
        bottom = ((H_S-H_F)*sph_S)
        return top/bottom

    def get_SPH_Obj(m_S, H_S, m_L, sph_L, H, m_C, sph_C, H_F):
        top = (H_F-H)*( (m_L*sph_L) + (m_C*sph_C))
        bottom = (m_S*(H_S-H_F))
        return top/bottom
