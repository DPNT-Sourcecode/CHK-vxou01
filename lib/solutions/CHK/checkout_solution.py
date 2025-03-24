

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    pricing = {"A": 50, "B": 30, "C": 20, "D": 15} 
    skus = skus.split(",")
    total = 0
    for sku in skus:
        total += pricing[sku]
    return total


