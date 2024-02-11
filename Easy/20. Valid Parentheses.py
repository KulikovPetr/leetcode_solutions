class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')':'(', '}':'{',']':'['}
        stack = []
        if len(s)%2 != 0:
            return False
        for item in s:
            if item == '(' or item == '{' or item == '[':
                stack.append(item)
            elif len(stack)>0:
                if brackets[item] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""