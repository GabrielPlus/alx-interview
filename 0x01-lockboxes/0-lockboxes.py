#!/usr/bin/python3
def canUnlockAll(boxes):
    num_boxes = len(boxes)
    unlocked_boxes = [False] * num_boxes
    unlocked_boxes[0] = True  # The first box is unlocked

    # Use a stack to keep track of the boxes to explore
    stack = [0]  # Start with the first box

    while stack:
        current_box = stack.pop()

        # Check each key in the current box
        for key in boxes[current_box]:
            if key < num_boxes and not unlocked_boxes[key]:
                unlocked_boxes[key] = True
                stack.append(key)

    # Check if all boxes are unlocked
    return all(unlocked_boxes)

