#x is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from x. Each digit must be rotated - we cannot choose to leave it alone.
#A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other (on this case they are rotated in a different direction, in other words 2 or 5 gets mirrored); 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.
#Now given a positive number n, how many numbers x from 1 to n are good?

class Solution:
    def rotatedDigits(self, N: int) -> int:
        ans = []
        for i in range(1, N+1):
            i = str(i)
            if '3' not in i and '4' not in i and '7' not in i:
                if '2' in i or '5' in i or '6' in i or '9' in i:
                    ans.append(i)
        return len(ans)
