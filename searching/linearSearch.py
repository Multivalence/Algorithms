from manipulate import Manipulate
import time
import random

def linear_search(array : list, key : int) -> int:

    """
    This function searches for a given element in an array using the linear search algorithm

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

    for i in range(len(array)):
        if array[i] == key:
            return i

    return -1


if __name__ == '__main__':
    m = Manipulate()

    with open('../data.txt', 'r') as textFile:
        objects = [m.countVowels(i.strip()) for i in textFile.readlines()]

    key = random.randint(0,8)

    t1 = time.perf_counter()

    # Will take average of ~ (6.5761 * (10^-4)) seconds if minimum system requirements are met
    print(linear_search(objects,key))

    t2 = time.perf_counter()
    print(f"Linear Search finished in {t2 - t1} seconds. Array size: {len(objects)}")



    # Testing to get average time
    '''
    count = []
    
    for i in range(100):
        key = random.randint(0,8)
    
        t1 = time.perf_counter()
    
        print(linear_search(objects, key))
    
        t2 = time.perf_counter()
        count.append(t2-t1)
    
    
    print(sum(count) / len(count))
    
    '''