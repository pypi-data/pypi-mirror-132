import csv

cpdef write_csv(int filename, int mode, list results):
    cdef const char *fieldnames[3]
    fieldnames[:3] = ['address', 'latitude', 'longitude']
    cdef list result = []
    cdef list data = []
    cdef dict d = {}
    cdef list coordinates = []

    with open(filename, mode) as csvfile:
        csvfile.truncate()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for result in results:
            data = result[0]
            for d in data:
                coordinates = d['coordinates']
                writer.writerow({'address': d['formatted_address'], 'latitude': d['coordinates'][0],
                                 'longitude': coordinates[1]})