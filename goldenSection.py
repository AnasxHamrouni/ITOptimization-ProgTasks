#Anas Khmais Hamrouni

def f(x):
    #f(x) = (x - 2)^2 + 3
    return (x - 2)**2 + 3

def golden_section_method(a, b, tolerance):
    golden_ratio = (1 + 5**0.5) / 2 
    
    # Initialize points
    c = b - (b - a) / golden_ratio
    d = a + (b - a) / golden_ratio
    
    while (b - a) > tolerance:
        # Evaluate the function at points c and d
        fc = f(c)
        fd = f(d)
        
        # Update the interval
        if fc < fd:
            b = d
            d = c
            c = b - (b - a) / golden_ratio
        else:
            a = c
            c = d
            d = a + (b - a) / golden_ratio
    
    # Final approximation
    xmin = (a + b) / 2
    return xmin, f(xmin)

#modify program input here
a = 0 
b = 5 
tolerance = 1e-4 

xmin, f_xmin = golden_section_method(a, b, tolerance)
print(f"Approximate xmin: {xmin}")
print(f"f(xmin): {f_xmin}")
