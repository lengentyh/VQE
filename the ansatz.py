#the ansatz
#n = 2 the number of qubit
layer = 4
def get_var_wavfnt(qc,params):
    #|ψ>=U|0>
    for j in range(layer):
        for i in range(n):
            qc.h(i)
        for i in range(n-1):
            qc.cz(i+1,i)
        for i in range(n):
            qc.rx(params[j*n+i],i)       
    return qc
