class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: # number negatives isn't palindrome
            return False
        elif str(x) == str(x)[::-1]: # change to string and compare your inverse
            return True
        else: # else  isn"t palindrome
            return False
        