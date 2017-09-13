# BigInt

The source code has been written in python 2.7.12

**#Intialisation:**


```
e = BigInt(999) 
>>> [9,9,9]

```


**addOne()**


The method adds one to the number and displays it accordingl
```
e.addOne()
>>> [1,0,0,0]

```

**adds(number)**


Adds other provided big int to original big int
``` 
e.adds(99)
>>> [1,0,9,8]

```

**addALL(numbers)**


This method adds all the other provided big ints to the original big int. 
Input can be multiple values
```
e.addAll(1,0,99999,12345)
>>> [1, 1, 3, 3, 4, 4]

```
