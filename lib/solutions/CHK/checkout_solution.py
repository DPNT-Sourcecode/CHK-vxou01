from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    pricing = {"A": 50, "B": 30, "C": 20, "D": 15} # keeps track of individual sku pricing
    skus = skus.split(",") # split input into individual sku
    total = 0 

    skus_counts = Counter(skus)
    
    for sku, count in skus_counts.items():
        if sku == "A" and count == 3:
            total += 130
        elif sku == "B" and count == 2:
            total += 45
        elif sku not in pricing:
            return -1
        else:
            total += pricing[sku]
    
    return total


