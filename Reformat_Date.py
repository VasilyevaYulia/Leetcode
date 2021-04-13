'''
Given a date string in the form Day Month Year, where:

Day is in the set {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}.
Month is in the set {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}.
Year is in the range [1900, 2100].
Convert the date string to the format YYYY-MM-DD, where:

YYYY denotes the 4 digit year.
MM denotes the 2 digit month.
DD denotes the 2 digit day.
'''
class Solution:
    def reformatDate(self, date: str) -> str:
        date = date.split(" ")
        month = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        
        if len(date[0]) < 4: date[0] = "0" + date[0]
        return date[2] + "-" + month[date[1]] + "-" + date[0][:2]
        
        '''
        month = {'01':"Jan", '02':"Feb", '03':"Mar", '04':"Apr", '05':"May", '06':"Jun", '07':"Jul", '08':"Aug", '09':"Sep", '10':"Oct", '11':"Nov", '12':"Dec"}
        ans = date[-4:] + '-'
        for i in month:
            if month[i] == date[-8:-5]:
                ans += i
                ans += '-'
        if len(date[:-11]) == 1:
            ans += '0'
            ans += date[:-11]    
        else: ans += date[:-11] 
        return ans
        '''
