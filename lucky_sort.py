from random import randint, choice
from statistics import mean

def randomize_positions(numbers):
    numbers_len = len(numbers)

    empty_array = [-float("inf")]*numbers_len

    positions_left = numbers_len
    for i in range(numbers_len):
        new_pos = randint(0, positions_left-1)
        
        if empty_array[new_pos] == -float("inf"):
            pass
        else:
            if choice([True, False]):
                while empty_array[new_pos] > -float("inf"):
                    new_pos += 1
                    if new_pos > numbers_len - 1:
                        new_pos = 0
            else:
                while empty_array[new_pos] > -float("inf"):
                    new_pos -= 1
                    if new_pos < 0:
                        new_pos = numbers_len - 1
        empty_array[new_pos] = numbers[i]

    return empty_array

def extract_sorted(numbers, verbose=False):

    min_number = min(numbers)
    max_number = max(numbers)

    numbers_len = len(numbers)

    last_inserted_element = -float("inf")

    already_sorted = []

    new_numbers = []

    for i in range(numbers_len):
        el = numbers[i]
        if el >= last_inserted_element or last_inserted_element == -float("inf"):
            number_percentage = (i+0.5)/numbers_len
            expected_number = (max_number - min_number) * number_percentage + min_number
            if el <= round(expected_number):
                already_sorted.append(el)
                last_inserted_element = el
            else:
                new_numbers.append(el)
        else:
            new_numbers.append(el)

    if verbose:
        print("already_sorted")
        print(already_sorted)

        print("new_numbers")
        print(new_numbers)

    return already_sorted, new_numbers

def merge(numbers1, numbers2):
    numbers = []
    index1 = 0
    index2 = 0

    while index1 < len(numbers1) and index2 < len(numbers2):
        if numbers1[index1] < numbers2[index2]:
            numbers.append(numbers1[index1])
            index1 += 1
        elif numbers1[index1] > numbers2[index2]:
            numbers.append(numbers2[index2])
            index2 += 1
        elif numbers1[index1] == numbers2[index2]:
            numbers.append(numbers1[index1])
            numbers.append(numbers1[index1])
            index1 += 1
            index2 += 1
    while index1 < len(numbers1):
        numbers.append(numbers1[index1])
        index1 += 1
    while index2 < len(numbers2):
        numbers.append(numbers2[index2])
        index2 += 1

    return numbers

array_size = 40

numbers = []

for i in range(array_size):
    numbers.append(randint(1,100))

verbose = True

already_sorted_numbers = []

iteration_counter = 1

while len(numbers) > 0:

    print("iteration", iteration_counter)


    numbers = randomize_positions(numbers)

    print("numbers")
    print(numbers)
    print("")

    already_sorted, numbers = extract_sorted(numbers, verbose=verbose)
    already_sorted_numbers.append(already_sorted)

    if len(numbers) == 0:
        break

    numbers.reverse()
    print("inverted")

    already_sorted, numbers = extract_sorted(numbers, verbose=verbose)
    already_sorted_numbers.append(already_sorted)

    print("\n")

    iteration_counter += 1

merged_numbers = []

for el in already_sorted_numbers:
    print("el")
    print(el)
    merged_numbers = merge(merged_numbers, el)
    print("merged_numbers")
    print(merged_numbers)