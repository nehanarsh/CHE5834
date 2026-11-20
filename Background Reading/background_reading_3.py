'''
Created on Oct. 11, 2021
Updated on Nov. 2, 2022

@author: olgap
'''

from scipy.integrate import solve_ivp
from scipy.constants import Avogadro as NA
import numpy as np
import radioactivedecay as rd
import matplotlib.pyplot as plt
from pyne.data import atomic_mass

tag = 'Fe'
iso = 59
nuc_id = tag + str(iso)
parent_id = tag + str(iso-1)
print (atomic_mass(nuc_id))
print (atomic_mass(parent_id))

''' general numpy '''
# using np.log10 to take log base 10 of array and single input
A = [1, 2, 3]
# print(np.log10(A))
B = 4
# print(np.log10(B))

''' radioactivedecay package '''
# some capability of radioactivedecay package
# creating a nuclide 
nuc_I135 = rd.Nuclide('I-135')

# obtaining the half-life
I135_halflife = nuc_I135.half_life('s')
# print (I135_halflife)
I135_decayconst = 0.693 / I135_halflife
# obtaining the decay product
next_daughter_135 = nuc_I135.progeny()

# a different way to get next decay product, e.g., for U-235
next_daughter_U235 = rd.Nuclide('I-135').progeny()

# print(I135_decayconst)
# print(next_daughter_I135)
# print (next_daughter_U235)

# initial amount of parent (t=0)
inv_mass_t0 = rd.Inventory({'I-135': 10.0}, 'g')
# set time elapsed to calc new inventory after decay takes place for this time
inv_mass_t1 = inv_mass_t0.decay(26.3, 'h')
# obtain masses of decay products
masses_progeny = inv_mass_t1.masses('g')
# can also get the amounts in other units
# if want to convert instead of specifying initial amount in these units
# if don't write 'mol' inside brackets below, default is moles, since this uses
# .moles() method, but still sometimes good to specify for clarify when quickly 
# looking at code later
moles_progeny = inv_mass_t1.moles('mol')

# prints all daughters (listed alphabetically)
# print (
    # 'amounts of all daughters in units specified when masses_progeny made: \n', 
    # masses_progeny)
# print()
# prints only selected daughters, using square bracket 'X-A' notation
# print (
#     'moles Ba-135: ', moles_progeny['Ba-135'], 
#     '# atoms Ba-135:',  inv_mass_t1.numbers()['Ba-135'], '\n',
#     'activity I-135 in Mega Curies:', inv_mass_t1.activities('MCi')['I-135']
#     )

# can look at order of daughter products graphically
# nuc_I135.plot()
# rd.Nuclide('U-235').plot() #would work if nuc_U135 not defined previously
inv_mass_t0 = rd.Inventory({'U-235': 10.0}, 'g')
inv_mass_t0.plot(100, 'h')
plt.show()


''' ODE solver '''

iso_list = ['I-135', 'Xe-135']


def decay_functs(t, y, k1, k2): 
    '''
    Args:
    t: independent variable
    y: dependent variable
    k1: decay constant for parent
    k2: decay constant for first daughter
    
    Returns:
    dy: list of all right hand sides of coupled ODEs
    when set up as dy/dt = f(y, t)
    
    Right-hand side of all coupled ODE's when set up as dy/dt = f(y, t).
    This is used as input into the built-in ODE solver, solve_ivp.
    '''
    # decay only ODE, production = 0
    # units for y dictated by initial input
    # E.g., if y_0 is atoms, y = [atoms]
    dy0 = -k1 * y[0]
    dy1 = k1 * y[0] -  k2 * y[1]
    dy = [dy0, dy1]
    
    return dy


def initial_val_decay_const(iso):
    
    '''
    Args
    iso: input isotope in 'X-A' string format, where X is the element symbol
    and A is the atomic mass number. This input is used in radioactivedecay 
    package inside this function
    
    Returns
    N_0_atoms: 
    decay_const: calculated from half-lives, which are 
    '''
    # based on input isotope (iso), calcs decay constant 
    # sets initial amount in grams, converted to atoms for initial value
    nuc = rd.Nuclide(iso)
    # log10 is base ten, log is natural log (ln)
    decay_const= np.log(2) / nuc.half_life('h') 
    
    if iso == iso_list[0]:
        input_g = 10
        nuc_MW = nuc.atomic_mass
        N_0_atoms = NA * input_g / nuc_MW
        
    else:
        N_0_atoms = 0     
    
    return N_0_atoms, decay_const

# the following could all be wrapped inside of a function
initialvalues_y_0 = []
k = []
    
# for iso in iso_list:
#     k.append(initial_val_decay_const(iso)[1])
#     initialvalues_y_0.append(initial_val_decay_const(iso)[0])
    
overalltime_range = [0, 80]

# t_solutions = [] 
# for i in range(0, 80, 2):
#     t_solutions.append(i)
    
    
# sol = solve_ivp(
#         decay_functs, overalltime_range, initialvalues_y_0, t_eval= t_solutions, 
#         args=(k), dense_output = True
#         )

# print('solution to first ODE, I-135:', sol.y[0])
# print ('')
# print('t-values ODEs solved at:', sol.t)    
# t_input = 40
# specific_sol = sol.sol(t_input)
# print (specific_sol)

''' Plotting solution to system of ODEs below '''

# this first for loop is not necessary to make the plots, but is more
# convenient then having to declare a bunch of variables for just the 
# I-135 y vals, then the Xe-135 vals (and so on, for a larger system of ODEs) 

plotcolours = ['mediumseagreen', 'mediumorchid']

# for solution, colr in zip(sol.y, plotcolours):
#     # plot function takes (x point list, y point list)
#     plt.plot(sol.t, solution, color = colr, linestyle ='-', marker = '.')


# info provided on font style, this is in "dictionary" style
# we have not learned about dictionaries yet, but the defining 
# of font properties using keywords below is easy to follow
font = {'family': 'arial',
    'color':  'black',
    'weight': 'normal',
    'size': 12,
    }


# first arg is the string name of the label, second arg is the font info,
# third arg is the desired padding space between the axis values and the 
# label location
plt.xlabel('Time (h)', fontdict = font, labelpad=8)
plt.ylabel('Number of Atoms', fontdict=font, labelpad=8) 
     
labels = iso_list
# labels are the string names of the different curves
# ncol is how many columns we want the legend labels to be in
# edgecolor is the colour of the legend box
# loc is the location of the legend
plt.legend(labels, ncol=1, edgecolor='black', loc='upper right', fontsize=10)
# turns tickmarks inward...only monsters have their ticks facing outward...
plt.tick_params(axis="both",direction="in", labelsize = '12')
# shows plot, which is useful when tweaking so you don't have to keep opening
# the saved file. Comment out the plt.show when you are happy with the plot
# and ready to save the figure 
# plt.show()

# saves figure with the string name.extension of filetype you would like 
# as the first arg...dpi is the resolution (300 or 400 dpi is good)
# figure is saved to your local git repository folder by default
# plt.savefig('I-135_activiy.png', dpi=300)


