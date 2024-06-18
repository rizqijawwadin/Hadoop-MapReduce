#!/usr/bin/env python
"""reducer.py"""

import sys

current_word = {}

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # update the count for the word
    if word in current_word:
        current_word[word] += count
    else:
        current_word[word] = count

# sort the words alphabetically
sorted_words = sorted(current_word.keys())

# output the final counts in alphabetical order
for word in sorted_words:
    print('%s\t%s' % (word, current_word[word]))
