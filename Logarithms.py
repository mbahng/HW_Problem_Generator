import random

def solve_logarithms(amount: int):
    for i in range(amount):
        base = random.randint(2, 7)
        random1 = random.randint(-5, 7)
        if random1 >= 0:
            number = base ** random1
            print(f"\item $\log_{base} {number}$")
        elif random1 < 0:
            number = base ** -random1
            print("\item $\log_{%s} \\frac{1}{%s}$" % (base,number))
    return None

def produce_two_logs():
    base = random.randint(2, 7)
    random1 = random.randint(-2, 6)
    random2 = random.randint(-2, 6)
    if random1 >= 0:
        number = base ** random1
        first_log = f"\log_{base} {number}"
    elif random1 < 0:
        number = base ** -random1
        first_log = "\log_{%s} \\frac{1}{%s}" % (base,number)
    if random2 >= 0:
        number = base ** random2
        second_log = f"\log_{base} {number}"
    elif random2 < 0:
        number = base ** -random2
        second_log = "\log_{%s} \\frac{1}{%s}" % (base,number)
    return [first_log, second_log]

def sum_of_two_logs(amount: int):
    for i in range(amount):
        two_logs = produce_two_logs()
        first_log = two_logs[0]
        second_log = two_logs[1]
        print(f"\item ${first_log} + {second_log}$")

def diff_of_two_logs(amount: int):
    for i in range(amount):
        two_logs = produce_two_logs()
        first_log = two_logs[0]
        second_log = two_logs[1]
        print(f"\item ${first_log} - {second_log}$")

if __name__ == '__main__':
    #solve_logarithms(15)
    #sum_of_two_logs(10)
    #diff_of_two_logs(10)
    pass
