#!/usr/bin/python3
def safe_print_integer(value):
    """ Print an integer with "{:d}.format().
    value - integer to be printed
    Returns:
        if TypeError or ValueError occurs - False
        else - True
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (ValueError, TypeError):
        return (False)
