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
               "W": 20,
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
    M_count = skus_list.count("M")
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
    if H_count >= 10:          
        total -= (H_count // 10) * 20
        H_count %= 10 #update remaining H count to use 5H discount

    # subtract H 'discount' 5H for 45
    if H_count >= 5:
        total -= (H_count // 5) * 5

    # subtract K 'discount' 2K for 150
    total -= (K_count // 2) * 10

    # subtract N 'discount' 3N get one M free
    if N_count >= 3:
        free_Ms = N_count // 3 
        
        if M_count < free_Ms:
            total -= M_count * pricing["M"]
        else:
            total -= free_Ms * pricing["M"]
        
        # subtract free_Ms 
        if M_count > 0:
            M_count -= free_Ms

    return total if skus_list else 0  # returns total amount unless empy



