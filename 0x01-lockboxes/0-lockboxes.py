#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes: A list of lists representing locked boxes and their keys.

    Returns:
        True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    keys = set(boxes[0])
    unlocked = {0}

    while keys:
        key = keys.pop()
        if key < len(boxes) and key not in unlocked:
            keys.update(boxes[key])
            unlocked.add(key)

    return len(unlocked) == len(boxes)
