#Given a list paths of directory info, including the directory path, and all the files with contents in this directory, return all the duplicate files in the file system in terms of their paths. You may return the answer in any order.
#A group of duplicate files consists of at least two files that have the same content.

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = defaultdict(list) 
        
        for i in paths:
            a = i.split()
            b = a[0] #путь 
            for j in a[1:]:
                c = j.split('(') #окончание пути
                g = c[1][0:-1]
                d[g].append(f'{b}/{c[0]}') # f-строки для помощи с форматированием. f-strings являются строковыми литералами с «f» в начале и фигурные скобки, содержащие выражения, которые в дальнейшем будут заменены своими значениями
        ans = []
        for i in d.values():
            if len(i)>1:
                ans.append(i)
        return ans
