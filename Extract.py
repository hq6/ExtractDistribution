#!/usr/bin/python

def processLine(line):
    ########################################
    # Update this code to process individual lines.

    ########################################
    pass

def processFile(f):
    ########################################
    # Reset any per-file state here

    ########################################
    for line in f:
        processLine(line)


################################################################################
# There should be no need to modify any code below this line.
################################################################################
import signal
import sys

def signal_handler(signal, frame):
    sys.exit(0)

def main():
    # Set up signal handler to die on SIGINT
    signal.signal(signal.SIGINT, signal_handler)

    if len(sys.argv) == 1:
        # Read from stdin
        processFile(sys.stdin)
    else:
        for f in sys.argv[1:]:
            try:
                with open(f) as currentFile:
                    processFile(currentFile)
            except:
                sys.stderr.write("Error opening file '%s'.\n" % f)

if __name__ == "__main__":
    main()
