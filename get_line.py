#!/usr/bin/env python

import sys
import fileinput

def get_new_entry(filename='tip_of_the_day.txt'):
    found_entry = False
    new_line = ""
    delim = "-- \n"
    for line in fileinput.input(filename, inplace=1):
        if line != delim:
            if not line.startswith("! ") and not found_entry:
                new_line+=line
                line = "! " + line
        sys.stdout.write(line)
        if new_line and line == delim:
            found_entry = True
    fileinput.close()
    return new_line
