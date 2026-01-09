from ultralytics import YOLO

def main():
    model = YOLO("yolov8n.yaml")  # architecture only

    model.train(
        data="data.yaml",
        epochs=50,
        imgsz=640,
        batch=16,
        pretrained=False
    )

if __name__ == "__main__":
    main()
