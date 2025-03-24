from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    pricing = {"A": 50, "B": 30, "C": 20, "D": 15} # keeps track of individual sku pricing
    # skus = skus.split("") # split input into individual sku
    total = 0 
    
    for sku in skus:
        if sku not in pricing: # case: illegal input
            return -1
        else:
            total += pricing[sku]
    
    # subtract 'discount'
    A_count = skus.count("A")
    total -= (((A_count//3)%3) * 20)

    B_count = skus.count("B")
    total -= (((B_count//2)%2) * 15)

    return total if sku else -1# returns total amount





