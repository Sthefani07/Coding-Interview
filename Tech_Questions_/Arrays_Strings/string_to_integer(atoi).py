# Whitespace: Ignore any leading whitespace (" ").
# Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
# Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
# Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
# Return the integer as the final result.




class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        
        if not s:
                return 0    # in case of a empty string return 0
        
        i= 0 # inicialize with zero
        sign= 1 
        
        if s[i] == "+":
                i = i + 1
        elif s[i] == "-":
                i = i + 1
                sign = -1
                
        parsed = 0 
        
        while i < len(s):
                cur = s[i]
                if not cur.isdigit():
                        break
                else:
                        parsed = parsed * 10 + int(cur)
                        
                i = i + 1
                
        parsed = parsed * sign
        
        if parsed > 2**31 - 1:
                return 2**31 - 1
        elif parsed <= -2**31:
                return -2**31
        else:
                return parsed
        
s = Solution()
print(s.myAtoi("42"))               # 42    
print(s.myAtoi("   -42"))           # -42
print(s.myAtoi("4193 with words"))  # 4193
print(s.myAtoi("words and 987"))    # 0
print(s.myAtoi("-91283472332"))     # -2147483648
print(s.myAtoi("3.14159"))          # 3
print(s.myAtoi("+1"))               # 1
print(s.myAtoi("+-2"))              # 0