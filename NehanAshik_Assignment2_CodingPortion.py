'''
Created on 21 Oct 2026

@author: nehan
'''

import periodictable as pdt
import math

Rate_A = 5.7e-9                             # burnup rate of Yb-176
Rate_B = 1.008e-4                           # rate of decay Yb-177
Rate_C = 1.207e-6                           # rate of decay Lu-177
isotope_A = pdt.Yb[176]
A_abundance = isotope_A.abundance / 100     # abundance of Yb-176

def Lu_atoms(time, initial_atoms):
    '''
    takes time and initial number of atoms as an argument 
    Uses the analytical solution for Nc to calculate no. of atoms of C
    
    Args: 
        time 
        initial number of atoms
    Returns: 
        number of atoms of C
    
    '''
    A_term = math.exp(- Rate_A * time) / ((Rate_B - Rate_A) * (Rate_C - Rate_A))    # first exp term
    B_term = math.exp(- Rate_B * time) / ((Rate_A - Rate_B) * (Rate_C - Rate_B))    # second exp term
    C_term = math.exp(- Rate_C * time) / ((Rate_A - Rate_C) * (Rate_B - Rate_C))    # third exp term
    Nc = Rate_A * initial_atoms * Rate_B * (A_term + B_term + C_term) 
    
    return Nc 

initial_Yb = float(input("Enter initial mass of Yb in grams: "))    # takes user input for initial mass                     # calculates initial mass of A using abundance
initial_A_moles = ( initial_Yb / pdt.Yb.mass )
initial_A_atoms = ( A_abundance * initial_A_moles ) * 6.022e+23     # converts mass to no. of atoms

# initial condition for iteration
t = 0
max_Lu = Lu_atoms(t, initial_A_atoms)

# iterating to find maximum number of atoms
while True:
    N_Lu = Lu_atoms(t, initial_A_atoms)
    if N_Lu >= max_Lu:
        max_Lu = N_Lu   
        t += 3600       # iterates up every hour starting from t = 0
    else:
        break           # breaks the loop when number of atoms dips below the maximum

print("Maximum Atoms of Lu-177: ", max_Lu)

# initial conditions for iteration
t = 0
Lu_sat = Lu_atoms(t, initial_A_atoms)

# iterating to determine 90% saturation
while True:
    Lu_sat = Lu_atoms(t, initial_A_atoms)
    if Lu_sat >= (0.9 * max_Lu):
        break
    t += 3600

t_weeks = t / ( 3600 * 24 * 7)
print(f"Number of weeks: {t_weeks:.2f} , Atoms of Lu-177 at 90% saturation: {Lu_sat:.3e}")

