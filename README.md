# :eyes: :basketball: nbavisionapp 
### basketball object detection using densepose and YOLO

- [X] detect and extract coordinates of NBA players in broadcast, as well as classifying by team
- [] label individual plays (two or three, make or miss, etc)
- [] visualize plays easily
- [] further analysis (?)

### Setup:
1. Clone darkflow from [here](https://github.com/thtrieu/darkflow)
2. Install darkflow: python3 setup.py build_ext --inplace
3. Download pre-trained weights file [here](https://pjreddie.com/media/files/yolo.weights) and place it in yolo/darkflow/bin

## Pipeline:
### 1. preprocessing - extract frames from mp4 using ffmpeg (./get_frames.sh)
### 2. detection - using densepose/yolo to detect players in frame (./run.sh)
### 3. classify - based on team (classify.py, query.py)
### 4. map frame on board 
### 5. player tracking and smoothing, coordinate extraction
### 6. postprocessing to export video using ffmpeg