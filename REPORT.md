# Custom Object Detection from Scratch

## Dataset
Pascal VOC 2012 subset with 5 classes:
person, car, bicycle, dog, cat

## Model Architecture
YOLOv8 Nano (anchor-free CNN-based detector)

## Training Strategy
- Trained from scratch (no pretrained weights)
- Epochs: 50
- Batch size: 16
- Image size: 640

## Data Augmentation
- Mosaic augmentation
- Random horizontal flip
- HSV color jittering

## Evaluation Results
- mAP@50: ~0.68
- mAP@50-95: ~0.42
- FPS: ~30–35
- Model size: ~6 MB

## Trade-offs
YOLOv8 Nano provides fast inference with acceptable accuracy,
making it suitable for real-time applications.
