
# Clipping each individual person detected with Darkflow YOLO json output. Does some filtering based on x and y coordinates and prepares for further query-based filtering

import json
import os 
import sys
from imageio import imread
import matplotlib.pyplot as plt
from PIL import Image
import numpy

img_dir = 'bucks_vs_suns/out/'
origin_img_dir = 'bucks_vs_suns'
save_dir = 'clips/'

def clip_img(file_name):
    img = imread(os.path.join(origin_img_dir,'{}.jpg'.format(file_name)))
    json_data = json.load(open(os.path.join(img_dir,'{}.json'.format(file_name))))
    z = 0
    for i,box in enumerate(json_data):
        if box['label'] == 'person':
            x0 = box['topleft']['x']
            y0 = box['topleft']['y']
            x1 = box['bottomright']['x']
            y1 = box['bottomright']['y']
            # Doing 
            if x1 < 1100 and y1 < 590 and y0 > 150:  
                z = z + 1
                print("Adding person with topleft x0: " + str(x0) + " y0: " + str(y0) + " bottomright x1: " + str(x1) + " y1: " + str(y1))
                clip_img = img[y0:y1, x0:x1]
                #clip_img = Image.fromarray(clip_img).resize(size=(160, 80)) 
                plt.imsave(os.path.join(save_dir,'{}_clip{}.jpg'.format(file_name, z)), clip_img)

if not os.path.exists(save_dir):
    os.mkdir(save_dir)
for f in os.listdir(img_dir):
    if '.jpg' in f:
        file_name = f.split('.')[0]
        clip_img(file_name)
