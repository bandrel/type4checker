#!/usr/bin/env python
__author__ = 'Justin Bollinger'

'''
This script takes the cli argument of a directory and then scans all of the files in the directory to
check to see if they contain a username with a type 4 encrypted password.  The script assumes that the file
extension of the configuration is a .txt.
'''

import re
import sys
import glob
import os

#Global variable declarations
configdirectory = sys.argv[1]
fileextension = 'txt'
type4devices = []

#Regex precomplted searches
re_username = re.compile('username (\S+)\ .*secret\ 4')
re_hostname = re.compile('(\S+)\.txt')

os.chdir(configdirectory)  # Change directory so that Glob can work its magic
configfiles = glob.glob('*.' + fileextension)    # returns a list of all of the text files.


for configfile in configfiles:
    with open(configfile, 'r') as currentconfig:
        hostmatch = re.search(re_hostname, configfile)
        for line in currentconfig:
            usermatch = re.search(re_username, line)
            if usermatch is not None:
                type4devices = [hostmatch.group(1), usermatch.group(1)]

for line in type4devices:
    print line


