"""create the radius array for batch reverse processing"""

cimport cython

ctypedef fused my_fused_type:
    cython.int
    cython.double

cpdef list construct_radius_arr(my_fused_type radius, int iterations):
    """create the radius array using a fused type"""
    return [radius for _ in range(iterations)]