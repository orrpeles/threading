#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program:
1 Based on program in chapter 11
2 use threding module to speed up the download
Ref: page 350, Automate the boring stuff
@author: python
"""

import requests, bs4, os, time, threading

#store comics in ./xkcd, cancels exception call if folder exists
os.makedirs('xkcd', exist_ok=True)

def downloadXkcx(startComic, endComic):
    for urlNumber in range(startComic, endComic):
    # download the page, store in res, terminate in case of exception
        print('Downloading page http://xkcd.com/%s' % (urlNumber))
        res = requests.get('http://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()
    # create BS object from text of downloaded page
    soup = bs4.BeautifulSoup(res.text) 
    
    comicElem = soup.select('#comic img')
    
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src') # get image
        # Download the image.
        print('Downloading image %s...' % (comicUrl))
        # store image in res
        res = requests.get(comicUrl)
        # if anything goes wrong with download kill program
        res.raise_for_status()

        # save the image to ./xkcd
        comicUrl = 'https:' + comicElem[0].get('src')
        # Download the image, store in res, terminate incase of exceptio
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()  
        #save image to ./xkcd
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
'''
    #Create and start thread objects
downloadThreads = [] # a list of all the Thread objects
for i in range(0, 1400, 100): # loops 14 times, creates 14 threads
# create thread object, in this example to download the entire site;
# when calling 'args', these represent the function's arguments, start and end
    downloadThread = threading.Thread(target=downloadXkcx, args=(i, i + 99))
# append to the list
    downloadThreads.append(downloadThread)
# call downloadXkcx in the new thread
    downloadThread.start()

# wait for threads to end
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done')
'''
