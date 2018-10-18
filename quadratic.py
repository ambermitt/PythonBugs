import math

def quadraticSolver(a, b, c):
    roots.append((-b + math.sqrt(pow(b, 2) - (4*a*c)))/(2*a))
    roots.append((-b - math.sqrt(pow(b, 2) - (4*a*c)))/(2*a))
    return roots

# returns a list in the format of [variable, a, b, c]
# given an equation in the form a(variable)^2 + b(variable) + c
def equationParser(equation):
    equation = equation.replace(" ", "")
    coef=[]
    squaredIndex = equation.find("^2")
    variable = equation[squaredIndex - 1]
    coef.append(variable)
    a = int(equation[:equation.find(variable)])
    coef.append(a)
    b = int(equation[squaredIndex + 1:equation.find(variable,squaredIndex + 1)]
    coef.append(b)
    c = int(equation[equation.find(variable,squaredIndex + 1) + 1:]
    coef.append(c)
    return coef

def main():
    equation = input("Equation: ")
    parsed = equationParser(equation)
    roots = quadraticSolver(parsed[0], parsed[1], parsed[2])
    print(parsed[0], "=", roots[0])
    print(parsed[0], "=", roots[1])
