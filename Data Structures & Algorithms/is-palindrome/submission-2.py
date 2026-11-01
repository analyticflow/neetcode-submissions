class Solution:
    def isPalindrome(self, s: str) -> bool: 
                space = ""
                for c in s:
                    if c.isalnum():
                        space += c.lower()
                return space == space[::-1]

                
