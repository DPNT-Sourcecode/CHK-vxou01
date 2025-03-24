from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    pricing = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40} # keeps track of individual sku pricing
    skus_list = list(skus) # convert string to list
    total = 0 
    
    for sku in skus_list:
        if sku not in pricing: # case: illegal input
            return -1
        else:
            total += pricing[sku]
    
    # subtract A 'discount'
    A_count = skus_list.count("A")
    if A_count >= 5:          
        total -= (A_count // 5) * 50
        A_count %= 5 #update remaining A count
    
    if A_count >= 3:
        total -= (A_count // 3) * 20

    # subtract B 'discount'
    if E_count < 2: # free B discount will be apllied instead
        B_count = skus_list.count("B")
        total -= (B_count // 2) * 15

    # subtract E 'discount'
    E_count = skus_list.count("E")
    if E_count >= 2:
        free_Bs = E_count // 2 
        if B_count < free_Bs:
            total -= B_count * pricing["B"]
        else:
            total -= free_Bs * pricing["B"]


    return total if skus_list else 0  # returns total amount unless empy


