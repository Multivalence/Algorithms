
def palindrome(word : str) -> int:
    """
    Given a string, calculates the amount of palindromes that exist within that string

    Parameters
    ----------
    word : str
       String that may contain palindrome sub-strings

    Returns
    -------
    int
       number of palindromes in string

    """
    
    word = word.lower()

    count = []

    for i in range(len(word)):
        for p in range(i+1, len(word)+1):
            count.append(word[i : p])


    t = [i for i in set(count) if len(i) > 1 and i == i[::-1]]
    return len(t)



if __name__ == '__main__':
    print(palindrome('ada'))  # 1
    print(palindrome('eadae'))  # 2
    print(palindrome('ade')) # 0
