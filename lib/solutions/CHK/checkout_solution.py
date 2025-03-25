from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    
    # keeps track of individual sku pricing
    pricing = {"A": 50, 
               "B": 30, 
               "C": 20, 
               "D": 15, 
               "E": 40, 
               "F": 10,
               "G": 20,
               "H": 10,
               "I": 35,
               "J": 60,
               "K": 80,
               "L": 90,
               "M": 15,
               "N": 40,
               "O": 10,
               "P": 50,
               "Q": 30,
               "R": 50,
               "S": 30,
               "T": 20,
               "U": 40,
               "V": 50,
               "X": 90,
               "Y": 10,
               "Z": 50} 
    skus_list = list(skus) # convert string to list
    total = 0 
    
    # add price for each individual sku
    for sku in skus_list:
        if sku not in pricing: # case: illegal input
            return -1
        else:
            total += pricing[sku]
    
    # sku counts to be used for disocunts
    A_count = skus_list.count("A")
    B_count = skus_list.count("B")
    E_count = skus_list.count("E")
    F_count = skus_list.count("F")
    H_count = skus_list.count("H")
    K_count = skus_list.count("K")
    N_count = skus_list.count("N")
    P_count = skus_list.count("P")
    Q_count = skus_list.count("Q")
    R_count = skus_list.count("R")
    U_count = skus_list.count("U")
    V_count = skus_list.count("V")



    # subtract A 'discount' 5A for 200
    if A_count >= 5:          
        total -= (A_count // 5) * 50
        A_count %= 5 #update remaining A count to use 3A discount

    # subtract A 'discount' 3A for 130
    if A_count >= 3:
        total -= (A_count // 3) * 20

    # subtract E 'discount' 2E get one B free
    if E_count >= 2:
        free_Bs = E_count // 2 
        
        if B_count < free_Bs:
            total -= B_count * pricing["B"]
        else:
            total -= free_Bs * pricing["B"]
        
        # subtract free_Bs so the 2B for 45 discount can be used
        if B_count > 0:
            B_count -= free_Bs

    # subtract B 'discount' 2B for 45
    total -= (B_count // 2) * 15

    # subtract F 'discount' 3F for 2
    total -= (F_count // 3) * 10

    # subtract H 'discount' 10H for 80
    if A_count >= 5:          
        total -= (A_count // 5) * 50
        A_count %= 5 #update remaining A count to use 3A discount

    # subtract H 'discount' 5H for 45
    if A_count >= 3:
        total -= (A_count // 3) * 20

    return total if skus_list else 0  # returns total amount unless empy


#A B C D E CBAABCABBAAAEEAA
# A: 9 == 380
# B: 5 == 90
# C: 3 == 60
#D : 1 == 15
# E: 3 == 120