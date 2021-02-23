

class Relation:

    def __init__(self, m):
        self.m = m

    def mat(self):
        for i in range(len(self.m)):
            x=-1
    
            while(x<0 or x>7):
                x = int(input("How many elements is " + chr(i+97) + " related to: "))
        
            for j in range(x):
                y = input("Enter the element " + chr(i+97) + " is related to: ")

                while(ord(y)>103):
                    y = input("Enter the element " + chr(i+97) + " is related to: ")

                self.m[i][ord(y)-97] = 1


    def ref(self):
        j=0
        for i in range(len(self.m)):
            if(self.m[i][j] == 1):
                j+=1
            else:
                return False
        return True
    

    def sym(self):
        for i in range(len(self.m)):
            for j in range(len(self.m)):
                if(self.m[i][j] != self.m[j][i]):
                    return False
        return True


    def boolProd(self):
        res = [[0]*len(self.m[0]) for c in range(len(self.m))]

        for i in range (len(self.m)):
            for j in range (len(self.m[0])):
                sum = 0
                for k in range (len(self.m[0])):
                    sum += self.m[i][k] * self.m[k][j]
                    
                    if(sum>0):
                        res[i][j] = 1
        return res


    def tran(self):
        boolMat = self.boolProd()

        for i in range (len(self.m)):
            for j in range (len(self.m[0])):
                if ((boolMat[i][j] == 1) and not(self.m[i][j] == 1)):
                    return False
        return True