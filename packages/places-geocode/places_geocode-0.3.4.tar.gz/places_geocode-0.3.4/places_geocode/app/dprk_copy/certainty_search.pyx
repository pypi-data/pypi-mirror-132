"""throttle confidence mapping code"""

# noinspection PyTypeChecker
cpdef float confidence_map(dict scale, list index, float distance):

    """map the confidence to a certainty value"""

    # define array length
    cdef int length = len(index)
    cdef int i = 0
    cdef list stack = []
    cdef float confidence = 0.0

    # loop through array and add to stack if condition satisfied
    for i in range(1, length + 1):
        # if distance is larger than the previous index item, add to stack
        if distance >= index[i - 1]:
            # insert in stack
            stack.append(scale[index[i]])
        else:
            continue

    # pop from the stack first
    try:
        confidence = stack.pop()
    # if stack is empty, it means it is the most accurate 1.0 mapping
    except IndexError:
        # return the mapping
        confidence = scale[index[0]]

    return confidence