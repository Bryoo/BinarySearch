# Http Client Program

First, you are to create a BinarySearch class, that inherits from the list class the following:

the __init__() takes two integers as parameters, a and b. a is the length of the list to be created and b is the step or difference between consecutive values. It should also initialize an instance variablelength`, that returns the number of elements in the array


Once you are done, create another method called search, it will take just one argument which is the value you are to find.

The search function should return a dictionary object, which contains

'count', the number of times you function iterated to find the index of the number in question, 'index' the index of the number in question


The search method should implement the binary search algorithm, each time you iterate, you should increase the count,

to test how efficient your implementation is.

## Getting Started
Some prerequisites are required to have achieved desired output.

    This code is written in Python3 and may have unexpected functionality when run with Python 2.x


Install pytest:
```
$ pip install pytest

```
Alternatively, Install nose
```
$ pip install nose

```

### Using the Code

clone the code from git using this limk:
```
git clone https://github.com/Bryoo/BinarySearch
```
Ensure you're in the main directory 'BinarySearch' and then run the code
```
python3 binarysearch.py

## Executing the tests included

if you've got pytest
```
$ py.test test_binary_search.py
```
If you've got nosetests
```
$ nosetests test_binary_search.py
```
Alternatively, if you do not have either nosetests or pytest installed, use:

```
$ python3 test_http_client.py
```

 The test cases present includes some tests for both edge and general cases:



