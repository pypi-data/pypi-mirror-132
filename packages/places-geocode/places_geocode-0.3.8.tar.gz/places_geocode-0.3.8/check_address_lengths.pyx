cpdef bint check_batch(list address_array, int maximum):
    """check if address array length is exceeded"""
    cdef bint counter = False

    if len(address_array) > maximum:
        counter = False
    else:
        counter = True

    return counter