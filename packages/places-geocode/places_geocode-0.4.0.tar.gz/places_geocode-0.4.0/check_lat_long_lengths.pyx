"""Cython function for checking incorrect lat, long scenarios"""

cpdef bint check_lat_long(list latitudes, list longitudes, int maximum):
    """check if lat long are the same length"""

    cdef bint counter = False
    cdef int coord_length = len(latitudes)

    if len(latitudes) == len(longitudes):
        if coord_length <= maximum:
            counter = True

    return counter



