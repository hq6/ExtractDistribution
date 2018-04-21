#!/usr/bin/python

from __future__ import division, print_function

# This method is called once per file to extract numbers out of that file.
def processFile(f):
    # Modify this code to do different per-file number extraction.
    nums = []
    for line in f:
        nums.append(int(line))
    return nums

################################################################################
# There should be no need to modify any code below this line.
################################################################################
import signal
import sys
import traceback

def print_cdf(cdf, outfile = sys.stdout):
    for number, fraction in cdf:
	outfile.write("%8.4f    %8.3f\n" % (number, fraction))


# Generate the cdf, which can later be either printed or plotted.
def generate_cdf(numbers):
    """
    Take the data values passed in as a list, and produces a cdf in the form of
    ([number], [fraction]), such that the given fraction of all numbers in the
    log file have values less than or equal to the given number.
    """
    # Generate a CDF from the array.
    numbers.sort()
    result = [(0.0, 0.0)]
    result.append((numbers[0], 1/len(numbers)))
    for i in range(1, 100):
       result.append((numbers[int(len(numbers)*i/100)], i/100))
    result.append((numbers[int(len(numbers)*999/1000)], .999))
    result.append((numbers[int(len(numbers)*9999/10000)], .9999))
    result.append((numbers[-1], 1.0))
    return result

def signal_handler(signal, frame):
    sys.exit(0)

# This program takes zero (read from stdin) or more files, runs a custom number
# extraction function defined above, and computes and plots a cumulative
# distribution.
def main():
    # Set up signal handler to die on SIGINT
    signal.signal(signal.SIGINT, signal_handler)

    numbers = []
    if len(sys.argv) == 1:
        # Read from stdin
        numbers.extend(processFile(sys.stdin))
    else:
        for f in sys.argv[1:]:
            try:
                with open(f) as currentFile:
                    numbers.extend(processFile(currentFile))
            except Exception as e:
                sys.stderr.write("Error processing file '%s':\n" % f)
                traceback.print_exc()
                return
    cdf = generate_cdf(numbers)
    print_cdf(cdf)

if __name__ == "__main__":
    main()
