

def substrings(word : str) -> list:

	"""
	Given a string, returns all palindromic sub-strings

	Parameters
	----------
	word : str
		String that may contain palindrome sub-strings

	Returns
	-------
	list
		all palindromic sub-strings found in word

	"""

	if len(word) == 0:
		return [word]
	
	subs = []
	subs.append(word)

	subs += substrings(word[1:])
	subs += substrings(word[:-1])
	

	return [i for i in set(subs) if len(i) > 1 and i == i[::-1] and i != ""]


	
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

	return len(substrings(word))
	

if __name__ == '__main__':
	print(palindrome('ada'))  # 1
	print(palindrome('eadae'))  # 2
	print(palindrome('ade')) # 0
	print(palindrome("array")) #2


	
