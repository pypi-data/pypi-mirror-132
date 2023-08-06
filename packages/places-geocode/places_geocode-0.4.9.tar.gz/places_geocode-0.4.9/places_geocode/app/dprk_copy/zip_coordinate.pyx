# noinspection PyMissingOrEmptyDocstring
cpdef list coordinate_zipped(list latitudes, list longitudes, bint reverse_param):

    """Cython/C function for handling long list of zipped coordinates"""

    cdef float lat = 0.0
    cdef float long = 0.0
    cdef list coordinates = []
    cdef int i = 0

    if reverse_param:
        for i in range(len(latitudes)):
            coordinates.append([longitudes[i], latitudes[i]])
    else:
        for i in range(len(latitudes)):
            coordinates.append([latitudes[i], longitudes[i]])

    return coordinates


