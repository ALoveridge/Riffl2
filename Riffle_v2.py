import numpy as np


class Deck():

    def __init__(self, n):
        self.size = n
        self.show = np.arange(2*n)

    def unriffle(self):
        self.show = np.concatenate((self.show[::2], self.show[1::2]), axis=0)

    def riffle(self):
        self.show = np.vstack((
                self.show[:self.size],
                self.show[self.size:])).reshape((-1), order='F')

    def check(self):
        return np.all(self.show[:-1] <= self.show[1:])

    def countr(self):
        i = 1
        self.riffle()
        while self.check() == False:
            i += 1
            self.riffle()
        return i


def Smr(m, r):
    return (1-r**(m+1))/(1-r)


def Fmr(m, r):
    return int(r**m-Smr(m-2, r))


def listv(l):
    for i in range(1, l):
        print(2*i, Deck(i).countr())


def countv(rn, l):
    s1 = 0
    for i in range(1, l):
        if Deck(i).countr() == rn:
            s1 += 2*i
            print(2*i, Deck(i).countr())
    print('The total sum is', s1)


# Sum of the values of n which have 8 riffles as the identity shuffle
countv(8, Fmr(8, 2))
