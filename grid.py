import numpy as np
from itertools import zip_longest
from transformation import transpose, mirror, rotate



"""GRID 1"""

def ABC():
    ABCList = []
    A = "_|"
    ABCList.append(A)
    B = "|_|"
    ABCList.append(B)
    C = mirror(A)
    ABCList.append(C)
    ABCArray = np.array(ABCList)
    return ABCArray
#print(ABC())

def DEF():
    DEFList = []
    D = "x|"
    DEFList.append(D)
    E = "|x|"
    DEFList.append(E)
    F = mirror(D)
    DEFList.append(F)
    DEFArray = np.array(DEFList)
    return DEFArray
#print(DEF())    

def GHI():
    GHIList = []
    G = chr(8254) + "|"
    GHIList.append(G)
    H = "|" + chr(8254) + "|"
    GHIList.append(H)
    I = mirror(G)
    GHIList.append(I)
    GHIArray = np.array(GHIList)
    return GHIArray
#print(GHI())



"""GRID 2"""

def JKL():
    JKLList = []
    J = "_.|"
    JKLList.append(J)
    K = "|._.|"
    JKLList.append(K)
    L = mirror(J)
    JKLList.append(L)
    JKLArray = np.array(JKLList)
    return JKLArray
#print(JKL())

def MNO():
    MNOList = []
    M = "x.|"
    MNOList.append(M)
    N = "|.x.|"
    MNOList.append(N)
    O = mirror(M)
    MNOList.append(O)
    MNOArray = np.array(MNOList)
    return MNOArray
#print(MNO())

def PQR():
    PQRList = []
    P = chr(8254) + ".|"
    PQRList.append(P)
    Q = "|." + chr(8254) + ".|"
    PQRList.append(Q)
    R = mirror(P)
    PQRList.append(R)
    PQRArray = np.array(PQRList)
    return PQRArray
#print(PQR())



"""GRID 3"""

def STUV():
    STUVList = []
    S = "\/"
    STUVList.append(S)
    T = "//"
    STUVList.append(T)
    U = mirror(S)
    STUVList.append(U)
    V = "\\"
    STUVList.append(V)
    STUVArray = np.array(STUVList)
    return STUVArray
#print(STUV())



"""GRID 4"""

def WXYZ():
    WXYZList = []
    W = "\./"
    WXYZList.append(W)
    X = "//.."
    WXYZList.append(X)
    Y = mirror(W)
    WXYZList.append(Y)
    Z = "..\\"
    WXYZList.append(Z)
    WXYZArray = np.array(WXYZList)
    return WXYZArray
#print(WXYZ())














#build functions to get arrays
#build dictionarys to access parts of certain arrays

#print(chr(8254))
#print("test")
#print("_" + chr(8254))

#when implementation of the four utilized grids is complete, convert each grid to 
#array, allowing for easy access to each 'letter' from the designated array




