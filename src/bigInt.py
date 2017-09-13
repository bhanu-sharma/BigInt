class BigInt:

    '''
    The class internally stores the input number in form of an integer list.
    >>> A = BigInt(999) 

    '''
    def __init__(self, num):
        
        '''
        Q0:
        Constructor constructor method, saves the original number.
        
        '''
        self.num = list(map(int, list(str(num))))
        
    def addOne(self):
        
        '''
        Q1
        The method adds one to the number and displays it accordingly
        >>> A.addOne()
        >>> '1000'
        
        '''
        temp_Big_int = self.num[:]
        for i in range(len(temp_Big_int))[::-1]:
            temp = temp_Big_int[i]
            if i != 0:
                temp += 1
                if temp/10 == 0:
                    temp_Big_int[i] = temp
                    break
                else:
                    temp_Big_int[i] = temp%10
            else:
                temp += 1
                temp_Big_int[i] = temp%10
                rev = temp_Big_int[::-1]
                rev.append(temp/10)
#                 temp_Big_int = rev[::-1]
                self.num = rev[::-1]
                
        num_string = reduce((lambda x, y: str(x)+str(y)), sum_[::-1])
        return num_string
    
    def adds(self, bigint, multiple = False, inp = [0]):
        
        '''
        Q2
        Adds other provided big int to original big int

        >>> B = BigInt(99)
        >>> A.adds(B)
        >>> '1098'

        '''
        sum_ = []
        carry = 0
        
        if multiple == False:
            bigint_x = self.num[:]
            
        if multiple == True:
            bigint_x = inp
            
#         by = list(map(int, list(str(by))))
        bigint_y = bigint.num
    
        if len(bigint_x) > len(bigint_y):
            x, y = bigint_x, bigint_y
            
        if len(bigint_x) < len(bigint_y):
            x, y = bigint_y, bigint_x
            
        else: x, y = bigint_x, bigint_y
            
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
        
        self.num = sum_[::-1]
        num_string = reduce((lambda x, y: str(x)+str(y)), sum_[::-1])
        return num_string
    
    def addAll(self, *args):

        '''
        Q3
        This method adds all the other provided big ints to the original big int. 
        Input can be multiple values

        >>> C = BigInt(99999)
        >>> D = BigInt(1234)
        >>> A.addAll(B, C, D)
        >>> '102232'
        
        '''
        sum_ = self.num[:]
        
        for i in args:
            sum_ = list(map(int, self.adds(i, multiple=True, inp=sum_)))
        
        self.num = sum[:]
        num_string = reduce((lambda x, y: str(x)+str(y)), sum_)
        return num_string