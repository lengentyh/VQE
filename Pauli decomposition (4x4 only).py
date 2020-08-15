# decomposition of Hamiltonian (4x4 only)
from numpy import*
from numpy import array
from numpy import tensordot
import math
j = complex(0,1)

#Pauli matrices
#and their symbols
I = array(([1,0],[0,1]))
X = array(([0,1],[1,0]))
Y = array(([0,-j],[j,0]))
Z = array(([1,0],[0,-1]))
P = [I,X,Y,Z]
SP = ['I','X','Y','Z']

h,m = 1, 1  #h ,m = 1.054*10**-34, 9.109*10**-31
k = 9  #k = 9*m #variable
a = 1  #lattice constant
n = 2  #number of qubits
N = 2**n

#T = h^2 / 2m * (dx)^2
dx = a/N 
T = complex( -((h**2)/(2*m))/((dx)**2), 0 )

#asign elements of H and V 
H = zeros((N,N), dtype = complex)
for i in range(N):
    V = (k/2) * ( (i*dx - a/2)**2 )
    for j in range(N):
        if i == j-1 : H[i][j] = T*1 
        if i == j+1 : H[i][j] = T*1 
        if i == j : H[i][j] = T*-2 + V
        
H[0][N-1] = T*1 
H[N-1][0] = T*1

threshold = 0.01*abs(T)

coefficients = []
for i in range(4):
    for j in range(4):
        c = (1/N)*trace( matmul( H,kron(P[i],P[j]) ))
        if abs(c) >= threshold:
            coefficients.append([i,j,";",c]) #四進位 get position etc...
            print(SP[i],SP[j],":",c)
print(H)        
print(coefficients)
print("The END")
