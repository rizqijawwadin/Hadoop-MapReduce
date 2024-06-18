#!/usr/bin/env python
"""mapper.py"""

import sys
import re

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # replace non-letters with spaces
    line = re.sub(r'[^a-zA-Z\s]', ' ', line)
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output)
        # tab-delimited; the trivial word count is 1
        print('%s\t%s' % (word.lower(), 1))
