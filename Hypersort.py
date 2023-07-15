import random


def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[random.randint(0, len(arr) - 1)]
    lesser, equal, greater = [], [], []

    for x in arr:
        if x < pivot:
            lesser.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)

    return quicksort(lesser) + equal + quicksort(greater)


def generate_random_numbers(n):
    random_numbers = [random.randint(1, 1000000) for _ in range(n)]
    return random_numbers


random_numbers = generate_random_numbers(10000000)
print(quicksort(random_numbers))
