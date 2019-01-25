import sys
from monteCarloFunctions import checkConsensus,chooseRandomPool,genNetwork,getLength

def help():
    print "################################################################################################################\n"
    print "### Implementation of MonteCarlo algo to get some statistic about the impact of Malicous peers on the network###\n"
    print "################################################################################################################\n"
    print "USAGE: python main.py [nb of peers on the network] [% of malicious peers] [size of a validation pool] [nb of iteration]\n"
    print "EXAMPLE: python main.py 1000 10 5 10000\n"
    print "################################################################################################################\n"

def main():

    if len(sys.argv) < 5:
        help()
        exit(1)

    # Generate the network
    l = getLength(int(sys.argv[1]))
    network = genNetwork(l,int(sys.argv[2]))


    iteration, cosensusReached  = [0 for _ in range(2)]
    tBlacklisted, gBlacklisted = [[] for _ in range(2)]
    c = True

    while iteration < int(sys.argv[4]):
        p = chooseRandomPool(network, int(sys.argv[3]), l, gBlacklisted)
        c, tBlacklisted = checkConsensus(network, p)
        for b in tBlacklisted:
            gBlacklisted.append(b)
        if c:
            cosensusReached +=1
        iteration +=1
    
    res = (cosensusReached * 100) / int(sys.argv[4])
    print "consenesus % is :", res
    
if __name__ == "__main__":
    main()