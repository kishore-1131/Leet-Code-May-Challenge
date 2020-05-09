class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        x1 = coordinates[0][0]
        y1 = coordinates[0][1]
        x2 = coordinates[1][0]
        y2 = coordinates[1][1]
        if (x2-x1)!=0 :
            m0 = ((y2-y1)/(x2-x1)) 
        else:
            return False
        for i in range(1,len(coordinates)):
            p1 = coordinates[0]
            p2 = coordinates[i]
            if (p2[0] - p1[0])!=0:
                m = (p2[1] - p1[1])/(p2[0] - p1[0])
                if(m!= m0):
                    return False
        return True  