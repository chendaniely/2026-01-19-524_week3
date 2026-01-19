def count_char(input_string):
    """
    Count the number of characters in a string.

    Parameters
    ----------
    input_string : str
        The string to count characters from.

    Returns
    -------
    int
        The number of characters in the input string.

    Raises
    ------
    TypeError
        If input_string is not of type str.

    Examples
    --------
    >>> count_char("hello")
    5
    >>> count_char("")
    0
    >>> count_char("hello world")
    11
    """

    #breakpoint() #browser()
    print(input_string)


    if not isinstance(input_string, str):
        raise TypeError(f"Expected the input to be of type str, got {type(input_string)}")

    #return len(input_string)
    count = 0
    for char in input_string:
        count += 1
    return count
