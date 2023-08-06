from difflib import SequenceMatcher
from bson import BSON

# noinspection PyTypeChecker,PyArgumentEqualDefault
cpdef list find_similar_components(str street, str region, str city, result):

    """find the most similar address components using the extension to the TFIDF-ML algorithm"""

    cdef float current_max_street = 0.0
    cdef float current_max_region = 0.0
    cdef float current_max_city = 0.0
    cdef dict current_max_result = {'street': None, 'city': None, 'region': None}
    cdef dict street_comparison = {}
    cdef float similarity_street = 0.0
    cdef float similarity_region = 0.0
    cdef float similarity_city = 0.0

    cdef dict property_components = {}

    for document in result:

        document = document['properties']

        # find similarities
        similarity_street = float(SequenceMatcher(None, street.lower(),
                                           document['street'].lower()).ratio())

        similarity_city = float(SequenceMatcher(None, street.lower(),
                                           document['city'].lower()).ratio())

        similarity_region = float(SequenceMatcher(None, street.lower(),
                                                document['region'].lower()).ratio())

        if similarity_street > current_max_street:
            current_max_street = similarity_street
            current_max_result['street'] = document

        if similarity_city > current_max_city:
            current_max_city = similarity_city
            current_max_result['city'] = document

        if similarity_region > current_max_region:
            current_max_region = similarity_region
            current_max_result['region'] = document

    return [
        [round(current_max_street, 2), current_max_result['street'], current_max_result['street']],
        [round(current_max_city, 2), current_max_result['city'], current_max_result['city']],
        [round(current_max_region, 2), current_max_result['region'], current_max_result['region']]
    ]
