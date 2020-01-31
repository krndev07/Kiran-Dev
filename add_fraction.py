def addFraction(num1, den1, num2, den2):
    from math import gcd
    num = num1*den2+num2*den1
    den = den1*den2
    ka=gcd(num,den)
    h=num//ka
    d=den//ka
    print(str(h)+"/"+str(d))