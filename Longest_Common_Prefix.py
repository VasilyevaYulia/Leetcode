#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ("")
        if len(strs) == 1:
            return (strs[0])

        ans = strs[0]
        c = len(ans)
        for str in strs[1:]:
            while ans != str[0:c]:
                ans = ans[0:(c-1)]
                c -= 1
                if c == 0:
                    return ("")
        return(ans)
