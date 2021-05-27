'''
  Example
Input: releaseTimes = [12,23,36,46,62], keysPressed = "spuda"
Output: "a"
Explanation: The keypresses were as follows:
Keypress for 's' had a duration of 12.
Keypress for 'p' had a duration of 23 - 12 = 11.
Keypress for 'u' had a duration of 36 - 23 = 13.
Keypress for 'd' had a duration of 46 - 36 = 10.
Keypress for 'a' had a duration of 62 - 46 = 16.
The longest of these was the keypress for 'a' with duration 16.
'''

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        maxTime = releaseTimes[0]
        ans = keysPressed[0]
        for i in range(1, len(releaseTimes)):
            difference = releaseTimes[i] - releaseTimes[i-1]
            if maxTime < difference:
                maxTime = difference
                ans = keysPressed[i]
            elif maxTime == difference:
                if ans < keysPressed[i]:
                    ans = keysPressed[i]
        return ans
