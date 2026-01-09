from ultralytics import YOLO

def main():
    model = YOLO("runs/detect/train/weights/best.pt")
    model.predict(source="dataset/images/val", save=True)

if __name__ == "__main__":
    main()
