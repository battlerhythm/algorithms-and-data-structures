class BubbleSort(object):
    @classmethod
    def sort(cls, alist):
        loopCount = len(alist)-1
        while loopCount != 0:
            for i in range(len(alist)-1):
                if alist[i] > alist[i+1]:
                    alist[i], alist[i+1] = alist[i+1], alist[i]
            loopCount -= 1
        return alist

class InsertionSort(object):
    @classmethod
    def sort(cls, alist):
        i = 0
        while i < len(alist)-1:
            j = i
            while j >= 0 and alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                j -= 1
            i += 1
        return alist

class SelectionSort(object):
    @classmethod
    def sort(cls, alist):
        ptr = 0
        minVal = None 
        while ptr < len(alist):
            minVal = alist[ptr]
            for i, e in enumerate(alist[ptr+1:], ptr+1):
                if e < minVal:
                    minVal = e
                    alist[ptr], alist[i] = alist[i], alist[ptr]
            ptr += 1
        return alist

class MergeSort(object):
    @classmethod
    def sort(cls, alist):
        if len(alist) <= 1:
            return alist
        left = alist[:len(alist)//2]
        right = alist[len(alist)//2:]
        left = cls.sort(left)
        right = cls.sort(right)
        return cls._merge(left, right)

    @classmethod
    def _merge(cls, left, right):
        result = []
        while left and right:
            if left[0] <= right[0]:
                result.append(left[0])
                del left[0]
            else:
                result.append(right[0])
                del right[0]
        while left:
            result.append(left[0])
            del left[0]
        while right:
            result.append(right[0])
            del right[0]
        return result 

class QuickSort(object):
    @classmethod
    def sort(cls, alist):
        cls._sort(alist, 0, len(alist)-1)
        return alist

    @classmethod
    def _sort(cls, alist, start, end):
        if start < end:
            pivot = cls._partition(alist, start, end)
            cls._sort(alist, start, pivot-1)
            cls._sort(alist, pivot+1, end)
        return alist

    @classmethod
    def _partition(cls, alist, start, end):
        pivot = end
        wall = start
        left = start
        while left < pivot:
            if alist[left] < alist[pivot]:
                alist[wall], alist[left] = alist[left], alist[wall]
                wall += 1
            left += 1
        alist[wall], alist[pivot] = alist[pivot], alist[wall]
        pivot = wall
        return pivot