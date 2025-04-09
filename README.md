# 🫁 Pneumonia Detection from Chest CT Scans using Detectron2

This project detects pneumonia in chest CT scan images using a **Faster R-CNN** model built with **Detectron2** and deployed via a **Flask web application**.

## 🚀 Project Highlights

- ⚙️ **Model**: Faster R-CNN (Detectron2)
- 🖼️ **Input**: Chest CT Scan Images
- 🧠 **Output**: Bounding box + pneumonia prediction
- 🌐 **Web App**: Upload image & see results
- 📦 **Deployment**: CPU-compatible, lightweight web interface

---

## 🧪 Demo

![Prediction Result](assets/demo_result.png)

---
### 1. Clone the Repository

```bash
git clone https://github.com/ajaychaudhary2/pneumonia-detection-detectron2.git
cd pneumonia-detection-detectron2

## 📥 Download Trained Model

📦 The trained model weights (`model_final.pth`) and config (`config.yaml`) are hosted on Google Drive.

You can download them automatically using this Python script:
python download_model.py

📌 Notes
Trained on RSNA Pneumonia Detection Challenge dataset.

Optimized for CPU-only environments.

Model weights are hosted externally due to GitHub's file size restrictions.


