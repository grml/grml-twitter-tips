#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import twitter
from optparse import OptionParser


parser = OptionParser()
parser.add_option("-f", "--file", dest="file", metavar="FILE",
                  default='~/.following.conf', help="config file")



def follow(api):
    following = api.GetFriends()

    followers = api.GetFollowers()

    for follower in followers:
        if (not follower in following) and not follower.protected:
            print "Following: " + follower.screen_name
            api.CreateFriendship(follower.screen_name)

    for friend in following:
        if not friend in followers:
            print "Unfollowing:  " + friend.screen_name
            api.DestroyFriendship(friend.screen_name)

def get_apis():
    env = {}
    retval = []
    (options, args) = parser.parse_args()
    filename = options.file
    try:
        execfile(os.path.expanduser(filename), {}, env)
    except IOError:
        sys.stderr.write("Could not read %s, quiting!\n" % filename)
        sys.exit(1)

    if not 'username' in env.keys():
        sys.stderr.write("Specify username in config")
        sys.exit(1)
    if not 'password' in env.keys():
        sys.stderr.write("Specify password in config")
        sys.exit(1)

    users = env['username']
    passwords = env['password']
    tweet = twitter.Api(username=users['twitter'], password=passwords['twitter'])
    dent = twitter.Api(username=users['identica'], password=passwords['identica'], host='http://identi.ca/api/')
    retval.append(tweet)
    retval.append(dent)
    for api in retval:
        api.SetXTwitterHeaders("grml.org", "http://www.grml.org", 1)
    return retval

def post(message, api):
    return api.PostUpdates(message, continuation='…')
