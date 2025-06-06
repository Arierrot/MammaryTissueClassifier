#!/usr/bin/env python3

import csv
import sys
from os import listdir
from os.path import isfile, join
import cv2


FATTY=0
FATTY_GLANDULAR=1
DENSE_GLANDULAR=2


def read_file(filename):
    csv_file = open(filename, 'r')
    reader = csv.reader(csv_file, delimiter=' ')
    data = dict()
    label_to_key = dict(F=FATTY, G=FATTY_GLANDULAR, D=DENSE_GLANDULAR)
    for row in reader:
        data[row[0]] = label_to_key[row[1]]
    csv_file.close()
    return data

def key_to_str(key):
    keystr = ("FATTY", "FATTY_GLANDULAR", "DENSE_GLANDULAR")
    return keystr[key]


if __name__=="__main__":

    

    csv_file = "./dataset/info.csv"

    path = './dataset/'
    files = [f for f in listdir(path) if isfile(join(path, f)) and f[-3:] =='pgm']


    data = read_file(csv_file)

    for f in files:
        im = cv2.imread(f"{path}/{f}", cv2.IMREAD_GRAYSCALE)
        mask = cv2.imread(f"{path}/mask_{f[:-3]}png", cv2.IMREAD_GRAYSCALE)
        cv2.imshow("im", im)
        cv2.imshow("mask", mask)
        cv2.waitKey(0)
        print(f"{f} es de tipo  {data[f[:-4]]}")
