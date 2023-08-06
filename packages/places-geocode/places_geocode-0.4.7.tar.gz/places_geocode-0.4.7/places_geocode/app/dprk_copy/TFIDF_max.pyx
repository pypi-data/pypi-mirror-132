from difflib import SequenceMatcher


"""TFIDF algorithm implementation Cython"""
cpdef list find_max_similarity(str street_query, result):

    """
    :param street_query: street to be compared to
    :param result: general query output 
    :return: maximum accuracy achieved, JSON of result, street: str
    """

    cdef float current_max = 0.0
    cdef dict current_max_result = {}
    cdef dict street_comparison = {}
    cdef float similarity = 0.0

    for street_comparison in result:
        similarity = float(SequenceMatcher(None, street_query.lower(),
                                     street_comparison['properties']['street'].lower()).ratio())

        if similarity > current_max:
            current_max = similarity
            current_max_result = street_comparison
        else:
            continue

    return [round(current_max, 2), current_max_result, current_max_result['properties']['street']]