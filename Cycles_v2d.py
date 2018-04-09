import numpy as np


def Cycles(ListS):
    List = np.copy(ListS)
    i = 0
    t = []
    while i < List.shape[0]:
        #print(i, List[i])
        if List[i] < 0:
            i += 1
        else:
            t2 = [i]
            while List[i] > -1:
                t2 = np.insert(t2, -0, List[i])
                i1 = i
                i = List[i1]
                List[i1] = -1
            t.append(np.delete(t2, -1))
    return t


def unRiffleS(n):
    return np.concatenate((np.arange(0, 2*n, 2), np.arange(1, 2*n, 2)))


def CountCycles(Cyc):
    lc = []
    for x in Cyc:
        lc.append(x.shape[0])
    return np.array(lc)


def CheckRiffle(CyLi, Rnum):
    if np.any(CyLi == Rnum):
        if np.any(Rnum % CyLi != 0):
            return False
        else:
            print(CyLi.sum())
            return True
    else:
        return False


def CR(n, Rnum):
    return CheckRiffle(CountCycles(Cycles(unRiffleS(n))), Rnum)


def Smr(m, r):
    return (1-r**(m+1))/(1-r)


def Fmr(m, r):
    return int(r**m-Smr(m-2, r))


def RiffleSumP(rn, l):
    s1 = 0
    for i in range(1, l):
        if CR(i, rn):
            s1 += 2*i
    return s1


def RiffleSumT(rn):
    return RiffleSumP(rn, Fmr(rn, 2))
