import datetime
starttime = datetime.datetime.now()

import numpy as np
import scipy.linalg as la

A = np.array([[17.125,-8,0,-8],[-8,16.2815,-8,0],[0,-8,16,-8],[-8,0,-8,16.28125]])
print(la.eig(A)[0])

endtime = datetime.datetime.now()
print ("total time used",endtime - starttime)
