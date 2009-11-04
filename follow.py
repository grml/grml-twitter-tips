#!/usr/bin/env python
# -*- coding: utf-8 -*-

#(c) 2009 Ben McIlwain, released under the terms of the GNU GPL v3.
import twitter
import os
import sys

env = {}
try:
    execfile(os.path.expanduser('~/.following.conf'), {}, env)
except IOError:
    sys.stderr.write("Could not read ~/.following.conf, quiting!\n")
    sys.exit(1)

if not 'username' in env.keys():
    sys.stderr.write("Specify username in config")
    sys.exit(1)
if not 'password' in env.keys():
    sys.stderr.write("Specify password in config")
    sys.exit(1)

api = twitter.Api(username=env['username'], password=env['password'])

following = api.GetFriends()

followers = api.GetFollowers()
for follower in followers:
    if (not follower in following):
        print "Following: " + follower.screen_name
        api.CreateFriendship(follower.screen_name)

for friend in following:
    if not friend in followers:
        print "Unfollowing:  " + follower.screen_name
        api.DestroyFriendship(friend.screen_name)
