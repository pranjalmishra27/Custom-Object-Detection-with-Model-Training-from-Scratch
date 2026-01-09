# Custom Object Detection from Scratch

This repository presents a complete **end-to-end object detection pipeline trained entirely from scratch** (without using any pretrained weights), developed as part of a **Computer Vision Engineer Internship Assignment**.

The project covers dataset preparation, model training, evaluation, and real-time inference, following industry-standard practices.

---

## 📌 Task Objective

- Build and train a **custom object detection model from scratch**
- Use a dataset with **3–5 object classes**
- Evaluate the model using:
  - Mean Average Precision (mAP)
  - Inference speed (FPS)
  - Model size
- Demonstrate real-time detection with a video/GIF
- Submit clean, reproducible code with documentation

---

## 📦 Dataset

- **Dataset:** Pascal VOC 2012 (subset)
- **Source:** https://www.kaggle.com/datasets/huanghanchina/pascal-voc-2012
- **Number of Classes:** 5  
  - person  
  - car  
  - bicycle  
  - dog  
  - cat  

Annotations were converted from **VOC XML format** to **YOLO format** manually as part of the preprocessing pipeline.

📁 A small sample of images and labels is provided in `dataset_samples/` for reference.  
(The full dataset is not included due to size constraints.)

---

## 🧠 Model Architecture

- **Model:** YOLOv8 Nano
- **Type:** CNN-based, anchor-free object detector
- **Training Mode:** From scratch (`pretrained = False`)
- **Reason for Selection:**
  - Lightweight architecture
  - Fast inference speed
  - Suitable for real-time deployment

---

## ⚙️ Training Configuration

| Parameter | Value |
|--------|------|
| Image Size | 640 × 640 |
| Epochs | 50 |
| Batch Size | 16 |
| Optimizer | Adam |
| Pretrained Weights | ❌ Not used |

Training was performed in **Google Colab** with GPU acceleration.

---

## 📈 Evaluation Results

| Metric | Value |
|------|------|
| mAP@50 | ~0.68 |
| mAP@50–95 | ~0.42 |
| Inference Speed | ~30–35 FPS |
| Model Size | ~6 MB |

---

## 🚀 Future Improvements

Due to GPU and time constraints, the following enhancements could not be implemented in the current version:

- Train larger YOLOv8 variants (Medium/Large) for improved accuracy  
- Increase training epochs with better learning rate scheduling  
- Apply advanced data augmentation (MixUp, CutMix)  
- Perform hyperparameter optimization  
- Optimize the model using quantization and pruning for faster deployment  

These upgrades are expected to further improve accuracy, robustness, and deployment efficiency.

## 🚀 How to Run

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
