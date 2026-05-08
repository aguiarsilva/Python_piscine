import os


def ft_tqdm(lst: range) -> None:
    """
    This function copies the behaviour and utility of the tdqm function
    with the yield operator.
    The output expected must be as close as possible to the original function.
    """
    # get total length of the list
    total = len(lst)
    if total == 0:
        return

    # get the terminal get_terminal_size
    try:
        cols = os.get_terminal_size().columns
    except OSError:
        cols = 80

    bar_width = max(10, cols - 40)


