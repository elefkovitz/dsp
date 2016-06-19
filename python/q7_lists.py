# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
    """
    Given a list of strings, return the count of the number of strings
    where the string length is 2 or more and the first and last chars
    of the string are the same.

    >>> match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
    3
    >>> match_ends(['', 'x', 'xy', 'xyx', 'xx'])
    2
    >>> match_ends(['aaa', 'be', 'abc', 'hello'])
    1
    """
    #raise NotImplementedError
    counter = 0
    for x in words:
        if len(x) >= 2 and x[0] == x[-1]:
            counter = counter + 1
        else:
            pass
    print counter

match_ends(['aba', 'xyz', 'aa', 'x', 'bbb', 'xzzzx'])
match_ends(['', 'x', 'xy', 'xyx', 'xx'])

def front_x(words):
    """
    Given a list of strings, return a list with the strings in sorted
    order, except group all the strings that begin with 'x' first.
    e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].

    >>> front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
    ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
    >>> front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
    ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    """
    #raise NotImplementedError
    xArray = []
    yArray = []

    for i in words:
        if i[0] == 'x':
            xArray.append(i)
        if i[0] != 'x':
            yArray.append(i)
    print sorted(xArray) + sorted(yArray)


front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])

def sort_last(tuples):
    """
    Given a list of non-empty tuples, return a list sorted in
    increasing order by the last element in each tuple.
    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)].

    >>> sort_last([(1, 3), (3, 2), (2, 1)])
    [(2, 1), (3, 2), (1, 3)]
    >>> sort_last([(2, 3), (1, 2), (3, 1)])
    [(3, 1), (1, 2), (2, 3)]
    >>> sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
    [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    """
    #raise NotImplementedError
    playList = list(tuples)
    sortedList = sorted(playList, key=lambda x: x[-1])
    print sortedList

sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])

#This one also feels like a hacked solution, I have a feeling I definitely
#did this one wrong, but not sure how I could have done it better.
#What should I have used instead?

def remove_adjacent(nums):
    """
    Given a list of numbers, return a list where all adjacent equal
    elements have been reduced to a single element, so [1, 2, 2, 3]
    returns [1, 2, 3]. You may create a new list or modify the passed
    in list.

    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([2, 2, 3, 3, 3])
    [2, 3]
    >>> remove_adjacent([3, 2, 3, 3, 3])
    [3, 2, 3]
    >>> remove_adjacent([])
    []
    """
    newList = []
    newList.append(nums[0])
    #raise NotImplementedError
    for s in range(len(nums)):
        #print s, nums[s]
        if s >= 1 and nums[s] != nums[s-1]:
            newList.append(nums[s])
    print newList
        #print s, nums[s]
    #print nums
remove_adjacent([3, 2, 3, 3, 3])
remove_adjacent([2, 2, 3, 3, 3])

def linear_merge(list1, list2):
    """
    Given two lists sorted in increasing order, create and return a
    merged list of all the elements in sorted order. You may modify
    the passed in lists. Ideally, the solution should work in "linear"
    time, making a single pass of both lists.

    >>> linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
    ['aa', 'aa', 'aa', 'bb', 'bb']
    """
    #raise NotImplementedError
    mergedList = sorted(list1 + list2)
    print mergedList

linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
