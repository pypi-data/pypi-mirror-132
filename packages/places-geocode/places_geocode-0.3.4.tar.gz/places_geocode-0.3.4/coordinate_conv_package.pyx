# noinspection PyTypeChecker
cpdef list coords_conv(list coordinates):
    """convert coordinates to lats and longs"""

    # create containers for lats and longs
    cdef list lats = []
    cdef list longs = []

    # separate the latitudes and longitudes
    [(lats.append(i[0]), longs.append(i[1])) for i in coordinates]

    return [lats, longs]