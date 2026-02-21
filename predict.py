"""Simple script to predict digits from images"""
import numpy as np
from PIL import Image
import pickle
import sys

def predict(image_path, invert=True):
    # Load model
    with open("model.pkl", "rb") as f:
        params = pickle.load(f)
    
    # Load and process image
    img = Image.open(image_path).convert('L').resize((28, 28))
    img_array = np.array(img)
    if invert:
        img_array = 255 - img_array
    img_array = img_array.reshape(1, 784) / 255.0
    
    # Predict
    Z1 = img_array @ params['W1'] + params['b1']
    A1 = np.maximum(0, Z1)
    Z2 = A1 @ params['W2'] + params['b2']
    exp_Z2 = np.exp(Z2 - np.max(Z2))
    A2 = exp_Z2 / np.sum(exp_Z2)
    
    digit = np.argmax(A2)
    confidence = A2[0][digit]
    
    print(f"The uploaded handwritten digit is recognized as: {digit}")
    print(f"Confidence: {confidence*100:.1f}%")
    return digit

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python predict.py <image_path> [--no-invert]")
        sys.exit(1)
    
    image_path = sys.argv[1]
    invert = "--no-invert" not in sys.argv
    predict(image_path, invert)
