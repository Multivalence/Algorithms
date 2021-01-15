
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
    
    if len(word) in [2, 3]:
        return 1 if word[0] == word[-1] else 0

    return (1 if word[0] == word[-1] else 0) + palindrome(word[1:-1])


if __name__ == '__main__':
    print(palindrome('ada'))  # 1
    print(palindrome('eadae'))  # 2
    print(palindrome('ade')) # 0
