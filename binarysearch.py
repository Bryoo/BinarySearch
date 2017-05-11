# -*- coding: utf-8 -*-

class BinarySearch(list):
    def __init__(self, length, diff):
        self.length = length
        self.diff = diff
        for el in range(1, length + 1):
            self.append(el * diff)

        self.length = len(self)

    """
    Given an array A of n elements with values or records A0 ... An−1,
    sorted such that A0 ≤ ... ≤ An−1, and key value T, the following
    subroutine uses binary search to find the index of T in A.

    1. Set L to 0 and R to n − 1.
    2. If L > R, the search terminates as unsuccessful.
    3. Set m (the position of the middle element) to the floor (the largest previous integer) of (L + R)/2.
    4. If Am < T, set L to m + 1 and go to step 2.
    5. If Am > T, set R to m – 1 and go to step 2.
    6. Now Am = T, the search is done; return m.
    """

    def search(self, key):
        left = 0
        right = self.length - 1
        index = -1
        count = 0
        while True:

            middle = ((left + right) // 2)
            if left > middle or middle > right:
                # terminate the loop as key isn't found
                break

            if self[middle] == key:
                # assign index to middle key value
                index = middle
                break

            elif self[right] == key:
                # assign index key value to index variable if found in right index after partition
                index = right
                break

            elif self[left] == key:
                # assign index key value to index variable if found in left index after partition

                index = left
                break

            elif middle == left or middle == right:
                break

            elif self[middle] < key:
                left = middle + 1

            elif self[middle] > key:
                right = middle - 1
            count += 1

        return {'count': count, 'index':index}
