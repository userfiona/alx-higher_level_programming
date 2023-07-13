#!/usr/bin/python3
"""
Reads from standard input and computes metrics.
After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""

import sys


def print_stats(size, status_codes):
    """Print accumulated metrics.
    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size:", size)
    for code, count in sorted(status_codes.items()):
        print("{}: {}".format(code, count))


if __name__ == "__main__":
    size = 0
    status_codes = {}
    valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

            try:
                _, _, _, code, file_size = line.split()
                size += int(file_size)
                if code in valid_codes:
                    status_codes[code] = status_codes.get(code, 0) + 1
            except (ValueError, IndexError):
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
