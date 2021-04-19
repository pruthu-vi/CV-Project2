import cv2
import urllib.request
import numpy as np
import os


def store_raw_images(link):
    neg_images_link = link
    neg_images_urls = urllib.request.urlopen(
        neg_images_link).read().decode('utf-8')

    if not os.path.exists('training/n'):
        os.makedirs('training/n')

    pic_num = 1

    for i in neg_images_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, "trainig/n/"+str(pic_num)+',jpg')
            img = cv2.imread("trainig/n/"+str(pic_num) +
                             ',jpg', cv2.IMREAD_GRAYSCALE)
            resized_img = cv2.resize(img, (100, 100))
            cv2.imwrite("trainig/n/"+str(pic_num)+',jpg', resized_img)
            pic_num += 1

        except Exception as e:
            print(str(e))


def main():
    link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'
    store_raw_images(link)
