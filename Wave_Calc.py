# Wave calculator

# Equations -
    # E = nu * lambda
    # C = h * nu
# E = Speed of light (3*10^10)
# nu is frquency of waves (given in s^-1)
#lambda is the wavelength given in cm
# C = energy given in ergs
# h = Plancks constant (6.63*10^-27 erg - s)

def energy_to_wavelength(E): 
    C = 3 * 10**10
    nu = E/ (6.63*10**-27)
    return "{:.2e}".format(C/nu)


def energy_to_frequency(E):
	nu = E/ (6.63*10**-27)
	return "{:.2e}".format(nu)

def frequency_to_energy(nu):
    E = (6.63*10**-27)*nu
    return "{:.2e}".format(E)

def wavelength_to_energy(lambda_):
    nu = (3*10**10) / lambda_
    E = (6.63*10**-27) * (nu)
    return "{:.2e}".format(E)


def frequency_to_wavelength(nu):
    lambda_ = (3*10**10)/nu
    return "{:.2e}".format(lambda_)

def wavelength_to_frequency(lambda_):
    nu = (3*10**10)/lambda_
    return "{:.2e}".format(nu)

