# get frames from video file

ffmpeg -i bucks_suns.mp4 -r 10 -qscale:v 2 output_%04d.jpg
