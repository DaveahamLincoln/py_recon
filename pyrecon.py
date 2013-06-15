#py_recon CSV Reconciliation Tool v1.0b
#
#developed by Dave Nearing III, Temporary Agent, 06/14/13
#source code hosted at https://github.com/DaveahamLincoln/py_recon
#Use by parties other than FRCC employees is restricted without prior consent granted by the FRCC Controller

import sys
from parser import *
from compdict import *

def main(args):
    AParser = parser(sys.argv[1])
    BParser = parser(sys.argv[2])
    A = AParser.parse()
    B = BParser.parse()
    CompDict = compdict(A,B)
    C = CompDict.compare()
    #print(C)
    
if __name__ == "__main__":
    main(sys.argv)