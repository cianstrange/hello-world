# Script:  bs4-scrape.py
# Desc:    A simple Python web page scraping/information gathering script that retrieves links
#          from a given url.
#           
#                .::::::::::.              
#             .::``::::::::::.              
#             :::..:::::::::::           
#             ````````::::::::             
#     .::::::::::::::::::::::: iiiiiii,   
#  .:::::::::::::::::::::::::: iiiiiiiii. 
#  ::::::::::::::::::::::::::: iiiiiiiiii  
#  ::::::::::::::::::::::::::: iiiiiiiiii  
#  :::::::::: ,,,,,,,,,,,,,,,,,iiiiiiiiii 
#  :::::::::: iiiiiiiiiiiiiiiiiiiiiiiiiii 
#  `::::::::: iiiiiiiiiiiiiiiiiiiiiiiiii`
#     `:::::: iiiiiiiiiiiiiiiiiiiiiii`   
#             iiiiiiii,,,,,,,,           
#             iiiiiiiiiii''iii            
#             `iiiiiiiiii..ii`         
#              `iiiiiiiiii`  
#
# Author:  Cian Heasley
# 
#  
"""
bs4-scrape.py is a simple script that uses BeautifulSoup to retrieve a list of links from
a given url. This code is an excerpt from a larger Python 3 program, I wanted to share
it because I found wildly varying and incomplete or incorrect code online that was
written to retrieve links from websites and attempt to fix relative urls. If the functions
below help anyone learning about Python, BeautifulSoup or web scraping, I'm glad.

To use this script you need Python 3 and you will need to pip install the various modules
imported below.

Example:

        $ python bs4-scrape.py --url [URL to scrape]


Todo:
    * Check whether links found are valid
    * Error handling
    * More argparse functionality

"""

from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
from urllib.parse import urljoin
from urllib import request
from pprint import pprint
import re
import argparse


def getHtml(url):
    """Return the HTML for a given URL."""
    return urlopen(url)


def getSoup(url):
    """Return BeautifulSoup instance for given URL."""
    return BeautifulSoup(getHtml(url), 'lxml')

def getLinks():
    """Scans the text for http URLs and return a set
    of URLs found, without duplicates, attempt to fix
    relative paths"""
    
    all_links = set()
    soup = getSoup(url)
    # Look for any links in the page   
    for link in soup.find_all('a', href=True):
        if 'href' in link.attrs:
            newurl = link.attrs['href']
            # Try to fix relative URLs using the URL arg provided
            if not newurl.startswith('http'):
                newurl = urljoin(url, newurl)
            # Ignore any URL that doesn't now start with http
            if newurl.startswith('http'):
                all_links.add(newurl)
    return all_links


def main(url):
    """ Main entry point. """

    #url = input("Enter the website url to scrape: ")
    soup = getSoup(url)
    quotes = '"'
    print("\n Preparing to scrape:", quotes, soup.title.string, quotes, "\n")
    # Count and print all links found
    linkage = getLinks()
    print("\n", (len(linkage)), "links found")
    pprint(linkage)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser(
    description='Script retrieves list of links on a webpage')
    # Add argument
    parser.add_argument(
        '-u', '--url', type=str, help='URL to scrape', required=True)
    # Array argument passed to script
    args = parser.parse_args()
    # Assign URL arg to variable
    url = args.url
    # Pass URL variable value to main
    main(args.url)



