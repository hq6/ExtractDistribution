#!/usr/bin/python

import sys
import matplotlib.pyplot as plt

def plot_cdf(cdf):
    numbers = [x[0] for x in cdf]
    fractions =  [x[1] for x in cdf]
    plt.plot(numbers, fractions)
    plt.show()

def read_cdf(f):
    cdf = []
    for line in f:
        parts = line.strip().split(",")
        cdf.append((float(parts[0]), float(parts[1])))
    return cdf

def main():
    if len(sys.argv) == 1:
        plot_cdf(read_cdf(sys.stdin))
    else:
      with open(sys.argv[1]) as currentFile:
        plot_cdf(read_cdf(currentFile))

if __name__ == '__main__':
    main()
