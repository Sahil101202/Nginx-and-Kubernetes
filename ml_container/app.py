import os
from flask import Flask, request, jsonify
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
from flask_cors import CORS
from PIL import Image

app = Flask(__name__)
CORS(app)

# Load pre-trained MobileNetV2 model
model = MobileNetV2(weights='imagenet')

# Define route for image classification
@app.route('/classify', methods=['POST'])
def classify_image():
    # try:
        # Check if image file is present in the request
        if 'image' not in request.files:
            return jsonify({'error': 'No image file provided'}), 400

        # Read the image file
        img = request.files['image']

        # Load and preprocess the image
        img = Image.open(img)
        img = img.resize((224, 224))
        img = image.img_to_array(img)
        img = preprocess_input(img)
        img = img.reshape(1, 224, 224, 3)

        # Predict the class of the image
        preds = model.predict(img)
        # Decode predictions
        decoded_preds = decode_predictions(preds, top=3)[0]

        # Format predictions
        predictions = [{'label': label, 'probability': float(prob)} for (_, label, prob) in decoded_preds]

        return jsonify(predictions), 200

    # except Exception as e:
    #     # Log the exception for debugging
    #     print(e)
    #     # Return a meaningful error response
    #     return jsonify({'error': 'An unexpected error occurred'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
