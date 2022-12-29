import io
import json

import torch
from torchvision import models
import torchvision.transforms as transforms
from PIL import Image
from flask import Flask, jsonify, request


app = Flask(__name__)
imagenet_class_index = json.load(open('imagenet_class_index.json'))

device = 'cuda:1' if torch.cuda.is_available() else 'cpu'
model = models.resnet50(pretrained=True).to(device)
model.eval()

PORT = 8894


def transform_image(image_bytes):
    inference_transforms = transforms.Compose(
        [transforms.Resize(512),
         transforms.ToTensor(),
         transforms.Normalize(
                             [0.485, 0.456, 0.406],
                             [0.229, 0.224, 0.225])])
    image = Image.open(io.BytesIO(image_bytes))
    return inference_transforms(image).unsqueeze(0)


def get_prediction(image_bytes):
    tensor = transform_image(image_bytes=image_bytes)
    outputs = model(tensor.to(device))
    y_hat = outputs.squeeze().argmax()
    predicted_idx = str(y_hat.item())
    return imagenet_class_index[predicted_idx]


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        img_bytes = file.read()
        class_id, class_name = get_prediction(image_bytes=img_bytes)
        return jsonify({'class_id': class_id, 'class_name': class_name})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
