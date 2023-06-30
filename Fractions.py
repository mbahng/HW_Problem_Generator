import random

def fraction_of_number():
    denominator = random.randint(2, 12)
    numerator = random.randint(1, denominator)
    number = denominator * random.randint(1, 30)
    return "$\\frac{%s}{%s}$ of $%s$" %(numerator, denominator, number)


for i in range(10):
    print(f"\item {fraction_of_number()}")