#!/usr/bin/env python3
from PIL import Image
import os
import PIL
import argparse

print(r"""  _                                     _         
 (_)_ __ ___   __ _       _ __ ___  ___(_)_______ 
 | | '_ ` _ \ / _` |_____| '__/ _ \/ __| |_  / _ \
 | | | | | | | (_| |_____| | |  __/\__ \ |/ /  __/
 |_|_| |_| |_|\__, |     |_|  \___||___/_/___\___|
              |___/                                 """)
print('\t\tBy coder12341')
print("""\nimg-resize  Copyright (C) 2021  coder12341
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.\n""")

ap = argparse.ArgumentParser()
ap.add_argument("-i", '--input', required=True, help="Add path to input image")
ap.add_argument("-o", "--output", required=False, nargs="?", default='resized_image', help="Output name")
ap.add_argument('width', type=int, metavar='New width', nargs='?',help='Set width to resize image')
ap.add_argument('height', type=int, metavar='New height', nargs='?', help='Set height to resize image')
ap.add_argument("-r", required=False, type=bool, default=False, nargs='?', const=True, help="Keep aspect ratio")
ap.add_argument("-e", required=False, type=bool, default=False, nargs='?', const=True, help="Enhance image")
args = vars(ap.parse_args())

#os.system('clear')
try:
    image = Image.open(args['input'])
except:
    print('[!] File not found!')
    exit()
width=None
height=None

if not args['r']:
    if args['width']==None:
        try:
            width=int(input('New width: '))
            if args['height']:
                height=args['height']
        except:
            print('Abort.')
            exit()

    if args['height']==None:
        try:
            height=int(input('New height: '))
            if args['width']:
                width=args['width']
        except:
            print('Abort.')
            exit()

    else:
        width=args['width']
        height=args['height']

current_width=image.size[0]
current_height=image.size[1]

try:
    extension=image.split('.')
except:
    extension=[None, 'png']

if args['r']==False:
    print('[+] Resizing to %sx%s'%(width, height))
    resized_image = image.resize((width, height))
    resized_image.save(args['output']+'.'+extension[1])
else:
    cont=input('Keep aspect ratio? [Y/n] ')
    if cont.lower=='y' or '\n':
        h_or_w=input('Do you want to set manually the width or height? [w/h] ')
        if h_or_w.lower()=='w':
            if width==None:
                width=int(input('New width: '))
            resized_image = image.resize((width, width*current_height//current_width))
            resized_image.save(args['output']+'.'+extension[1])
        elif h_or_w.lower()=='h':
            if height==None:
                height=int(input('New height: '))
            resized_image = image.resize((height*current_width//current_height, height))
            resized_image.save(args['output']+'.'+extension[1])
        else:
            print('Abort.')
            exit()
    else:
        print('[+] If you don\'t want to keep the aspect ratio, run again the command without the \'-r\' argument')
        print('Abort.')
        exit()

if args['e']:
    import cv2
    import numpy as np

    filename=args['output']+extension[1]
    img = cv2.imread('hi.png')
    result = cv2.fastNlMeansDenoisingColored(img,None,20,10,7,21)
    cv2.imwrite(args['output']+'.'+extension[1], result)
