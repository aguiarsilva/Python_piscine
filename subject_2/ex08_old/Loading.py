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

    # get the terminal size using get_terminal_size
    try:
        cols = os.get_terminal_size().columns
    except OSError:
        cols = 80

    bar_width = max(10, cols - 40)

    # start the timer
    try:
        start = os.clock_gettime(os.CLOCK_MONOTONIC)
    except AttributeError:
        start = os.times()[4]

    try:
        for i, item in enumerate(lst, 1):
            yield item

            percentage = i / total
            pct_display = int(percentage * 100)

            # calculate time executing activity
            try:
                now = os.clock_gettime(os.CLOCK_MONOTONIC)
            except AttributeError:
                now = os.times()[4]
            elapsed_time = now - start

            # calculate the speed and the remaining time for the activity
            if elapsed_time > 0:
                speed = i / elapsed_time
                remaining_time = (total - i) / speed
            else:
                speed = 0.0
                remaining_time = 0.0

            # make progress bar
            filled = int(bar_width * percentage)
            bar = '█' * filled + ' ' * (bar_width - filled)

            elapsed_str = format_time(elapsed_time)
            remaining_str = format_time(remaining_time)

            if speed > 99.95:
                speed_str = f'{round(speed)}it/s'
            elif speed > 0:
                speed_str = f'{speed:.2f}it/s'
            else:
                speed_str = f'{speed:.0f}it/s'

            output = (f'\r{pct_display:3d}%|{bar}| {i}/{total} '
                      f'[{elapsed_str}<{remaining_str}, {speed_str}]')

            print(output, end='', flush=True)
    finally:
        print()


def format_time(seconds):
    """
    Format the time as MM:SS or HH:MM:SS
    """
    if seconds < 0:
        seconds = 0
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    if hours > 0:
        return f'{hours:02d}:{minutes:02d}:{secs:02d}'
    return f'{minutes:02d}:{secs:02d}'
