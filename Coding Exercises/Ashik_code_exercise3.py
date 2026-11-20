import scipy.integrate as sp
import radioactivedecay as rd
import math
import matplotlib.pyplot

NA = 6.022E+23
isotope_list = ['Ce-134', 'La-134', 'Ba-134']

def decay_eqns(t, atoms, lambda_ce, lambda_la):

    N_ce, N_la, N_ba = atoms
    
    d_Ce = - lambda_ce * N_ce
    d_La = lambda_ce * N_ce - lambda_la * N_la
    d_Ba = lambda_la * N_la

    return (d_Ce, d_La, d_Ba)

def initial_val(isotope):
    iso = rd.Nuclide(isotope)
    
    lambda_A = math.log(2) / iso.half_life('d')

    if iso.nuclide == 'Ce-134':
        N_0 = (0.01 / iso.atomic_mass) * NA 

    else:
        N_0 = 0

    return N_0, lambda_A

t_solutions = []
lambda_atoms = []
initial_atoms = []

for i in range(0, 31, 1):
    t_solutions.append(i)

for iso in isotope_list:
    initial_atoms.append(initial_val(iso)[0])
    lambda_atoms.append(initial_val(iso)[1])

sol = sp.solve_ivp(
    fun = decay_eqns,
    t_span = (0, 30),
    y0 = initial_atoms,
    t_eval = t_solutions,
    args=tuple(lambda_atoms[:2]),
    dense_output = True
)

print(sol)