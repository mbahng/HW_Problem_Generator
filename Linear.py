import random

def slope_intercept_to_point_slope():
    m = 0
    while m == 0:
        m = random.randint(-8, 10)
    b = random.randint(-15,15)
    if b > 0:
        return f"Convert to point slope form: $y = {m}x + {b}$"
    elif b < 0:
        return f"Convert to point slope form: $y = {m}x {b}$"
    elif b == 0:
        return f"Convert to point slope form: $y = {m}x$"

def point_slope_to_slope_intercept():
    m = 0
    while m == 0:
        m = random.randint(-8, 10)
    x, y = random.randint(-15, 15), random.randint(-15, 15)
    if x > 0:
        if y > 0:
            return f"Convert to slope intercept form: $y - {y} = {m} (x - {x})$"
        if y == 0:
            return f"Convert to slope intercept form: $y = {m} (x - {x})$"
        if y < 0:
            return f"Convert to slope intercept form: $y + {-y} = {m} (x - {x})$"
    if x == 0:
        if y > 0:
            return f"Convert to slope intercept form: $y - {y} = {m} x$"
        if y == 0:
            return f"Convert to slope intercept form: $y = {m}{x}$"
        if y < 0:
            return f"Convert to slope intercept form: $y + {-y} = {m}{x}$"
    if x < 0:
        if y > 0:
            return f"Convert to slope intercept form: $y - {y} = {m} (x + {-x})$"
        if y == 0:
            return f"Convert to slope intercept form: $y = {m} (x + {-x})$"
        if y < 0:
            return f"Convert to slope intercept form: $y + {-y} = {m} (x + {-x})$"

def graph_slope_intercept():
    six_m = 0
    while six_m == 0:
        six_m = random.randint(-3, 4)
    b = random.randint(-8, 8)
    if six_m > 0:
        if b > 0:
            return "\item Graph the following: $y = \\frac{%s}{6} x + \\frac{%s}{2}$" % (six_m, b)
        elif b == 0:
            return "\item Graph the following: $y = \\frac{%s}{6} x$" % (six_m)
        elif b < 0:
            b = -b
            return "\item Graph the following: $y = \\frac{%s}{6} x - \\frac{%s}{2}$" % (six_m, b)
    elif six_m < 0:
        six_m = -six_m
        if b > 0:
            return "\item Graph the following: $y = -\\frac{%s}{6} x + \\frac{%s}{2}$" % (six_m, b)
        elif b == 0:
            return "\item Graph the following: $y = -\\frac{%s}{6} x$" % (six_m)
        elif b < 0:
            b = -b
            return "\item Graph the following: $y = -\\frac{%s}{6} x - \\frac{%s}{2}$" % (six_m, b)

def graph_point_slope():
    six_m = 0
    while six_m == 0:
        six_m = random.randint(-3, 4)
    x_0, y_0 = random.randint(-8, 8), random.randint(-8, 8)
    if six_m > 0:
        if x_0 > 0:
            if y_0 > 0:
                return "\item Graph the following: $y - \\frac{%s}{2} = \\frac{%s}{6} (x - \\frac{%s}{2})$" % (
                    y_0, six_m, x_0)
            elif y_0 == 0:
                return "\item Graph the following: $y = \\frac{%s}{6} (x - \\frac{%s}{2})$" % (
                    six_m, x_0)
            elif y_0 < 0:
                y_0 = -y_0
                return "\item Graph the following: $y + \\frac{%s}{2} = \\frac{%s}{6} (x - \\frac{%s}{2})$" % (
                    y_0, six_m, x_0)
        elif x_0 == 0:
            if y_0 > 0:
                return "\item Graph the following: $y - \\frac{%s}{2} = \\frac{%s}{6} x$" % (
                    y_0, six_m)
            elif y_0 == 0:
                return "\item Graph the following: $y = \\frac{%s}{6} x$" % (
                    six_m)
            elif y_0 < 0:
                y_0 = -y_0
                return "\item Graph the following: $y + \\frac{%s}{2} = \\frac{%s}{6} x$" % (
                    y_0, six_m)
        elif x_0 < 0:
            x_0 = -x_0
            if y_0 > 0:
                return "\item Graph the following: $y - \\frac{%s}{2} = \\frac{%s}{6} (x + \\frac{%s}{2})$" % (
                    y_0, six_m, x_0)
            elif y_0 == 0:
                return "\item Graph the following: $y = \\frac{%s}{6} (x + \\frac{%s}{2})$" % (
                    six_m, x_0)
            elif y_0 < 0:
                y_0 = -y_0
                return "\item Graph the following: $y + \\frac{%s}{2} = \\frac{%s}{6} (x + \\frac{%s}{2})$" % (
                    y_0, six_m, x_0)
    elif six_m < 0:
        six_m = -six_m
        if x_0 > 0:
            if y_0 > 0:
                return "\item Graph the following: $y - \\frac{%s}{2} = -\\frac{%s}{6} (x - \\frac{%s}{2})$" % (
                    y_0, six_m, x_0)
            elif y_0 == 0:
                return "\item Graph the following: $y = -\\frac{%s}{6} (x - \\frac{%s}{2})$" % (
                    six_m, x_0)
            elif y_0 < 0:
                y_0 = -y_0
                return "\item Graph the following: $y + \\frac{%s}{2} = -\\frac{%s}{6} (x - \\frac{%s}{2})$" % (
                    y_0, six_m, x_0)
        elif x_0 == 0:
            if y_0 > 0:
                return "\item Graph the following: $y - \\frac{%s}{2} = -\\frac{%s}{6} x$" % (
                    y_0, six_m)
            elif y_0 == 0:
                return "\item Graph the following: $y = -\\frac{%s}{6} x$" % (
                    six_m)
            elif y_0 < 0:
                y_0 = -y_0
                return "\item Graph the following: $y + \\frac{%s}{2} = -\\frac{%s}{6} x$" % (
                    y_0, six_m)
        elif x_0 < 0:
            x_0 = -x_0
            if y_0 > 0:
                return "\item Graph the following: $y - \\frac{%s}{2} = -\\frac{%s}{6} (x + \\frac{%s}{2})$" % (
                    y_0, six_m, x_0)
            elif y_0 == 0:
                return "\item Graph the following: $y = -\\frac{%s}{6} (x + \\frac{%s}{2})$" % (
                    six_m, x_0)
            elif y_0 < 0:
                y_0 = -y_0
                return "\item Graph the following: $y + \\frac{%s}{2} = -\\frac{%s}{6} (x + \\frac{%s}{2})$" % (
                    y_0, six_m, x_0)

def graph_linear_functions(amount: int):
    for i in range(amount):
        type = random.randint(1, 2)
        if type == 1:
            print(graph_slope_intercept())
        elif type == 2:
            print(graph_point_slope())
    return ""

def converting_linear_problems_generator(amount: int):
    for i in range(amount):
        type = random.randint(1, 2)
        if type == 1:
            print(f"\item {slope_intercept_to_point_slope()}")
        elif type == 2:
            print(f"\item {point_slope_to_slope_intercept()}")
    return None

if __name__ == '__main__':
    converting_linear_problems_generator(20)
    pass