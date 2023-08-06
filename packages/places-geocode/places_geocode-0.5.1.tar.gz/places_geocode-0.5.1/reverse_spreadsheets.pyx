import csv

cpdef spread_write(list arr, str filename, str mode):
    cdef const char *fieldnames[3]
    fieldnames[:9] = ['latitude', 'longitude', 'address', 'number', 'street', 'city', 'postcode', 'region', 'validation']
    cdef float latitude = 0.0
    cdef float longitude = 0.0
    cdef dict packet = {}
    cdef str formatted_address = ''
    cdef bint address_val = True
    cdef dict row_keys = {}

    with open(filename, mode) as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for packet in arr:
            formatted_address = packet['formatted_address']
            latitude, longitude = packet['coordinate'][0], packet['coordinate'][1]
            row_keys = {'address': formatted_address, 'latitude': latitude, 'longitude': longitude}
            row_keys.extend(packet['address_parts'])

            writer.writerow(row_keys)