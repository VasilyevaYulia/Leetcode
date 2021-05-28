'''
Example:
  Input: sentence = "I speak Goat Latin"
  Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
'''

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        ans = sentence.split(' ')
        vowel = 'aeiou'
        for i in range(len(ans)):
            if ans[i][0].lower() not in vowel:
                ans[i] = ans[i][1:] + ans[i][0]
            ans[i] = ans[i] + 'maa' + i*'a'
        return ' '.join(ans)
