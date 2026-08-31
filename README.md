# Lucky Sort

Lucky Sort is a Python sorting experiment that sorts a list of numbers through repeated randomization, extraction of sorted subsequences, and a final k-way merge.

## How it works

The program first generates a list of random integers between 1 and 100. The default list contains 40 numbers.

It then repeatedly performs the following steps:

1. The remaining numbers are randomly shuffled.
2. `extract_sorted()` scans the shuffled list and separates the numbers into two groups:
   - `already_sorted`: numbers that can be added to the current sorted sequence.
   - `new_numbers`: numbers that do not fit and will be processed again in a later iteration.
3. The extracted sorted sequence is stored.
4. The process continues with the remaining numbers until all numbers have been extracted.

The extraction logic uses the minimum, maximum, and average values of the current list to estimate what value would be expected at each position. A number is accepted into the current sorted sequence when it is greater than or equal to the previously accepted number and is sufficiently close to the estimated value for its position.

Once all numbers have been separated into sorted sequences, `k_way_merge()` combines those sequences into one final sorted list.

## Functions

### `randomize_positions(numbers)`

Creates a shuffled copy of the input list using the Fisher-Yates shuffle algorithm.

The original list is not modified.

### `extract_sorted(numbers, verbose=False)`

Extracts a subset of the numbers that can form an increasing sequence.

It uses the minimum, maximum, average, and current position in the list to estimate the expected value at each position.

It returns:

    already_sorted, new_numbers

`already_sorted` contains the numbers extracted during the current iteration, while `new_numbers` contains the numbers that will be processed again.

### `extract_sorted_old(numbers, verbose=False)`

An earlier and simpler version of the extraction algorithm.

It iterates through the list and keeps a number if it is greater than or equal to the largest number already added to the sorted sequence. All other numbers are returned for another iteration.

### `k_way_merge(sorted_lists)`

Merges multiple sorted lists into a single sorted list.

It uses a min-heap from Python's `heapq` module. The heap contains the next available element from each input list, allowing the smallest available value to be selected at each step.

## Algorithm flow

    Generate random numbers
            ↓
    Shuffle remaining numbers
            ↓
    Extract a sorted subset
            ↓
    Save the sorted subset
            ↓
    Repeat with remaining numbers
            ↓
    Merge all sorted subsets
            ↓
    Final sorted list

## Configuration

The number of generated elements can be changed with:

    array_size = 40

The random values are currently generated in the range 1–100:

    randint(1, 100)

Verbose output can be enabled or disabled with:

    verbose = True

## Requirements

Python 3 with the standard library. No external dependencies are required.

## Running

Run the Python file directly:

    python main.py

The program will generate a random list, process it through multiple iterations of Lucky Sort, and print the resulting sorted list.
