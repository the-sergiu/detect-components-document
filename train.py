from ultralytics import YOLO

yolo = YOLO('yolov8s.pt')
yolo.train(data='custom.yaml', epochs=20)