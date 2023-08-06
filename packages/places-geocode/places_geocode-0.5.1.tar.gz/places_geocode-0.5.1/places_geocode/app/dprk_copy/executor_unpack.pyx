# noinspection PyTypeChecker
cpdef dict executor_read(list results):
    cdef dict response_packet = {'response_packet': [], 'supplied_packet': []}
    cdef dict result = {}

    for result in results:
        response_packet['response_packet'].extend(result['response_packet'])
        response_packet['supplied_packet'].extend(result['supplied_packet'])

    return response_packet


