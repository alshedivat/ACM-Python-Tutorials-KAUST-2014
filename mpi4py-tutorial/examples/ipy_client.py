#!/usr/bin/env ipython
from IPython.parallel import Client
rc = Client()
view = rc[:]
view.activate()
view.execute('from mpi4py import MPI')
