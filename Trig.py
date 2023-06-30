import random
degrees = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 45, 135, 225, 315]
radians = ["0", "\\frac{\pi}{6}", "\\frac{\pi}{3}", "\\frac{\pi}{2}", "\\frac{2 \pi}{3}", "\\frac{5 \pi}{6}",
           "\\pi", "\\frac{7 \pi}{6}", "\\frac{4 \pi}{3}", "\\frac{3\pi}{2}", "\\frac{5 \pi}{3}", "\\frac{11 \pi}{6}",
           "2 \\pi", "\\frac{\pi}{4}", "\\frac{3 \pi}{4}", "\\frac{5 \pi}{4}", "\\frac{7 \pi}{4}"]

def sine(degree = True):
    if degree == True:
        print("\\item $\sin{(" + str(degrees[random.randint(0, 16)]) + "^\circ)}$")
    else:
        print("\\item $\sin{(" + str(radians[random.randint(0, 16)]) + ")}$")

def cosine(degree = True):
    if degree == True:
        print("\\item $\cos{(" + str(degrees[random.randint(0, 16)]) + "^\circ)}$")
    else:
        print("\\item $\cos{(" + str(radians[random.randint(0, 16)]) + ")}$")

def tangent(degree = True):
    if degree == True:
        print("\\item $\\tan{(" + str(degrees[random.randint(0, 16)]) + "^\circ)}$")
    else:
        print("\\item $\\tan{(" + str(radians[random.randint(0, 16)]) + ")}$")

def degrees_to_radians():
    print("\\item Convert to radians: $" + str(degrees[random.randint(0, 16)]) + "^\circ$")

def radians_to_degrees():
    print("\\item Convert to degrees: $" + str(radians[random.randint(0, 16)]) + "$")

def generate_converting_problems(amount):
    for i in range(amount):
        type = random.randint(0,1)
        if type == 0:
            degrees_to_radians()
        elif type == 1:
            radians_to_degrees()
    return None

def generate_trig_degree_problems(amount):
    for i in range(amount):
        type = random.randint(0, 2)
        if type == 0:
            sine()
        elif type == 1:
            cosine()
        elif type == 2:
            tangent()
    return None

def generate_trig_radians_problems(amount):
    for i in range(amount):
        type = random.randint(0, 2)
        if type == 0:
            sine(False)
        elif type == 1:
            cosine(False)
        elif type == 2:
            tangent(False)
    return None

generate_trig_radians_problems(50)