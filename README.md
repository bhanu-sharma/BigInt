# BigInt

The source code has been written in python 2.7.12

**#Intialisation:**


```
>>> A = BigInt('999') 

```


**addOne()**


The method adds one to the number and displays it accordingl
```
>>> A.addOne()
>>> '1000'

```

**adds(number)**


Adds other provided big int to original big int
``` 
>>> B = BigInt('99')
>>> A.adds(B)
>>> '1098'
>>> C = BigInt(A.adds(B))

```

**addAll(numbers)**


This method adds all the other provided big ints to the original big int. 
Input can be multiple values
```
>>> B = BigInt('1234')
>>> C = BigInt('99999')
>>> D = BigInt('0')
>>> A.addAll(B, C, D)
>>> '102233'
>>> G = BigInt(A.addAll(B, C, D))

```
