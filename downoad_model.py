import gdown
import os

model_path = "rsna_output/model_final.pth"
config_path = "rsna_output/config.yaml"

# Download if not already present
if not os.path.exists(model_path):
    os.makedirs("rsna_output", exist_ok=True)
    gdown.download("https://drive.google.com/uc?id=YOUR_MODEL_FILE_ID", model_path, quiet=False)

if not os.path.exists(config_path):
    gdown.download("https://drive.google.com/uc?id=YOUR_CONFIG_FILE_ID", config_path, quiet=False)