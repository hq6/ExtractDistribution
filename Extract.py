#!/usr/bin/python

from __future__ import division, print_function
import re

# This method is called once per file to extract numbers out of that file.
# The default is to assume the file is a set of numbers.
def processFile(f):
    writeIDs = {}
    nums = []
    for line in f:
        line = line.strip()
        # Write is being dispatched
        if "Dispatching opcode 14" in line:
            match = re.search(': +(\d+\.\d) ns .* ID (\d+):', line)
            writeIDs[match.group(2)] = float(match.group(1))
            continue
        if "reply sent" in line:
            match = re.search(': +(\d+\.\d) ns .* ID (\d+):', line)
            if match.group(2) in writeIDs:
                nums.append(float(match.group(1)) - writeIDs[match.group(2)])
                del writeIDs[match.group(2)]
    return nums

################################################################################
# There should be no need to modify any code below this line.
################################################################################
import signal
import sys
import traceback

def print_cdf(cdf, outfile = sys.stdout):
    print("Number,Fraction")
    for number, fraction in cdf:
	outfile.write("%.4f,%.4f\n" % (number, fraction))


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
            except:
                sys.stderr.write("Error processing file '%s':\n" % f)
                traceback.print_exc()
                return
    cdf = generate_cdf(numbers)
    print_cdf(cdf)
    try:
        from Plot import plot_cdf
        plot_cdf(cdf)
    except:
        sys.stderr.write("Plotting with matplotlib failed.")
        traceback.print_exc()
        return

if __name__ == "__main__":
    main()
