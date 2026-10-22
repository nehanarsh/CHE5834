'''
Created on 4 Oct 2026

@author: nehan
'''

atomic_mass = [48, 44, 8, 146, 14, 13, 137, 227] # list of mass numbers
atomic_number = [20, 16, 5, 62, 6, 8, 55, 89] # list of atomic numbers
BE_actual = [8.667, 7.996, 4.717, 8.280, 7.520, 5.812, 8.389, 7.651] # Binding Energies from KAERI
BE_SEMF = [] #Empty list for calculated BE values


element_list = zip(atomic_mass, atomic_number) 

for element in element_list:
    A = element[0] # retrieves mass number from list
    Z = element[1] # retrieves atomic number from list
    # calculates total BE using SEMF model
    BE = 15.73*A - 17.84*A**(2/3) - (0.7103*(Z)**2)/A**(1/3) - (23.69*(A-2*Z)**2)/A + (((-1)**Z)*33.6*(1+(-1)**A))/(2*A**(3/4))
    BE_nucleon = BE/A 
    BE_SEMF.append(round(BE_nucleon,3))

#displays BE SEMF and BE actual and BE differences    
print("A \t Proton \t BE/A \t BE/A(SEMF) \t delta BE")
for i in range(len(atomic_mass)):
    print(atomic_mass[i], "\t", atomic_number[i], "\t", BE_actual[i], "\t", BE_SEMF[i], "\t\t", round(BE_actual[i] - BE_SEMF[i],3))

