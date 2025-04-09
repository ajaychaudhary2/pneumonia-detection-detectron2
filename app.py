import os
import cv2
import torch
from flask import Flask, render_template, request
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load model
cfg = get_cfg()
cfg.merge_from_file(r"G:\DL_project\pneumonia-detection-detectron2\rsna_output\config.yaml")
cfg.MODEL.WEIGHTS = r"G:\DL_project\pneumonia-detection-detectron2\rsna_output\model_final.pth"
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5
cfg.MODEL.DEVICE = "cpu"  # or 'cuda' if GPU available

predictor = DefaultPredictor(cfg)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    image = cv2.imread(filepath)
    outputs = predictor(image)

    v = Visualizer(image[:, :, ::-1], MetadataCatalog.get(cfg.DATASETS.TRAIN[0]), scale=1.0)
    out = v.draw_instance_predictions(outputs["instances"].to("cpu"))
    output_path = os.path.join(UPLOAD_FOLDER, 'result.jpg')
    cv2.imwrite(output_path, out.get_image()[:, :, ::-1])

    return render_template('result.html', original=file.filename, result='result.jpg')

if __name__ == '__main__':
    app.run(debug=True)
