#You are given coordinates, a string that represents the coordinates of a square of the chessboard. Below is a chessboard for your reference.
#Return true if the square is white, and false if the square is black.
#The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first, and the number second.

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x = 'abcdefgh'
        y = '12345678'
        return (x.index(coordinates[0])%2) ^ (y.index(coordinates[1])%2)
        ''' 
        w = 'abcdefgh'
        n = '12345678'
        j = 1
        a = {}
        for i in n:
            for j, num in enumerate(w):
                if int(i)%2 == 0:
                    if j%2 == 0:
                        a[num+i] = True
                    else: a[num+i] = False
                else: 
                    if j%2 == 0:
                        a[num+i] = False
                    else: a[num+i] = True
        return a.get(coordinates)
        '''        
