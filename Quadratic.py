import random

def factored_to_standard():
    '''Quadratic Factored form to Standard form problem generator.'''
    a = random.randint(-4, 4)
    c = random.randint(-4, 4)
    b = random.randint(-15, 15)
    d = random.randint(-15, 15)
    if b > 0 and d > 0 and a!= 0 and c!= 0:
        return f"Expand the following: $({a}x + {b})({c}x + {d})$"
    elif b < 0 and d > 0 and a!= 0 and c!= 0:
        return f"Expand the following: $({a}x {b})({c}x + {d})$"
    elif b > 0 and d < 0 and a!= 0 and c!= 0:
        return f"Expand the following: $({a}x + {b})({c}x {d})$"
    elif b < 0 and d < 0 and a!= 0 and c!= 0:
        return f"Expand the following: $({a}x {b})({c}x {d})$"
    elif a==0 or c==0:
        e = random.randint(-4, 4)
        k = random.randint(-10, 10)
        if k > 0:
            return f"Expand the following: ${random.randint(2, 20)}({e}x + {k})$"
        elif k < 0:
            return f"Expand the following: ${random.randint(2, 20)}({e}x {k})$"
    return ""

def vertex_to_standard():
    a = 0
    while a == 0:
        a = random.randint(-15, 15)
    h = random.randint(-15, 15)
    k = random.randint(-15, 15)
    if a == 1:
        a = ""
    elif a == -1:
        a = "-"
    if k > 0:
        if h > 0:
            return f"Expand the following: ${a}(x + {k})^2 + {h}$"
        elif h == 0:
            return f"Expand the following: ${a}(x + {k})^2$"
        elif h < 0:
            return f"Expand the following: ${a}(x + {k})^2 {h}$"
    elif k == 0:
        if h > 0:
            return f"Expand the following: ${a}x^2 + {h}$"
        elif h == 0:
            return f"Expand the following: ${a}x^2$"
        elif h < 0:
            return f"Expand the following: ${a}x^2 {h}$"
    elif k < 0:
        if h > 0:
            return f"Expand the following: ${a}(x {k})^2 + {h}$"
        elif h == 0:
            return f"Expand the following: ${a}(x {k})^2$"
        elif h < 0:
            return f"Expand the following: ${a}(x {k})^2 {h}$"

def standard_to_vertex():
    a = 0
    while a == 0:
        a = random.randint(-6, 6)
    b = random.randrange(-20, 20, 2)
    c = random.randrange(-15, 15)
    if a == 1:
        a = ""
    elif a == -1:
        a = "-"
    if b> 0:
        if c > 0:
            return f"Complete the square for the following: ${a} x^2 + {b}x + {c}$"
        elif c == 0:
            return f"Complete the square for the following: ${a} x^2 + {b}x$"
        elif c < 0:
            return f"Complete the square for the following: ${a} x^2 + {b}x {c}$"
    elif b == 0:
        if c > 0:
            return f"Complete the square for the following: ${a} x^2 + {c}$"
        elif c == 0:
            return f"Complete the square for the following: ${a} x^2$"
        elif c < 0:
            return f"Complete the square for the following: ${a} x^2 {c}$"
    elif b<0:
        if c > 0:
            return f"Complete the square for the following: ${a} x^2 {b}x + {c}$"
        elif c == 0:
            return f"Complete the square for the following: ${a} x^2 {b}x$"
        elif c < 0:
            return f"Complete the square for the following: ${a} x^2 {b}x {c}$"
    return ""

def easy_standard_to_factored():
    alpha = random.randint(-15, 15)
    beta = random.randint(-15, 15)
    b = alpha + beta
    c = alpha * beta
    if b > 0:
        if c > 0:
            return f"Factor the following: $x^2 + {b}x + {c}$"
        elif c == 0:
            return f"Factor the following: $x^2 + {b}x$"
        elif c < 0:
            return f"Factor the following: $x^2 + {b}x {c}$"
    elif b == 0:
        if c > 0:
            return f"Factor the following: $x^2 + {c}$"
        elif c == 0:
            return f"Factor the following: $x^2$"
        elif c < 0:
            return f"Factor the following: $x^2 {c}$"
    elif b < 0:
        if c > 0:
            return f"Factor the following: $x^2 {b}x + {c}$"
        elif c == 0:
            return f"Factor the following: $x^2 {b}x$"
        elif c < 0:
            return f"Factor the following: $x^2 {b}x {c}$"
    return ""

def hard_standard_to_factored():
    alpha = random.randint(-15, 15)
    beta = random.randint(-15, 15)
    coefficient1, coefficient2 = 0, 0
    while coefficient1 == 0 or coefficient2 == 0:
        coefficient1 = random.randint(-3, 4)
        coefficient2 = random.randint(-3, 4)
    a = coefficient1 * coefficient2
    b = coefficient1 * beta + coefficient2 * alpha
    c = alpha * beta
    if b > 0:
        if c > 0:
            return f"Factor the following: ${a}x^2 + {b}x + {c}$"
        elif c == 0:
            return f"Factor the following: ${a}x^2 + {b}x$"
        elif c < 0:
            return f"Factor the following: ${a}x^2 + {b}x {c}$"
    elif b == 0:
        if c > 0:
            return f"Factor the following: ${a}x^2 + {c}$"
        elif c == 0:
            return f"Factor the following: ${a}x^2$"
        elif c < 0:
            return f"Factor the following: ${a}x^2 {c}$"
    elif b < 0:
        if c > 0:
            return f"Factor the following: ${a}x^2 {b}x + {c}$"
        elif c == 0:
            return f"Factor the following: ${a}x^2 {b}x$"
        elif c < 0:
            return f"Factor the following: ${a}x^2 {b}x {c}$"
    return ""

def graph_quadratic_functions():

    return None

def converting_quadratic_problems_generator(amount: int):
    for i in range(amount):
        type = random.randint(1, 7)
        if type == 1:
            print(f"\item {factored_to_standard()}")
        elif type == 2:
            print(f"\item {vertex_to_standard()}")
        elif type == 3 or type == 6:
            print(f"\item {standard_to_vertex()}")
        elif type == 4 or type == 7:
            print(f"\item {easy_standard_to_factored()}")
        #elif type == 5:
        #    print(f"\item {hard_standard_to_factored()}")
    return None

def find_discriminant(amount: int):
    for i in range(amount):
        a = 0
        while a == 0:
            a = random.randint(-3, 3)
        b, c = random.randint(-10, 10), random.randint(-12, 12)
        if b > 0:
            b = "+ " + str(b) + "x"
        elif b == 0:
            b = ""
        elif b < 0:
            b = str(b) + "x"
        if c > 0:
            c = "+ " + str(c)
        elif c == 0:
            c = ""
        elif c < 0:
            c = str(c)
        print(f"\item Find the discriminant of: y = ${a}x^2 {b} {c}$")
    return None

def find_roots(amount: int):
    for i in range(amount):
        a = 0
        while a == 0:
            a = random.randint(-3, 3)
        b, c = random.randint(-10, 10), random.randint(-12, 12)
        if b > 0:
            b = "+ " + str(b) + "x"
        elif b == 0:
            b = ""
        elif b < 0:
            b = str(b) + "x"
        if c > 0:
            c = "+ " + str(c)
        elif c == 0:
            c = ""
        elif c < 0:
            c = str(c)
        print(f"\item Find the roots of: y = ${a}x^2 {b} {c}$")
    return None

if __name__ == '__main__':
    for i in range(10): 
        print("\item " + f"{standard_to_vertex()}"[39:])
    pass