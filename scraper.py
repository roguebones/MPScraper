#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import urllib
import re


# use this image scraper from the location that
# you want to save scraped images to

def make_soup(url):
    html = urllib.request.urlopen(url).read()
    return BeautifulSoup(html, features='html.parser')


def get_images(url):
    soup = make_soup(url)

    # this makes a list of bs4 element tags

    images = [img for img in
              soup.findAll(attrs={'data-original': re.compile('jpg')})]
    print
    str(len(images)) + ' images found.'
    print
    'Downloading images to current working directory.'

    # compile our unicode list of image links

    image_links = [each.get('data-original') for each in images]

    image_links = [w.replace('_smallMed_', '_medium_') for w in
                   image_links]

    for each in image_links:
        filename = each.split('/')[-1]
        urllib.request.urlretrieve(each, filename)

    return image_links



