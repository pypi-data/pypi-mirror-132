
cpdef create_packet(dict address_components, str formatted_address, list coordinate, str certainty, float accuracy, bint address_val):
    """
    :param address_val:
    :param accuracy:
    :param certainty:
    :param address_components:
    :param formatted_address: 
    :param coordinate: 
    :return: 
    """

    cdef dict inner_data_packet = {}

    inner_data_packet = {'address_parts': address_components,
                         'certainty': certainty,
                         'coordinate': coordinate,
                         'formatted_address': formatted_address,
                         'accuracy': accuracy,
                         'address_validation': address_val}

    return inner_data_packet