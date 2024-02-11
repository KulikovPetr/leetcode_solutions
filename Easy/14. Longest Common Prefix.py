class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output_string = ''
        breakflag = False
        if len(strs) == 1:
            return strs[0]
        while not breakflag:
            if output_string == strs[0]:
                return output_string
            output_string = strs[0][0:len(output_string)+1]
            for item in strs:
                if output_string == item[0:len(output_string)] and item != '':
                    pass
                else:
                    breakflag = True

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""