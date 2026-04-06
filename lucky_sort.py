from random import randint, choice
from statistics import mean
import heapq

def randomize_positions(numbers):
    numbers = numbers[:]
    n = len(numbers)

    for i in range(n-1, 0, -1):
        j = randint(0, i)
        numbers[i], numbers[j] = numbers[j], numbers[i]

    return numbers

def extract_sorted(numbers, verbose=False):

    min_number = min(numbers)
    max_number = max(numbers)
    average_number = mean(numbers)

    numbers_len = len(numbers)

    last_inserted_element = None

    already_sorted = []

    new_numbers = []

    for i in range(numbers_len):
        el = numbers[i]
        if last_inserted_element == None or el >= last_inserted_element:
            number_percentage = (i+0.5)/numbers_len
            expected_number = 0
            if i <= numbers_len/2:
                expected_number = (average_number - min_number) * number_percentage * 2 + min_number
            else:
                expected_number = (max_number - average_number) * (number_percentage-0.5) * 2 + average_number
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

def extract_sorted_old(numbers, verbose=False):

    already_sorted = []
    new_numbers = []
    highest_number_in_sorted = numbers[0]
    
    for el in numbers:
        if el >= highest_number_in_sorted:
            already_sorted.append(el)
            highest_number_in_sorted = el
        else:
            new_numbers.append(el)

    if verbose:
        print("already_sorted")
        print(already_sorted)

        print("new_numbers")
        print(new_numbers)

    return already_sorted, new_numbers

def k_way_merge(sorted_lists):
    heap = []
    result = []

    # initialize heap with first element of each list
    for list_index, lst in enumerate(sorted_lists):
        if lst:  # ignore empty lists
            heapq.heappush(heap, (lst[0], list_index, 0))

    # extract min and push next from same list
    while heap:
        value, list_index, element_index = heapq.heappop(heap)
        result.append(value)

        next_index = element_index + 1
        if next_index < len(sorted_lists[list_index]):
            next_value = sorted_lists[list_index][next_index]
            heapq.heappush(heap, (next_value, list_index, next_index))

    return result

array_size = 40

numbers = []

verbose = True

for i in range(array_size):
    numbers.append(randint(1,100))

already_sorted_numbers = []

iteration_counter = 1

while len(numbers) > 0:

    print("")
    print("iteration", iteration_counter)

    numbers = randomize_positions(numbers)
    
    print("numbers")
    print(numbers)
    print("")

    already_sorted, numbers = extract_sorted(numbers, verbose=verbose)
    already_sorted_numbers.append(already_sorted)

    iteration_counter += 1

merged_numbers = k_way_merge(already_sorted_numbers)
print("merged_numbers")
print(merged_numbers)