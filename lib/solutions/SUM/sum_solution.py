# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if (0 <= x <= 100) and (0 <= y <= 100):
        return x+y
    else:
        raise ValueError("Input is out of range")
