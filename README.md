# nbavisionapp 
### basketball object detection using densepose and YOLO

- [] detect and extract coordinates of NBA players in broadcast, as well as classifying by team
- [] label individual plays (two or three, make or miss, etc)
- [] visualize plays easily
- [] further analysis (?)

## Pipeline:
### 1. preprocessing - extract frames from mp4 using ffmpeg
### 2. detection - using densepose/yolo to detect players in frame
### 3. classify - based on team
### 4. map frame on board
### 5. player tracking and smoothing, coordinate extraction
### 6. postprocessing to export video using ffmpeg