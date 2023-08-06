"""handle null parameters and maximize accuracy"""
cpdef minimize_nulls(list original, list new_arr):

    """minimize the nulls present in final array with stack data structure"""

    cdef list optimized_original = [original[0]]
    cdef int i = 0

    for i in range(1, len(original)):
        if new_arr[i] == '':
            optimized_original.append(original[i])
        else:
            optimized_original.append(new_arr[i])

    return optimized_original