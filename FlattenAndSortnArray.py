def flatten_and_sort(array):
    fallten = [num for subarr in array for num in subarr]
    return sorted(fallten)