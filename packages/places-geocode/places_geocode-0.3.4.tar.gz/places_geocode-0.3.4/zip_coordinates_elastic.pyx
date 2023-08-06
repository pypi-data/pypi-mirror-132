"""create elasticsearch coordinate set for search"""

cimport cython

ctypedef fused value_type:
    cython.int
    cython.double
    cython.str

# noinspection PyMissingOrEmptyDocstring
cpdef list coordinate_zipped(list latitudes, list longitudes, bint reverse_param):

    """Cython/C function for handling long list of zipped coordinates"""

    cdef list coordinates = []
    cdef int i = 0
    cdef str coordinate = ''

    if reverse_param:
        for i in range(len(latitudes)):
            coordinate = '{}, {}'.format(latitudes[i],longitudes[i])
            coordinates.append(coordinate)
    else:
        for i in range(len(latitudes)):
            coordinate = '{}, {}'.format(longitudes[i], latitudes[i])
            coordinates.append(coordinate)

    return coordinates


