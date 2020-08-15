#main program
get_ipython().run_line_magic('matplotlib', 'inline')
# Importing standard Qiskit libraries and configuring account
from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import *
# Loading your IBM Q account(s)
provider = IBMQ.load_account()


Default_Provider = IBMQ.get_provider(hub='ibm-q-hub-ntu', group='ntu-internal', project='default')
NUM_SHOTS = 4096


#main program 
import datetime
starttime = datetime.datetime.now()

import numpy as np
import math as math
from qiskit.providers.ibmq import least_busy
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import Aer, execute
from qiskit.aqua.components.optimizers import COBYLA, SPSA
from qiskit.extensions.standard import HGate, RXGate, IGate
gates = { 'X': HGate(), 'Y': RXGate(math.pi/2), 'Z': IGate() }


s = size(coefficients,0)
def objective_function(params):
    cost = 0
    qc_list = []
    output_distr = 0
    backend = least_busy(Default_Provider.backends(filters=lambda x: x.configuration().n_qubits >= n*s 
                                       and x.configuration().simulator 
                                       and x.status().operational==True))
    #the circuit
    for i in range(s):
        qc = QuantumCircuit(n, n)
        get_var_wavfnt(qc,params)          
        for m in range(n):
            if SP[ coefficients[i][m] ] != 'I':
                qc.append( gates[SP[ coefficients[i][m] ]], [m])      
                qc.measure(m, m)
        qc_list.append(qc)
        
    transpiled_circs = transpile(qc_list, backend=backend, layout_method='dense')
    qobjs = assemble(transpiled_circs, backend=backend, shots=NUM_SHOTS)
    job_info = backend.run(qobjs)
    
    #calculate the expected values
    for j in range(s):
        counts = job_info.result().get_counts(transpiled_circs[j])
        output_distr = get_probability_distribution(counts)  
        for v in output_distr.keys():
            parity = check_parity(v)
            cost += coefficients[j][n+1].real * output_distr[v] * parity
    return cost

optimizer = COBYLA(maxiter=500, tol=0.0001)
#optimizer = SPSA(max_trials=100)
print("on the half way")
# Create the initial parameters 
num_params = layer*n
params = 2 * math.pi * np.random.rand(int(num_params))
ret = optimizer.optimize(num_vars=num_params, objective_function=objective_function, initial_point=params)

# Obtain the results using the final parameters
eigval = objective_function(ret[0])
print("Obtained eigenvalue:", eigval)
print("Parameters Found:", ret[0])

midtime = datetime.datetime.now()
print ("time used till eigenvalue",midtime - starttime)








