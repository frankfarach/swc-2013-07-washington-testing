#!/usr/bin/env python

def list_extract(numlist):
    """Recursively flatten any combination of nested lists and/or tuples"""
    if type(numlist) == list or type(numlist) == tuple:
        for element in numlist:
            for subvalue in list_extract(element):
                yield subvalue
    else:
        yield numlist

def mean(numlist):
    """Calculate the mean of the values in numlist

    Input
    =====
    `numlist` (`list`, `tuple`, or nested `lists` and or `tuples`) - List of values whose mean will be calculated

    Output
    ======
    (`float`) - Mean of the values in numlist
    """
    try :
        numlist = list(list_extract(numlist))
        total = sum(numlist)
        length = len(numlist)
        if length == 0:
            return None
    except TypeError :
        raise TypeError("The list was not numbers.")
    except :
        print "Something unknown happened with the list."
    return float(total)/length


def test_mean():
    assert mean([0, 0, 0, 0]) == 0
    assert mean([0, 200]) == 100
    assert mean([0, -200]) == -100
    assert mean([0]) == 0
    assert mean([1, 2]) == 1.5
    assert mean([]) == None
    assert mean([[1,2], [3,4]]) == 2.5
    assert mean([[1, 2, 3]]) == 2
    assert mean([[]]) == None
    assert mean((0, 0)) == 0
    assert mean([[], [0,1,2]]) == 1
    assert mean([[[5, 6, [6, 7]], []]]) == 6
    assert mean([1e-20, -1e-20]) == 0

test_mean()
