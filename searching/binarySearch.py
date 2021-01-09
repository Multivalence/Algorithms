from manipulate import Manipulate
import time
import random

def binary_search(array : list, key : int) -> int:
    """
    This function searches for a given element in an array using the binary search algorithm

    Parameters
    ----------
    array : list
        List containing numbers
    key : int
        Element to locate in list

    Returns
    -------
    int
        Index at which given number appears in list. -1 if not found.
    """

    stuff = []

    while True:

        startingIndex = len(array) // 2
        stuff.append(startingIndex)

        if key > array[startingIndex]:
            if len(array) == 1:
                return -1
            array = array[startingIndex:]


        elif key < array[startingIndex]:

            if len(array) == 1:
                return -1

            array = array[:startingIndex]
            stuff.append(-1*startingIndex)

        elif key == array[startingIndex]:
            return sum(stuff)



if __name__ == '__main__':
    m = Manipulate()

    with open('../data.txt', 'r') as textFile:
        objects = [m.countVowels(i.strip()) for i in textFile.readlines()]

    key = random.randint(0,8)

    t1 = time.perf_counter()

    # Will take average of ~ 0.0009 seconds if minimum system requirements are met
    print(binary_search(sorted(objects),key))

    t2 = time.perf_counter()
    print(f"Binary Search finished in {t2 - t1} seconds. Array size: {len(objects)}")


    #Testing to get average time

    '''
    count = []
    
    for i in range(100):
        key = random.randint(0, 8)

        t1 = time.perf_counter()

        binary_search(objects, key)

        t2 = time.perf_counter()
        count.append(t2 - t1)

    print(sum(count) / len(count))
    '''