def ft_filter(myFunction, iterable):
    """
    ft_filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    """
    if myFunction is None:
        myFunction = bool
    return (i for i in iterable if myFunction(i))

# ages = [5, 12, 17, 18, 24, 32]

# def myFunc(x):
#   if x < 18:
#     return False
#   else:
#     return True


# adults = filter(myFunc, ages)

# for x in adults:
#   print(x)