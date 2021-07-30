# Clone YOLOv4-deepsort, install requirements, and modify object-tracker to better fit in to NBAvisionapp's workflow

git clone https://github.com/theAIGuysCode/yolov4-deepsort
# CPU
pip install -r requirements.txt
# GPU
# pip install -r requirements-gpu.txt

python save_model.py --model yolov4 
wget https://drive.google.com/u/0/uc?export=download&confirm=JoPl&id=1UHtGQSfN_kOHMvEfrPFdwexDg7wwyulc
mv yolov4.weights yolov4-deepsort/data
rm yolov4-deepsort/object_tracker.py
cp object_tracker.py yolov4-deepsort/
cd yolov4-deepsort

python object_tracker.py --imgfolder ../out/ --output ../demo.avi --model yolov4 --json_output ../json/