# Copyright (c) 2013 the authors listed at the following URL, and/or
# the authors of referenced articles or incorporated external code:
# https://github.com/litleaf/

import sys,os,time

global totalInversion

def merge(left, right):
    global totalInversion
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            totalInversion += len(left[i:])
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result


def mergesort(lst):
    if len(lst) <= 1:
        return lst
    middle = int(len(lst) / 2)
    left = mergesort(lst[:middle])
    right = mergesort(lst[middle:])
    return merge(left, right)

if __name__ == "__main__":
    global totalInversion
    totalInversion = 0
    st = time.time()
    if len(sys.argv)<2:
        inputList = open("IntegerArray.txt").read().splitlines()
    else:
        inputList = open(sys.argv[1]).read().splitlines()
    inputList = map(int, inputList)
    mergesort(inputList)
    print 'Total Inversion:',totalInversion
    print 'Use time:',time.time()-st
