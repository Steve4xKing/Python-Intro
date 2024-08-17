def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

    true_lst = []
    for item in lst:
        if item == False or item == None or item == '' or item == [] or item == ():
            continue #continue seems like it can be very useful
        else:
            true_lst.append(item)

    return true_lst

# print(compact([0, 1, 2, '', [], False, (), None, 'All done']))