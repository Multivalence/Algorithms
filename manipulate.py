class Manipulate:


    # Counts the vowels (excluding y) in the string
    @staticmethod
    def countVowels(fileContent: str) -> int:

        """
           Counts vowels in provided text

           Parameters
           ----------
           fileContent : str
               String containing text

           Returns
           -------
           int
               Number of vowels in given text

           Raises
           -------
           AssertionError
                Raised if fileContent is not a string
           """

        assert isinstance(fileContent, str), "Given Parameter is not a string"
        vowels = "AaEeIiOoUu"
        allvowels = [i for i in fileContent if i in vowels]

        return len(allvowels)

    # Counts the Consonants (including y) in the string
    @staticmethod
    def countConsonants(fileContent: str) -> int:

        """
           Counts Consonants in provided text

           Parameters
           ----------
           fileContent : str
               String containing text

           Returns
           -------
           int
               Number of Consonants in given text

           Raises
           -------
           AssertionError
                Raised if fileContent is not a string
           """

        assert isinstance(fileContent, str), "Given Parameter is not a string"
        vowels = "AaEeIiOoUu"
        allcons = [i for i in fileContent if i not in vowels]

        return len(allcons)

    # Counts characters that are not letters
    @staticmethod
    def countNonAlpha(fileContent: str) -> int:

        """
           Counts non Alpha characters in provided text

           Parameters
           ----------
           fileContent : str
               String containing text

           Returns
           -------
           int
               Number of non alpha characters in given text

           Raises
           -------
           AssertionError
                Raised if fileContent is not a string
           """

        assert isinstance(fileContent, str), "Given Parameter is not a string"
        fileContent = list(fileContent)
        count = 0
        for i in fileContent:
            if not i.isalpha():
                count += 1

        return count
