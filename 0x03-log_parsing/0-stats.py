#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
"""
import sys
import signal
import re


total_file_size = 0
status_code_counts = {
    200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
}
line_count = 0


def signal_handler(sig, frame):
    """Handle SIGINT signal by printing statistics and exiting."""
    print_stats()
    sys.exit(0)


def print_stats():
    """Print file size and status code counts."""
    print("File size: {}".format(total_file_size))
    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print("{}: {}".format(code, count))


def process_line(line):
    """Process a single line of input."""
    global total_file_size, status_code_counts, line_count
    line_count += 1
    match = re.match(
        r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] '
        r'"GET /projects/260 HTTP/1.1" (\d+) (\d+)$',
        line
    )
    if match:
        status_code = int(match.group(3))
        file_size = int(match.group(4))

        total_file_size += file_size

        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        if line_count % 10 == 0:
            print_stats()
            line_count = 0


def main():
    """Main function to handle input processing."""
    signal.signal(signal.SIGINT, signal_handler)

    for line in sys.stdin:
        process_line(line.strip())


if __name__ == "__main__":
    main()
