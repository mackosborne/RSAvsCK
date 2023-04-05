import time
import random
from tabulate import tabulate
import matplotlib.pyplot as plt

def makeGraph(algorithms, totalTimes):
    plt.plot(algorithms, totalTimes)
    plt.xlabel("Algorithm")
    plt.ylabel("Total Time")
    plt.title("Total Time for Each Algorithm")
    plt.show()
    
    
   


def makeTable(algorithms, totalTimes):
    info = []
    for algorithm in algorithms:
        info.append([algorithm, totalTimes[algorithm]])
    
    print(tabulate(info, headers=["Algorithm", "Total Time"], tablefmt="grid"))
    
    