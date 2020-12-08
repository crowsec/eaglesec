import wfuzz
import requests
from utils.colors import *

wordlist = requests.get('http://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/common.txt').text.split('\n')

def fuzz80(host):
    fuzz = wfuzz.get_payload(wordlist)
    for row in fuzz.fuzz(sc=[200], url="http://"+host+"/FUZZ"):
        print(str(row))

def fuzz443(host):
    fuzz = wfuzz.get_payload(wordlist)
    for row in fuzz.fuzz(sc=[200], url="https://"+host+"/FUZZ"):
        print(str(row))

def print(r):
    if "C=200" in r:
        prLightPurple(r)
    elif "C=301" in r:
        prYellow(r)
    else:
        prRed(r)