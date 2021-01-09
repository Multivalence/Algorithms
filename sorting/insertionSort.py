from manipulate import Manipulate
import time


'''
# Time quadruples every time elements are doubled
INSERTION SORT      
5000: ~1.4 seconds
10000: ~5.6 seconds
20000: ~22.4 seconds
40000: ~89.6 seconds
80000: ~358.4 seconds
160000: ~1433.6 seconds

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

def insertion_sort(array : list) -> list:
    """
    This function sorts an array of numbers using the insertion sort algorithm

    Parameters
    ----------
    array : list
        List containing numbers

    Returns
    -------
    list
        The sorted list
    """

    for i in range(1, len(array)):
        iteration = array[i]
        index = i

        while iteration < array[index-1] and index > 0:
            array[index] = array[index - 1]
            index -= 1

        array[index] = iteration


    return array



if __name__ == '__main__':
    m = Manipulate()

    with open('../data.txt', 'r') as textFile:
        objects = [m.countNonAlpha(i.strip()) for i in textFile.readlines()]

    t1 = time.perf_counter()

    # Will take ~24 minute(s) to complete if minimum system requirements are met
    print(insertion_sort(objects))

    t2 = time.perf_counter()
    print(f"Insertion Sort finished in {t2-t1} seconds. Array size: {len(objects)}")