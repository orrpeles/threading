#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 22:13:54 2019
Program:
1 Loads the XKCD home page.
2 Saves the comic image on that page.
3 Follows the Previous Comic link.
4 Repeats until it reaches the first comic.
Ref: Chapter 11, Automate the boring stuff
@author: python
"""

import requests, bs4, os, time

url = 'https://xkcd.com/'
urlEnd = 'https://xkcd.com//2150/'
os.makedirs('/home/python/pythonAutomate/threading/xkcd', exist_ok=True) #store comics in ./xkcd, cancels exception call if folder exists

while url != urlEnd:
    print('Downloading page %s' % url)
    res = requests.get(url) # download the page
    res.raise_for_status # if something goes wrong, raise an exception and terminate program
    
    soup = bs4.BeautifulSoup(res.text) # create BS object from text of downloaded page
    
    comicElem = soup.select('#comic img')
    
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src') # get image
        # Download the image.
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl) # store image in res
        res.raise_for_status() # if anything goes wrong with download kill program
    
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    
    # get prev button URL
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com/' + prevLink.get('href') #modify URL
    # get prev button URL
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com/' + prevLink.get('href')
    print('url is: %s' % url)
    time.sleep(1)

print('Done')

