#!/data/data/com.termux/files/usr/bin/python

import requests
import sys
from termcolor import colored
import time
import os

os.system('clear')
print (colored('Checking...', 'red'))
time.sleep(1)

def unshorten_url(url):
    headers = {'User-Agent':'Anonymous'}
    return requests.head(url, allow_redirects=True, headers=headers).url

try:
    url = sys.argv[1]
    a = unshorten_url(url)
    print ("")
    print (colored(f"Url>> {a}", 'green'))
    sys.exit()
except IndexError as I:
    print (colored("Usage: ./unshorten.py <Url>", "blue"))
    sys.exit()
