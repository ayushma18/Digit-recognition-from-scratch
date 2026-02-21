#!/usr/bin/env python3
"""Simple digit recognition test script"""

import numpy as np
import pickle
from PIL import Image
import sys
import os

def predict(image_path, invert=True):
    """Test digit recognition on an image"""
    
    # Load model
    if not os.path.exists("trained_digit_recognizer.pkl"):
        print("Error: Model not found. Train the model first.")
        return
    
    with open("trained_digit_recognizer.pkl", "rb") as f:
        params = pickle.load(f)
    
    # Load and preprocess image
    img = Image.open(image_path).convert('L').resize((28, 28))
    img_array = np.array(img)
    
    if invert:
        img_array = 255 - img_array
    
    img_array = img_array.reshape(1, 784) / 255.0
    
    # Predict
    Z1 = img_array @ params['W1'] + params['b1']
    A1 = np.maximum(0, Z1)  # ReLU
    Z2 = A1 @ params['W2'] + params['b2']
    exp_Z2 = np.exp(Z2 - np.max(Z2))
    A2 = exp_Z2 / np.sum(exp_Z2)  # Softmax
    
    digit = np.argmax(A2)
    confidence = A2[0][digit]
    
    # Display result
    print(f"\nPredicted digit: {digit}")
    print(f"Confidence: {confidence*100:.2f}%")
    
    print("\nAll probabilities:")
    for i in range(10):
        bar = "█" * int(A2[0][i] * 40)
        print(f"  {i}: {A2[0][i]*100:5.2f}% {bar}")
    
    return digit

if __name__ == "__main__":
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
        invert = True if len(sys.argv) == 2 else sys.argv[2].lower() in ['true', '1', 'yes']
        predict(image_path, invert)
    else:
        print("Usage: python test_digit.py <image_path> [invert]")
        print("Example: python test_digit.py sample_digit.png")
        
        # Try default image
        if os.path.exists("sample_digit.png"):
            print("\nTesting with sample_digit.png...")
            predict("sample_digit.png", invert=False)
