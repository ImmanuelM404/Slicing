"""Utilities for manipulating lists."""


from ctypes import set_last_error


def head(input_list):
    first = input_list[0]
    # return first
    """Return the first item of the input list.
    
    For example:

      >>> head(['Jan', 'Feb', 'Mar'])
      'Jan'
    """

    return None


def tail(input_list):
    # new_list = input_list.slice(0,1)
    new_list = input_list[1:]
    # return new_list
    
    """Return a new list of all items, excluding the first item.

    For example:

    >>> tail(['Jan', 'Feb', 'Mar'])
    ['Feb', 'Mar']

    """

    return []


def last(input_list):
    # last_item = input_list.pop()
    last_item = input_list[-1]
    return last_item
    """Return the last item of the input list.

    For example:

    >>> last(['Jan', 'Feb', 'Mar'])
    'Mar'

    """

    return []

top = ['Jan', 'Feb', 'Mar']
def top(input_list):
    last = input_list[:-1]
    return last 
    """Return all elements of the input list except the last.

    For example:

    >>> top(['Jan', 'Feb', 'Mar'])
    ['Jan', 'Feb']

    """

    return []


def first_three(input_list):
    three_elements = input_list[0:3]
    return three_elements
    # return three_elements

        
    """Return the first three elements of the input list.

    For example:

    >>> first_three(['Jan', 'Feb', 'Mar', 'Apr', 'May'])
    ['Jan', 'Feb', 'Mar']

    """

    return []


def last_five(input_list):
    slice = input_list[-5:]
    # return slice
    

    """Return the last five elements of the input list.

    For example:

    >>> last_five([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
    [15, 18, 21, 24, 27]

    """

    return []


def middle(input_list):
    input_list[0:2]
    input_list[-1:-3]

    """Return all elements of input_list except the first two and the last two.

    For example:

    >>> middle([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
    [6, 9, 12, 15, 18, 21]

    """

    return []


def inner_four(input_list):
    innerfour = input_list[2:6]
    return innerfour
    # newArray = []
    
    # third = input_list[2]
    # newArray.append(third)

    # fourth = input_list[3]
    # newArray.append(fourth)

    # sixth = input_list[5]
    # newArray.append(sixth)

    # return newArray


    """Return the third, fourth, fifth, and sixth elements of input_list.

    For example:

    >>> inner_four([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
    [6, 9, 12, 15]
    """

    return []
    


def inner_four_end(input_list):
    fourend = input_list[-6:-2]
    return fourend
    # arr = []
    
    # sixth = input_list[-6]
    # arr.append(sixth)

    # fifth = input_list[-5]
    # arr.append(fifth)

    # fourth = input_list[-4]
    # arr.append(fourth)

    # third = input_list[-3]
    # arr.append(third)

    # return arr



    """Return the elements that are 6th, 5th, 4th, and 3rd from the end of input_list.

    This function should return those elements in a list, in the exact order
    described above.

    For example:

    >>> inner_four_end([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
    [12, 15, 18, 21]

    """

    return []


def replace_head(input_list):
    input_list.insert(0, '42')
    """Replace the head of input_list with the value 42 and return nothing.

    For example:

    >>> multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    >>> replace_head(multiples)
    >>> multiples == [42, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    True

    """

    pass


def replace_third_and_last(input_list):
    a = input_list.insert(2, '37')
    b = input_list.insert(-1, '37')
    """Replace third and last elements of input_list with 37 and return nothing.

    For example:

    >>> multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    >>> replace_third_and_last(multiples)
    >>> multiples == [0, 3, 37, 9, 12, 15, 18, 21, 24, 37]
    True

    """

    pass


def replace_middle(input_list):
    del input_list[2:-2]
    input_list.inseert(2, '42')
    input_list.insert(3, '37')
    """Replace all elements of a list but the first two and last two with 42 and 37.

    After the replacement, 42 and 37 should appear in that order in input_list.

    Return nothing.

    For example:

    >>> multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    >>> replace_middle(multiples)
    >>> multiples == [0, 3, 42, 37, 24, 27]
    True

    """

    pass


def delete_third_and_seventh(input_list):
    del input_list[2]
    del input_list[6]
    """Remove third and seventh elements of input_list and return nothing.

    For example:

    >>> notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
    >>> delete_third_and_seventh(notes)
    >>> notes == ['Do', 'Re', 'Fa', 'So', 'La', 'Do']
    True

    """

    pass


def delete_middle(input_list):
    del input_list[2:-2]
    """Remove all elements from input_list except the first two and last two.

    Return nothing.

    For example:

    >>> notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
    >>> delete_middle(notes)
    >>> notes == ['Do', 'Re', 'Ti', 'Do']
    True

    """

    pass


# This is the part were we actually run the doctests.

if __name__ == '__main__':
    import doctest

    result = doctest.testmod()
    if result.failed == 0:
        print('ALL TESTS PASSED')
