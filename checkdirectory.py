#!/usr/bin/env python
__author__ = 'Justin Bollinger'

import re
import sys
import glob
import os

origionaldir = os.getcwd()
configdirectory = sys.argv[1]
re_username = re.compile('username (\S+)\ .*secret\ 4')
re_hostname = re.compile('(\S+)\.txt')

os.chdir(configdirectory)
configfiles = glob.glob('*.txt')
type4devices = []

for configfile in configfiles:
    with open(configfile, 'r') as currentconfig:
        hostmatch = re.search(re_hostname, configfile)
        for line in currentconfig:
            usermatch = re.search(re_username, line)
            if usermatch is not None:
                type4devices = [hostmatch.group(1), usermatch.group(1)]

print type4devices


