import os
from matplotlib.colors import rgb_to_hsv
from imageio import imread
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

img_dir = 'bucks_vs_suns_filtered'
hist_vec = None
imgs = None
d_threshold = 1.75
frame_box_list = []
color_space = 'rgb'
query_files = ['output_0002_clip9.jpg', 'output_0004_clip9.jpg', 'output_0004_clip6.jpg']

labeled_hist_vec = np.zeros([3, 30])

def hyphen_split(a):
    if a.count("-") == 1:
        return a.split("-")[0]
    return "-".join(a.split("-", 2)[:2])


for i, f in enumerate(query_files):
    img = imread(os.path.join(img_dir, f), pilmode='RGB')
    c_hist_vec = None
    img = img[20:-20, 10:-10]
    channel = 3
    for c in range(channel):
        hist, _ = np.histogram(img[:,:,c].ravel(), bins=10)
        hist = hist.astype(float)
        hist = (hist - np.min(hist))/ (np.max(hist) - np.min(hist))
        #(hist,_,_) = plt.hist(img[:,:,c].ravel(), bins=10)
        #plt.show()
        if c_hist_vec is None:
            c_hist_vec = hist
        else:
            c_hist_vec = np.vstack((c_hist_vec, hist))

    c_hist_vec = c_hist_vec.reshape(1, -1)
    labeled_hist_vec[i] = c_hist_vec

group = []

for i,f in enumerate(os.listdir(img_dir)):
    if 'jpg' not in f:
        continue
    img = imread(os.path.join(img_dir, f), pilmode='RGB')
    frame = f.split('.')[0].split('_')[0]
    print(f.split('.')[0].split('_')[1][4:])
    if (f.split('.')[0].split('_')[1][4:]):
        box = int(f.split('.')[0].split('_')[1][4:])
    
    frame_box_list.append({'frame':frame, 'box':box})
    if imgs is None:
        imgs = [img]
    else:
        imgs.append(img)
    c_hist_vec = None
    
    img = img[20:-20, 10:-10]
    if color_space == 'hsv':
        img = rgb_to_hsv(img/255)
    channel = 2 if color_space == 'hsv' else 3
    for c in range(channel):
        hist, _ = np.histogram(img[:,:,c].ravel(), bins=10)
        hist = hist.astype(float)
        hist = (hist - np.min(hist))/ (np.max(hist) - np.min(hist))
        if c_hist_vec is None:
            c_hist_vec = hist
        else:
            c_hist_vec = np.vstack((c_hist_vec, hist))
    c_hist_vec = c_hist_vec.reshape(1, -1)
    d = np.linalg.norm(labeled_hist_vec-c_hist_vec, axis=1)
    min_index = np.argmin(d)
    group.append(min_index)

print(hist_vec.shape)
from sklearn.cluster import KMeans, DBSCAN

kmeans = KMeans(n_clusters=4, random_state=0, n_jobs=-1)
# dbscan = DBSCAN(eps=0.15, min_samples=5)

cluster_result = kmeans.fit(hist_vec)

frame_class_dict = {}
img_test = [[],[],[]]
for need_g in range(len(np.unique(group))):
    fig = plt.figure()
    plt.axis('off')
    k = 1
    for i, g in enumerate(group):
#         if frame_box_list[i]['frame'] not in frame_class_dict.keys():
#             frame_class_dict[frame_box_list[i]['frame']] = {}
#         frame_class_dict[frame_box_list[i]['frame']][frame_box_list[i]['box']] = g
#         if len(img_test[g]) < 5:
#             img_test[g].append(imgs[i])
        if g == need_g:
            fig.add_subplot(3, 3, k)
            k = k + 1
            plt.axis('off')
            plt.imshow(imgs[i])
        if k == 10:
            break
    plt.savefig('test_group{}.jpg'.format(need_g))

import pickle
pickle.dump(frame_class_dict, open('query_method001.pkl','wb'))