# get frames from video file

ffmpeg -i ../videos/spurs_thunder.mp4 -r 30 -qscale:v 2 ../out/output_%04d.jpg
