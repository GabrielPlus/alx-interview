#!/usr/bin/python3
canUnlockAll = __import__('0-lockboxes').canUnlockAll

# Example usage
boxes = [[1], [2], [3], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 2], [3], [4], [0], []]
print(canUnlockAll(boxes))  # Output: False

