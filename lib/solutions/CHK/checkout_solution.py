from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    pricing = {"A": 50, "B": 30, "C": 20, "D": 15} # keeps track of individual sku pricing
    skus_list = list(skus) # convert string to list
    total = 0 
    
    for sku in skus_list:
        if sku not in pricing: # case: illegal input
            return -1
        else:
            total += pricing[sku]
    
    # subtract 'discount'
    A_count = skus_list.count("A")
    total -= (((A_count//3)%3) * 20)

    B_count = skus_list.count("B")
    total -= (((B_count//2)%2) * 15)

    return total if skus_list else -1 # returns total amount unless empy





