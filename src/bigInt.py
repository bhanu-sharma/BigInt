class BigInt:
    '''
    The class internally stores the input number in form of an integer list.
    e = BigInt(999) 
    >>> [9,9,9]
    '''
    def __init__(self, num):
        '''
        Q0:
        Constructor constructor method, saves the original number.
        '''
        self.num = list(map(int, list(str(num))))
        print self.num
    def addOne(self):
        '''
        Q1
        The method adds one to the number and displays it accordingly
        e.addOne()
        >>> [1,0,0,0]
        '''
        bx = self.num[:]
        for i in range(len(bx))[::-1]:
            temp = bx[i]
            if i != 0:
                temp += 1
                if temp/10 == 0:
                    bx[i] = temp
                    break
                else:
                    bx[i] = temp%10
            else:
                temp += 1
                bx[i] = temp%10
                gec = bx[::-1]
                gec.append(temp/10)
                bx = gec[::-1]
        return bx
    def adds(self, by, multiple = False, test = [0]):
        '''
        Q2
        Adds other provided big int to original big int
        e.adds(99)
        >>> [1,0,9,8]
        '''
        sum_ = []
        carry = 0
        if multiple == False:
            bx = self.num[:]
        if multiple == True:
            bx = test
            
        by = list(map(int, list(str(by))))
        if len(bx) > len(by):
            x, y = bx, by
        if len(bx) < len(by):
            x, y = by, bx
        else: x, y = bx, by
        for i, j in zip(range(len(x))[::-1], range(len(y))[::-1]):
            tempx = x[i]
            tempy = y[j]
            temp = tempx + tempy + carry
            if temp/10 != 0:
                sum_.append(temp%10)
                carry = temp/10
            else:
                sum_.append(temp)
                carry = 0
        if len(x) != len(y):
            for k in range(0,len(x)-len(y))[::-1]:
                tempx = x[k]
                temp = tempx + carry
                if temp/10 != 0:
                    sum_.append(temp%10)
                    carry = temp/10
                else:
                    sum_.append(temp)
                    carry = 0
        if carry !=0: sum_.append(carry)
        else: pass


        return sum_[::-1]
    def addAll(self, *args):
        '''
        Q3
        This method adds all the other provided big ints to the original big int. 
        Input can be multiple values
        e.addAll(1,0,99999,12345)
        >>> [1, 1, 3, 3, 4, 4]
        '''
        bx = self.num[:]
        sum_ = bx
        for i in args:
            #by = list(map(int, list(str(i))))
            sum_ = self.adds(i, multiple=True, test=sum_)
        return sum_