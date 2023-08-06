"""create the coordinates for the elastic search polygon instance"""

cpdef list convex_array(list latitudes, list longitudes, bint reverse_param):

    """create convex array (encapsulated) for elasticsearch polygon geoshape query"""

    cdef list coordinates = []

    if reverse_param:
        coordinates = [f"{long}, {lat}" for lat, long in zip(latitudes, longitudes)]
    else:
        coordinates = [f"{lat}, {long}" for lat, long in zip(latitudes, longitudes)]

    return coordinates