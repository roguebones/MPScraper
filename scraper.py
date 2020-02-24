#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import urllib
import re
import requests


# use this image scraper from the location that you want to save scraped images to

def main():
    #user_url = 'https://www.mountainproject.com/user/15116/blitzo/photos'
    user_url = 'https://www.mountainproject.com/user/200084808/chase-g/photos'
    download_all_images(user_url)

    # TODO: take user input of user_url

def make_soup(url):
    html = urllib.request.urlopen(url).read()
    return BeautifulSoup(html, features='html.parser')

def make_url_list(url):

    page_num = 1
    url += '?page='
    url_list = []

    while True:
        
        page_url = url + str(page_num)
        r = requests.get(page_url)
        pat = re.search('https://www.mountainproject.com/photo/', r.text)
        if pat is None:
            break
        else:
            url_list.append(page_url)
        page_num += 1

    return url_list

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

def download_all_images(url):
    
    for item in make_url_list(url):
        get_images(item)

    # TODO: multithreading

main()



