#Anas Khmais Hamrouni

def f(x):
    #f(x) = x^3 − 6x^2 + 11x − 6
    return x**3 - 6*x**2 + 11*x - 6

def bisection_method(a, b, tolerance):
    if abs(f(a)) < tolerance:
        return a 
    if abs(f(b)) < tolerance:
        return b  

    if f(a) * f(b) > 0:
        print("No sign change in this interval.")
        return None
    
    while True:
        c = (a + b) / 2
        fc = f(c)
        
        if abs(fc) < tolerance:
            return c
        
        if f(a) * fc < 0:
            b = c
        else:
            a = c

#dividing given interval to 3 sub intervals to identify multiple roots if any
def find_roots(a, b, tolerance, subdivisions=3):
    roots = []
    step = (b - a) / subdivisions
    
    for i in range(subdivisions):
        #updating boundaries for subintervals
        x1 = a + i * step
        x2 = x1 + step

        # Check if the bounds are roots
        if abs(f(x1)) < tolerance:
            if x1 not in roots:
                roots.append(x1)
        if abs(f(x2)) < tolerance:
            if x2 not in roots:
                roots.append(x2)
        # Check for a sign change within the subinterval
        elif f(x1) * f(x2) <= 0:
            root = bisection_method(x1, x2, tolerance)
            if root is not None and root not in roots:
                roots.append(root)
    
    return roots

#modify program input here
a = 0.9  
b = 2.8 
tolerance = 1e-6

roots = find_roots(a, b, tolerance)
print(f"Roots found: {roots}")
