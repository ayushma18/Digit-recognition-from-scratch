#!/usr/bin/env python3
"""
Quick Test Script for Digit Recognition
Run this after training your model in the notebook
"""

import os
import sys

def test_image(image_path, invert=True):
    """Test a single image with the trained model"""
    
    # Check if model exists
    if not os.path.exists("trained_digit_recognizer.pkl"):
        print("❌ Error: Trained model not found!")
        print("\nPlease:")
        print("  1. Open digit_recognition_from_scratch.ipynb")
        print("  2. Run all cells to train the model")
        print("  3. The model will be saved as 'trained_digit_recognizer.pkl'")
        print("  4. Then run this script again")
        return
    
    # Check if image exists
    if not os.path.exists(image_path):
        print(f"❌ Error: Image '{image_path}' not found!")
        print(f"\nCurrent directory: {os.getcwd()}")
        print("Please provide the correct path to your image.")
        return
    
    # Import required libraries
    try:
        import numpy as np
        import pickle
        from PIL import Image
        import matplotlib.pyplot as plt
    except ImportError as e:
        print(f"❌ Error: Missing required library: {e}")
        print("\nPlease install: pip install numpy pillow matplotlib")
        return
    
    # Load the trained model
    print("Loading trained model...")
    with open("trained_digit_recognizer.pkl", "rb") as f:
        parameters = pickle.load(f)
    print("✅ Model loaded!")
    
    # Define activation functions
    def relu(Z):
        return np.maximum(0, Z)
    
    def softmax(Z):
        exp_Z = np.exp(Z - np.max(Z, axis=1, keepdims=True))
        return exp_Z / np.sum(exp_Z, axis=1, keepdims=True)
    
    def forward_propagation(X, parameters):
        W1 = parameters['W1']
        b1 = parameters['b1']
        W2 = parameters['W2']
        b2 = parameters['b2']
        
        Z1 = np.dot(X, W1) + b1
        A1 = relu(Z1)
        Z2 = np.dot(A1, W2) + b2
        A2 = softmax(Z2)
        
        return A2
    
    # Preprocess image
    print(f"Processing image: {image_path}")
    img = Image.open(image_path)
    img = img.convert('L')
    img = img.resize((28, 28), Image.Resampling.LANCZOS)
    img_array = np.array(img)
    
    if invert:
        img_array = 255 - img_array
    
    img_array = img_array.astype(np.float32) / 255.0
    img_array = img_array.reshape(1, 784)
    
    # Make prediction
    predictions = forward_propagation(img_array, parameters)
    predicted_digit = np.argmax(predictions[0])
    confidence = predictions[0][predicted_digit]
    
    # Display result
    print("\n" + "=" * 70)
    print(f"The uploaded handwritten digit is recognized as: {predicted_digit}")
    print("=" * 70)
    print(f"Confidence: {confidence*100:.2f}%")
    print("\nProbability distribution:")
    for digit in range(10):
        bar = "█" * int(predictions[0][digit] * 40)
        print(f"  Digit {digit}: {predictions[0][digit]*100:5.2f}% {bar}")
    print("=" * 70)

if __name__ == "__main__":
    # Default test
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
        invert = True
        if len(sys.argv) > 2:
            invert = sys.argv[2].lower() in ['true', '1', 'yes']
        test_image(image_path, invert)
    else:
        print("=" * 70)
        print("DIGIT RECOGNITION TEST SCRIPT")
        print("=" * 70)
        print("\nUsage:")
        print("  python test_digit.py <image_path> [invert]")
        print("\nExamples:")
        print("  python test_digit.py my_digit.png")
        print("  python test_digit.py my_digit.png True   # Black on white")
        print("  python test_digit.py my_digit.png False  # White on black")
        print("\nOR: Edit this file and update the default image path below")
        print("=" * 70)
        
        # Default image for testing
        default_image = "sample_digit.png"
        if os.path.exists(default_image):
            print(f"\n✅ Found default test image: {default_image}")
            print("Testing with default image...\n")
            test_image(default_image, invert=False)
        else:
            print(f"\n⚠️  Default image '{default_image}' not found.")
            print("Please provide an image path as argument.")
