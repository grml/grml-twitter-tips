#!/usr/bin/env python

import utils
from get_line import get_new_entry
import sys

apis = utils.get_apis()
entry = get_new_entry()
if entry:
    print "Posting: " + entry
    for api in apis:
        utils.post(entry, api)
