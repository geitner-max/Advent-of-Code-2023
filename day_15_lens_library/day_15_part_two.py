
__author__ = "Maximilian Geitner"
__date__ = "15.12.2023"

def hash_value(label_input):
    current_value = 0
    for char_inner in label_input:
        val = ord(char_inner)
        current_value = ((current_value + val) * 17 % 256)
    return current_value

def remove_label(boxes, label_input):
    hash_val = hash_value(label_input)
    selected_box = boxes[hash_val]
    new_box = []
    for label, focal_length in selected_box:
        if label == label_input:
            # remove from box
            pass
        else:
            new_box.append((label, focal_length))
    boxes[hash_val] = new_box
    return boxes

def replace_if_exists(boxes, label_input, focal_length_input):
    hash_val = hash_value(label_input)
    selected_box = boxes[hash_val]
    new_box = []
    box_added = False
    for label, focal_length in selected_box:
        if label == label_input:
            new_box.append((label_input, focal_length_input))
            box_added = True
        else:
            new_box.append((label, focal_length))
    if not box_added:
        new_box.append((label_input, focal_length_input))
    boxes[hash_val] = new_box
    return boxes
if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"


    with open(filename) as file:
        # dash (-) : remove lens from box
        # If the operation character is an equals sign (=), it will be followed by a number indicating the focal length of the lens that needs to go into the relevant box
        # If there is already a lens in the box with the same label, replace the old lens with the new lens
        # If there is not already a lens in the box with the same label, add the lens to the box immediately behind any lenses already in the box.
        boxes = [[]] * 256
        for line in file:
            line = line.replace("\n", "")

            steps = line.split(",")

            for step in steps:
                label = ""
                state = 0
                for char in step:
                    if char == '-':
                        # remove label
                        boxes = remove_label(boxes, label)
                    elif char == '=':
                        state = 1
                    else:
                        if state == 0:
                            label += char
                        else:
                            # retrieve focal length
                            focal_length = int(char)
                            # look for lens with same label
                            boxes = replace_if_exists(boxes, label, focal_length)
        total = 0

        for index in range(256):
           value_box = index + 1
           for index_slot, val in enumerate(boxes[index]):
               label, focal_len = val
               total += (value_box * (index_slot + 1) * focal_len)
        print("Solution Day 15 Part Two", total)
