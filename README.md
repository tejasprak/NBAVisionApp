# :eyes: :basketball: nbavisionapp 
### basketball object detection using densepose and YOLO

- [X] detect and extract coordinates of NBA players in broadcast, as well as classifying by team
- [] label individual plays (two or three, make or miss, etc)
- [] visualize plays easily
- [] further analysis (?)

### Setup:
1. The script run.sh will clone the YOLO model, DeepSort, and download pretrained weights:  ./run.sh
2. If run.sh does not work: Clone yolov4-deepsort: git clone https://github.com/theAIGuysCode/yolov4-deepsort
3. Download pre-trained weights file [here](https://pjreddie.com/media/files/yolo.weights) and place it in yolov4-deepsort/data
4. Copy object_tracker.py into the yolov4-deepsort directory

## Pipeline:
### 1. preprocessing - extract frames from mp4 using ffmpeg (frame_extraction/get_frames.sh)
### 2. detection - using yolov4-deepsort to detect players in frame (./run.sh)
### 3. player tracking and smoothing, coordinate extraction (yolov4-deepsort)
### 4. classify - based on team (team_classification/classify.py, query.py)
### 5. map frame on board (WIP)
### 6. postprocessing to export video using ffmpeg 