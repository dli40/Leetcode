class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x= str(x)
        size = len(x)
        for i in range(size//2):
            if(x[i]!=x[size-1-i]):
                return False
        return True        
#ANALYSIS:
""" TIME: O(N)
    MEMORY: O(N)
    Checks to see if word is a palindrom. Compares each character to its corresponding character
    starting at the end of the word, then increments/decrements by one. Goes until the middle character."""
