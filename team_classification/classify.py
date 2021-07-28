
# Clipping each individual person detected with Darkflow YOLO json output. Does some filtering based on x and y coordinates and prepares for further query-based filtering

import json
import os 
import cv2 as cv
import sys
from imageio import imread
import matplotlib.pyplot as plt
from PIL import Image
import numpy

img_dir = '../new_json/'
origin_img_dir = '../bucks_vs_suns2'
save_dir = '../clips/'
ppl = 0

def clip_img(file_name):
    global ppl
    print(os.path.join(origin_img_dir,'{}.jpg'.format(file_name)))
    img = imread(os.path.join(origin_img_dir,'{}.jpg'.format(file_name)))
    (newW, newH) = (640,480)
    (H, W) = img.shape[:2]
    rW = W / float(newW)
    rH = H / float(newH)
    # resize the image and grab the new image dimensions
    img = cv.resize(img, (newW, newH))
    print(os.path.join(img_dir,'{}.json'.format(file_name)))
    json_data = json.load(open(os.path.join(img_dir,'{}.json'.format(file_name))))
    z = 0
    for i,box in enumerate(json_data):
        if box['label'] == 'person':
            #ppl++
            x0 = box['topleft']['x']
            y0 = box['topleft']['y']
            x1 = box['bottomright']['x']
            y1 = box['bottomright']['y']
            print("x0", x0, "y0", y0, "x1", x1, "y1", y1)
            if x0 < 0:
                x0 = 0
            if y0 > 60 and x0 < 525:
                print("confidence", box['confidence'])
                clip_img = img[y0:y1, x0:x1]
                z = z + 1
                plt.imsave(os.path.join(save_dir,'{}_clip{}.jpg'.format(file_name, z)), clip_img)
                image = Image.open(os.path.join(save_dir,'{}_clip{}.jpg'.format(file_name, z)))
                #image.show()
            # Doing 
            #if x1 < 1100 and y1 < 590 and y0 > 150:  
            #    z = z + 1
                #print("Adding person with topleft x0: " + str(x0) + " y0: " + str(y0) + " bottomright x1: " + str(x1) + " y1: " + str(y1))
            #    
                #clip_img = Image.fromarray(clip_img).resize(size=(160, 80)) 
            #    plt.imsave(os.path.join(save_dir,'{}_clip{}.jpg'.format(file_name, z)), clip_img)
                #image = Image.open(os.path.join(save_dir,'{}_clip{}.jpg'.format(file_name, z)))
                #image.show()
                #input()


if not os.path.exists(save_dir):
    os.mkdir(save_dir)
for f in os.listdir(origin_img_dir):
    if '.jpg' in f:
        file_name = f.split('.')[0]
        clip_img(file_name)
