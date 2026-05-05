def ft_filter(func, iterable):
    """
    Return an iterator yielding those items of iterable for which \
            function(item) is true.
    If the function is None, return the items that are true.
    """
    if func is None:
        return iter([item for item in iterable if bool(item)])
    else:
        return iter([item for item in iterable if func(item)])
