'''
Updated on Oct. 13, 2023

@author: olgap
'''

import periodictable as pdt

stable_isos = []
unstable_isos = []


def stability_checker(iso):
    '''
    determines stability of given isotope based on N/Z value 
    for elements below z = 20, function returns 'stable' if N/Z <= 1
    for elements between 20 and 80, function returns 'stable' if N/Z <= 1.2
    for elements above z = 80, function returns 'unstable'
    
    Args:
    iso: an isotope object from the periodictable package 
    
    Return: 
    stability: a string, either 'stable' or 'unstable', determined
    from pre-set stability criteria for N_over_Z
    
    N_over_Z: a ratio : calculated ratio of neutrons to protons
    
    '''
    A = iso.isotope
    Z = iso.number
    N = A - Z
    
    if Z <= 0:
        print (iso)
        print('invalid proton number')
    else:
        None
        
    N_over_Z  = round(N / Z, 2) 
    
    s = 'likely stable'
    us = 'likely unstable'
    
    firstNZ_limit = 1
    secondNZ_limit = 1.2
    
    if Z <= 20:
        if N_over_Z <= firstNZ_limit:
            stability = s
        else:
            stability = us
    
    elif 20 < Z < 80:
        if N_over_Z < secondNZ_limit:
            stability = s
        else:
            stability = us
            
    elif Z >= 80:
        stability = us
        
    else:
        None
   
    return stability, N_over_Z
    

''' generating list of all isotopes  '''


all_isotopes_list = []

#for elmt in pdt.elements:
#    print (elmt) prints the atomic symbol of the element
#    print (elmt.isotopes) prints a list of all isotopes of the element

def all_isotope_generator():
    '''
    This function goes through every isotope and appends it to all_isotopes_list. it stops at U-235
    
    Args: N/A
    Return: N/A
    Side-effects: updates the all_isotopes_list with all isotopes upto U-235
    
    '''
    for elmt in pdt.elements:
        for iso in elmt.isotopes:
            # if iso == 235:
            #     break
            all_isotopes_list.append(elmt[iso])
            
    return None

# checking that list is reasonable length, expecting ~ 3000
all_isotope_generator()

#print("length of list: ", len(all_isotopes_list))
#if len(all_isotopes_list) > 3000:
#   print("isotopes list is too long, check code")
#print(all_isotopes_list)

''' stability checker ''' 

for iso in all_isotopes_list:
    stabilityguesser = stability_checker(iso)[0]
    if stabilityguesser == 'likely stable':
        stable_isos.append(iso)
    else:
        unstable_isos.append(iso)

''' final output of number of stable and unstable isotopes'''
print('The simplified N/Z ratio calculation results in', len(stable_isos), \
     'stable isotopes out of', len(all_isotopes_list))
print('In reality, ~266 isotopes are stable.')


# def stability_checker(iso, stable, unstable):
#     '''
#     Calculates the ratio of neutrons to protons based on input of isotopes
#     from the periodictable package.
#
#     Args:
#     iso: an isotope object from the periodictable package
#     stable: a string input
#     unstable: a string input  
#
#     Return: 
#     stability: a variable assigned to one of the string inputs 
#     (stable or unstable), determined from stability criteria for 
#     N_over_Z
#
#     N_over_Z: a ratio : calculated ratio of neutrons to protons
#     '''
#     A = iso.isotope
#     Z = iso.number
#     N = A - Z
#
#     if Z <= 0:
#         print (A, Z)
#         print('invalid proton number')
#     else:
#         None
#
#     N_over_Z  = round(N / Z, 2) 
#
#
#     firstNZ_limit = 1
#     secondNZ_limit = 1.5
#
#     if Z <= 20:
#         if N_over_Z <= firstNZ_limit:
#             stability = stable
#         else:
#             stability = unstable
#
#     elif 20 < Z < 80:
#         if N_over_Z < secondNZ_limit:
#             stability = stable
#         else:
#             stability = unstable
#
#     elif Z >= 80:
#         stability = unstable
#
#     else:
#         None
#
#     return stability, N_over_Z
#
#
# s = 'likely stable'
# us = 'likely unstable'

# for iso in all_isotopes_list:
#     stabilityguesser = stability_checker(iso, stable=s, unstable=us)[0]
#     if stabilityguesser == s:
#         stable_isos.append(iso)
#     else:
#         unstable_isos.append(iso)
