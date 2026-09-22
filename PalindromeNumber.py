class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: # number negatives isn't palindrome
            return False
        elif x % 11 == 0: # every number that your division is exectly by 11 without rest is palindrome
            return True
        else: # else  isn"t palindrome
            return False
        