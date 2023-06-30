import random

def find_sum_of_arithmetic_sequence(amount: int):
    for i in range(amount):
        first_term = random.randint(1, 34)
        common_diff = random.randint(1, 14)
        number_of_terms = random.randint(16, 123)
        second_term = first_term + common_diff
        third_term = second_term + common_diff
        last_term = first_term + common_diff * (number_of_terms - 1)
        print(f"\item Find the sum of: ${first_term} + {second_term} + {third_term} + \ldots + {last_term}$")
    return None

def find_number_of_terms_in_sequence(amount: int):
    for i in range(amount):
        first_term = random.randint(-20, 34)
        common_diff = 0
        while common_diff == 0:
            common_diff = random.randint(-4, 14)
        number_of_terms = random.randint(16, 123)
        second_term = first_term + common_diff
        third_term = second_term + common_diff
        final_term = first_term + common_diff * (number_of_terms - 1)
        print(f"Find the number of terms in: {first_term}, {second_term}, {third_term}, \ldots, {final_term}")

find_sum_of_arithmetic_sequence(3)