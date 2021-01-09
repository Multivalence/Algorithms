from manipulate import Manipulate
import time

'''
#Time Quadruples every time elements are doubled
BUBBLE SORT
5000: ~3 seconds
10000: ~11.5 seconds
20000: ~46 seconds
40000: ~184 seconds
80000: ~736 seconds
160000: ~2944 seconds

# Time triples every time elements are doubled
TIMSORT (BUILT-IN)
5000: 0.002 seconds
10000: 0.006 seconds
20000: 0.018 seconds
40000: 0.054 seconds
80000: 0.162 seconds
160000: 0.486 seconds

Processor: Intel(R) Core(TM) i7-2600 CPU @ 3.40 Ghz 
RAM: 16.0 GB
System Type: 64-bit operating system, x64-based processor

'''
def bubble_sort(array : list) -> list:
    """
    This function sorts an array of numbers using the bubble sort algorithm

    Parameters
    ----------
    array : list
        List containing numbers

    Returns
    -------
    list
        The sorted list
    """

    for i in range(len(array)-1):
        for p in range(0, len(array)-i-1):
            if array[p+1] < array[p]:
                array[p], array[p + 1] = array[p + 1], array[p]

    return array


if __name__ == '__main__':
    m = Manipulate()

    with open('../data.txt', 'r') as textFile:
        objects = [m.countConsonants(i.strip()) for i in textFile.readlines()]

    t1 = time.perf_counter()

    # Will take ~49.1 minute(s) to complete if minimum system requirements are met
    print(bubble_sort(objects))

    t2 = time.perf_counter()
    print(f"Bubble Sort finished in {t2-t1} seconds. Array size: {len(objects)}")

