cimport cython

ctypedef fused my_fused_type:
    cython.list
    cython.str

# noinspection PyTypeChecker
cpdef list is_duplicates(list edges_arr):
    """
    :param edges_arr: 
    :return: bint duplicate + exact dup edges
    """

    cdef list duplicates = []
    cdef list i = []
    cdef list item = []
    cdef bint dup_counter = False

    cdef list refined_edges = [str(i) for i in edges_arr]

    for edge in refined_edges:
        if refined_edges.count(edge) > 1:
            dup_counter = True
            duplicates.append(edge)

    if dup_counter:
        return [True, duplicates]
    else:
        return [False, duplicates]