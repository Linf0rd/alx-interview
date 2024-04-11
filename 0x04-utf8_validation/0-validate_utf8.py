#!/usr/bin/python3
"""
Method that determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    Args:
        data: A list of integers representing the data set

    Returns:
        True if data is a valid UTF-8 encoding, else False
    """
    num_bytes = 0
    for num in data:
        if num_bytes == 0:
            if (num >> 3) == 0b11110:
                num_bytes = 3
            elif (num >> 4) == 0b1110:
                num_bytes = 2
            elif (num >> 5) == 0b110:
                num_bytes = 1
            elif (num >> 7) == 0b0:
                num_bytes = 0
            else:
                return False
        else:
            if (num >> 6) != 0b10:
                return False
            num_bytes -= 1
    return num_bytes == 0


if __name__ == "__main__":
    data1 = [65]
    print(validUTF8(data1))

    data2 = [
      80, 121, 116, 104, 111, 110, 32,
      105, 115, 32, 99, 111, 111, 108, 33
    ]
    print(validUTF8(data2))

    data3 = [229, 65, 127, 256]
    print(validUTF8(data3))
