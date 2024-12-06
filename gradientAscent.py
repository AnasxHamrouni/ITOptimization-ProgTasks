#Anas Khmais Hamrouni

def f(x):
    return -x**2 + 4*x + 1

def f_prime(x):
    return -2*x + 4

def gradient_ascent(x0, learning_rate, num_iterations):
    x = x0
    
    for i in range(num_iterations):
        gradient = f_prime(x)  
        x += learning_rate * gradient  # Update x in the direction of the gradient
    
    xmax = x
    return xmax, f(xmax)

#modify program input here
x0 = 0 
learning_rate = 0.1  
num_iterations = 100 

xmax, f_xmax = gradient_ascent(x0, learning_rate, num_iterations)
print(f"Approximate xmax: {xmax}")
print(f"f(xmax): {f_xmax}")
