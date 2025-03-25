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
               "K": 70,
               "L": 90,
               "M": 15,
               "N": 40,
               "O": 10,
               "P": 50,
               "Q": 30,
               "R": 50,
               "S": 20,
               "T": 20,
               "U": 40,
               "V": 50,
               "W": 20,
               "X": 17,
               "Y": 20,
               "Z": 21} 
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
    
    #group discount
    group_discount_skus = ["S", "T", "X", "Y", "Z"]

    # count group items
    group_skus = []
    for sku in group_discount_skus:
        group_skus.extend([sku] * skus_list.count(sku))
    # sort group items by price (to discount highest priced sku)
    # apply discount



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
        
        if B_count > 0:
            Bs_to_subtract = min(free_Bs, B_count)
            total -= Bs_to_subtract * pricing["B"]
            B_count -= Bs_to_subtract

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

    # subtract K 'discount' 2K for 120
    total -= (K_count // 2) * 20

    # subtract N 'discount' 3N get one M free
    if N_count >= 3:
        free_Ms = N_count // 3 

        if M_count > 0:
            Ms_to_subtract = min(free_Ms, M_count)
            total -= Ms_to_subtract * pricing["M"]
            M_count -= Ms_to_subtract

    # subtract P 'discount' 5P for 200
    total -= (P_count // 5) * 50

    # subtract R 'discount' 3R get one Q free
    if R_count >= 3:
        free_Qs = R_count // 3 

        if Q_count > 0:
            Qs_to_subtract = min(free_Qs, Q_count)
            total -= Qs_to_subtract * pricing["Q"]
            Q_count -= Qs_to_subtract

    # subtract Q 'discount' 3Q for 80
    total -= (Q_count // 3) * 10

    # subtract U 'discount' 4U for 3
    total -= (U_count // 4) * 40

    # subtract V 'discount' 3V for 130
    if V_count >= 3:          
        total -= (V_count // 3) * 20
        V_count %= 3 #update remaining A count to use 3A discount

    # subtract V 'discount' 2V for 90
    if V_count >= 2:
        total -= (V_count // 2) * 10

    return total if skus_list else 0  # returns total amount unless empy
