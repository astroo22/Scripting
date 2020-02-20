import struct
import numpy
def mEps64(eps):
    while ((1+eps) !=1):
        prevEp = eps
        eps = eps/2
    print( "Machine Eps is: " , prevEp)
def mEps32(eps2):
    while ((1+eps2) !=1):
        prevEp2 = eps2
        prevEp2 = struct.unpack('f', struct.pack('f', prevEp2))[0]
        eps2 = eps2/2
        eps2 = struct.unpack('f', struct.pack('f', eps2))[0]
    
    print( "Machine Eps 32 is: " , prevEp2)
mEps64(0.5);
mEps32(0.5);
