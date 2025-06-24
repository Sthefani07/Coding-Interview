# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.


from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) -1  # the last index in the string
        
        while left < right:
                s[left], s[right] = s[right], s[left]
                left = left + 1
                right = right - 1

s = Solution()
string = ["h","e","l","l","o"]
print(string)  # ["o","l","l","e","h"]
string = ["H","a","n","n","a","h"]
print(string)  # ["h","a","n","n","a","H"]
print("---  another example ---")


#another example of reverting a string, although not in place. in this case we use the reverse() method
def reverseName(s):
    s.reverse()
    return s
print(reverseName(["S","t","h", "e","f","a","n","i"]))  # ["i","n","a","f","e","h","t","S"]
