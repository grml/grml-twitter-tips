#!/usr/bin/env python

import utils
from get_line import get_new_entry
import sys

additional = ' #grmlproject, #tip'
zsh = ', #zsh'

apis = utils.get_apis()
entry = get_new_entry()


def add_text(orig, add):
    if len(orig) + len(add) <= 140 or len(orig) > 140:
        orig += add
    return orig

if entry:
    entry = entry.rstrip()
    entry = add_text(entry, additional)
    if entry.find('zsh') != -1:
        entry = add_text(entry, zsh)

    print "Posting: " + entry
    for api in apis:
        utils.post(entry, api)
