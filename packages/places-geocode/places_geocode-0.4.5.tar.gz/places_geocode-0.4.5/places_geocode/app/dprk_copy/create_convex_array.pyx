cpdef list convex_array(list latitudes, list longitudes, bint reverse_param):

    """

    :param latitudes: 
    :param longitudes: 
    :param reverse_param: 
    :return: zipped coordinates
    
    """

    cdef list final_coordinates = []
    cdef list coordinates = []

    if reverse_param:
        coordinates = [[long, lat] for lat, long in zip(latitudes, longitudes)]
    else:
        coordinates = [[lat, long] for lat, long in zip(latitudes, longitudes)]

    coordinates.append(coordinates[0])
    final_coordinates.append(coordinates)

    return final_coordinates