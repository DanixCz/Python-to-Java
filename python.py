promena1=5
promena2=3

def obs_kruh(r):
    if r > 0:
        return 3.14 * (r**2)
    else:
        return "Zaddal jsi nulovou nebo zapornou hodnotu"

def obv_kruh(r:float) -> float:
    """
    Zadeejte polomer kruhu r:
    """
    if r > 0:
        return 2*3.14*r
    
    else:
        return "Zaddal jsi nulovou nebo zapornou hodnotu"
    
def obs_obd(a,b):
    if a > 0 and b > 0:
        return a**2 + b**2
    else:
        return "Zadal jsi nulovou nebo zapornou hodnotu"
    
print(obv_kruh(promena1))
print(obv_kruh(promena1))
print(f"Obsah obdelníku je: {obs_obd(promena1, promena1)}")