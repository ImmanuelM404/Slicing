from typing import Counter
from list_operations import *


def custom_len(input_list):
    """Return number of items in the list.

    The function custom_len(input_list) should have
    the same functionality and result as len(input_list).

    For example:

        >>> custom_len(['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do'])
        8

    """
  
    customLen = len(input_list)
    return customLen
print(custom_len(['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do', 'We','The']))

#---------------------------------------------------------------------------------
# For the next four exercises, you'll need to be clever and think about ways
# to use list slice assignment.
#
# NOTE: these are especially contrived. You wouldn't really want
# to typically append things to a list like this (you'd want to to use the
# list.append() method), but we want you to practice list slicing assignment
# in different ways so it sticks in your brain.


def custom_append(input_list, value):
    """Add the value to the end of the list.

    The function custom_append(input_list, value) should have the same
    functionality as input_list.append(value) where value is added to the
    end of the list and the function returns nothing.

    For example:

        >>> notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
        >>> custom_append(notes, 'Re')
        >>> notes == ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do', 'Re']
        True

    """
    new = input_list + [value]
    # Remember: + creates a new list and leaves the original unchanged
    
    #pass
    return new
notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
print(custom_append(notes, 'Re'))

#----------------------------------------------------------------------------------------------------
def custom_extend(input_list, second_list):
    """Append every item in second_list to input_list.

    Like input_list.extend(second_list), custom_extend(input_list, second_list)
    should append every item in the second list to the end of the first list
    and return nothing.

    For example:

        >>> months = ['Jan', 'Feb', 'Mar']
        >>> custom_extend(months, ['Apr', 'May'])
        >>> months == ['Jan', 'Feb', 'Mar', 'Apr', 'May']
        True

    """
    extend = input_list + second_list

    return extend

    # pass
months = ['Jan', 'Feb', 'Mar']
print(custom_extend(months, ['Apr', 'May']))

#-----------------------------------------------------------------------------------
def custom_insert(input_list, index, value):
    """Insert value at index in the list.

    Like input_list.insert(index, value), should insert (not replace) the value
    at the specified index of the input list and return nothing.

    For example:

        >>> months = ['Jan', 'Mar']
        >>> custom_insert(months, 1, 'Feb')
        >>> months == ['Jan', 'Feb', 'Mar']
        True

    """
   
    return input_list[:index] + [value] + input_list[index:]
    
    
    
    # pass
months = ['Jan', 'Mar']
print(custom_insert(months, 1, 'Feb'))

def custom_remove(input_list, value):
    """Remove the first item of the value in list.

    The function custom_remove(input_list, value) should have the same
    functionality as input_list.remove(value) where the first item of
    the value specified is removed and the function returns nothing.

    For example:

        >>> notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
        >>> custom_remove(notes, 'Do')
        >>> notes == ['Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
        True

    """
    
     
    list = 0 

    for values in input_list:
        if values == value:
            input_list[list:list + 1] = []
            break
        list += 1
    
    
    pass
notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
print(custom_remove(notes, 'Mi'))
print(notes == ['Do', 'Re', 'Fa', 'So', 'La', 'Ti', 'Do'])

  
def custom_pop(input_list):
    """Remove the last item in the list and returns it.

    The function custom_pop(input_list) should have the same functionality
    and result as input_list.pop().

    For example:

        >>> months = ['Jan', 'Feb', 'March']
        >>> custom_pop(months)
        'March'
        >>> months
        ['Jan', 'Feb']

    """
    last = input_list[-1]
    input_list = []
    return last
months = ['Jan', 'Feb', 'March']  
print(custom_pop(months))


def custom_index(input_list, value):
    """Return the index of the first item of value found in input_list.

    The function custom_index(input_list, value) should have the same
    functionality and result as input_list.index(value).

    For example:

        >>> custom_index(['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do'], 'Re')
        1

    """

    counter = 0

    for values in input_list:
        if values == value:
            return counter

        counter += 1
print(custom_index(['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do'], 'Do'))

def custom_count(input_list, value):
    """Return the number of times value appears in the list.

    Like input_list.count(value), custom_count(input_list, value) should
    return the number of times the specified value appears in the list.

    For example:

        >>> custom_count(['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do'], 'Do')
        2

    """
    counter = 0

    for values in input_list:
        if values == value:
            counter += 1
    return counter 
print(custom_count(['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do'], 'Do'))

def custom_reverse(input_list):
    """Reverse the elements of the input_list.

    Like input_list.reverse(), custom_reverse(input_list) should reverse the
    elements of the original list and return nothing (we call this reversing
    "in place").

    For example:

        >>> multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
        >>> custom_reverse(multiples)
        >>> multiples == [27, 24, 21, 18, 15, 12, 9, 6, 3, 0]
        True

    """
#11111111111111111111111111111111111111111111111111111111111111111111111111111111111111

def custom_contains(input_list, value):
    """Return True or False if value is in the input_list.

    Like (value in input_list), should return True if the list contains the
    specified value and False if it does not. Remember, do not use the `if X in Y`
    statement -- find another way to solve it!

    For example:

        >>> custom_contains([0, 3, 6, 9, 12, 15, 18, 21, 24], 23)
        False

        >>> custom_contains([0, 3, 6, 9, 12, 15, 18, 21, 24], 24)
        True

    """
    for values in input_list:
        if values == value:
            return True
    return False
print(custom_contains([0, 3, 6, 9, 12, 15, 18, 21, 24], 23))
print(custom_contains([0, 3, 6, 9, 12, 15, 18, 21, 24], 24))

def custom_equality(some_list, another_list):
    """Return True if passed lists are identical, False otherwise.

    Like (some_list == another_list), custom_equality(some_list, another_list)
    should return True if both lists contain the same values in the same indexes.

    For example:

        >>> custom_equality(['Jan', 'Feb', 'Mar'], ['Jan', 'Feb', 'Mar'])
        True

        >>> custom_equality(['Jan', 'Feb', 'Mar'], ['Jan', 'Mar', 'Feb'])
        False

    """

    if custom_len(some_list) != custom_len(another_list):
        return False

    else:
        for i in range(len(some_list)):
            if some_list[i] != another_list[i]:
                return False
        return True


print(custom_equality(['Jan', 'Feb', 'Mar'], ['Jan', 'Feb', 'Mar']))
print(custom_equality(['Jan', 'Feb', 'Mar'], ['Jan', 'Mar', 'Feb']))
