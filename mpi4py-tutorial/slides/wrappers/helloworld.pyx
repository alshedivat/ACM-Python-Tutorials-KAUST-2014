# file: helloworld.pyx
from mpi4py.MPI cimport *
from mpi4py.mpi_c cimport *

cdef import from "helloworld.h":
    void c_sayhello"sayhello"(MPI_Comm)

def sayhello(Comm py_comm):
    cdef MPI_Comm c_comm = py_comm.ob_mpi
    c_sayhello(c_comm)
