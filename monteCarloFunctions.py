
import numpy as np
from random import randint


def getLength(size):
    """
       getLength take as parameter the total wanted size of the network
       and return a length of a square with the nearest dimension to that size.
    """
    l, i = [0 for _ in range(2)]
    while i < size:

        if i**2 == size:
            l = i
            break
        if i**2 < size and (i+1)**2 > size:
            l = i
            break
        i +=1

    return l

def genNetwork(length, maliciousFactor):
    """
       genNetwork take as parameter the length of a 2d array and the % of malicous peer 
       and render a binary 2d array.
       A good Peer is presented by 0, a Maclicous peer is presented by 1
    """
    N = length**2
    K = (maliciousFactor * N)/100
    arr = np.array([1] * K + [0] * (N-K))
    np.random.shuffle(arr)
    arr2d = np.reshape(arr,(length,length))
    print arr2d
    return arr2d

def checkConsensus(arr, poolPos):
    """
       checkConsensus take as parameter the pool to check and the network matrix
       return a bool True if consenesus is reached, False if it is not the case
    """
    pool, blacklisted = [[] for _ in range(2)]
    for i in poolPos:
        pool.append(arr[i[0]][i[1]])
        if arr[i[0]][i[1]] == 1:
            blacklisted.append(i)

    print pool

    for i in pool:
        if i == 1:
            return False, blacklisted
    return True, blacklisted


def chooseRandomPool(arr,np,length,blacklisted):
    """
       chooseRandomPool choose and return a random pool from the network
       arr: the networkn 2d array
       np: the number of peers to choose
       length: the number of peers on a pool
       blacklisted: is the array contained the position of blacklisted peer
    """
    ppos = 0
    pos, pool = [[] for _ in range(2)]
    while ppos < np:
        x = randint(0, (length-1))
        y = randint(0, (length-1))
        if [x,y] not in pos and [x,y] not in blacklisted:
            pos.append([x,y])
            ppos += 1
    
    return pos






