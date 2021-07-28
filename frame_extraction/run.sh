# script to run darkflow detection on frames

cd ../yolo/darkflow
# add -gpu 1.0 for GPU
./flow --imgdir ../../bucks_vs_suns/ --model cfg/yolo.cfg --load bin/yolo.weights --json
