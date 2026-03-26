import cmath 

def solve_quadratic():
    print("Quadratic Solver: ax^2 + bx + c = 0")
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

   
    d = (b**2) - (4*a*c)

    
    sol1 = (-b - cmath.sqrt(d)) / (2*a)
    sol2 = (-b + cmath.sqrt(d)) / (2*a)

    output_str = f"Inputs: a={a}, b={b}, c={c}\nSolutions: {sol1} and {sol2}\n"

    
    with open("quadratic_results.txt", "a") as f:
        f.write(output_str)
    
    print("Results saved to quadratic_results.txt")

