def egcd(phiN, given):
    if phiN == 0:
        return (given, 0, 1)
    else:
        g, x, y = egcd(given % phiN, phiN)
        return (g, y - (given // phiN) * x, x)
print("gcd , x1 , y1 = ",egcd(26,7))