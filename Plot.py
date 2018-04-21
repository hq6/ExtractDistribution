#!/usr/bin/python

import sys
import matplotlib.pyplot as plt

def plot_cdf(cdf, xlabel="Number", ylabel="Fraction"):
    numbers = [x[0] for x in cdf]
    fractions =  [x[1] for x in cdf]
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.plot(numbers, fractions)
    plt.show()

def read_cdf(f):
    # Read column headers
    xlable, ylabel = next(f).split(",")

    # Read the rest of the cdf
    cdf = []
    for line in f:
        parts = line.strip().split(",")
        cdf.append((float(parts[0]), float(parts[1])))
    return xlable, ylabel, cdf

def main():
    if len(sys.argv) == 1:
        xlabel, ylabel, cdf = read_cdf(sys.stdin)
    else:
      with open(sys.argv[1]) as currentFile:
        xlabel, ylabel, cdf = read_cdf(currentFile)

    plot_cdf(cdf, xlabel, ylabel)

if __name__ == '__main__':
    main()
