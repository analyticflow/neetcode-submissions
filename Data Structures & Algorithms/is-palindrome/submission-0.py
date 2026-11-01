class Solution:
    def isPalindrome(self, s: str) -> bool: 
                filtered_chars = [char.lower() for char in s if char.isalnum()]
                cleaned_str = "".join(filtered_chars)
                return cleaned_str == cleaned_str[::-1]

                
