# 🎯 Handwritten Digit Recognition - Quick Start Guide

## How to Upload and Test Your Image

### Step 1: Prepare Your Image
1. Draw or write a digit (0-9) on paper and take a photo, or create a digital image
2. Save it as PNG, JPG, or JPEG format
3. The digit should be clearly visible

### Step 2: Place the Image
- Put your image file in this directory: `/home/ayushma/test/AI/Digit_Recognition/`
- You can drag and drop it into VS Code's file browser

### Step 3: Run the Notebook
1. Open `digit_recognition_from_scratch.ipynb`
2. Run all cells in order (this trains the neural network)
3. Go to the cells at the **end of the notebook** titled "Test Your Own Image Now!"
4. Update the filename in the cell: `my_image = "your_image.png"`
5. Set the color inversion:
   - `invert = True` for BLACK digit on WHITE background (most common)
   - `invert = False` for WHITE digit on BLACK background
6. Run the cell!

### Expected Output
```
============================================================
The uploaded handwritten digit is recognized as: 5
============================================================
Confidence Level: 98.76%
```

Plus visual display showing:
- Your original image
- Processed 28×28 image
- Probability distribution bar chart

## Quick Examples

### Example 1: Black digit on white background
```python
my_image = "my_handwritten_7.png"
invert = True  # Invert colors
```

### Example 2: Use the one-line shortcut
```python
display_prediction("my_digit.png", trained_parameters, invert=True)
```

## Troubleshooting

**Problem:** "Image not found"
- **Solution:** Make sure the image is in the same folder as the notebook
- Check the exact filename (including extension: .png, .jpg, etc.)
- The filename is case-sensitive

**Problem:** Wrong prediction
- **Solution:** Check the `invert` setting
- If your digit is black on white, use `invert=True`
- If your digit is white on black, use `invert=False`
- Make sure the digit is clearly visible and centered

**Problem:** Low confidence
- **Solution:** 
  - Draw the digit more clearly
  - Use a darker/thicker pen or marker
  - Ensure good lighting in the photo
  - Crop the image to show mainly the digit

## What Happens Behind the Scenes

1. **Image Loading**: PIL loads your image file
2. **Preprocessing**: 
   - Convert to grayscale
   - Resize to 28×28 pixels
   - Optionally invert colors
   - Normalize pixel values to [0, 1]
3. **Prediction**: Neural network processes the 784-pixel input
4. **Output**: 
   - Forward propagation through trained network
   - Softmax activation gives probability for each digit
   - Highest probability is the prediction

## Performance
- Expected accuracy: 95-97% on test data
- Training time: ~2-5 minutes (10 epochs)
- Prediction time: Instant (<0.1 seconds)

## No ML Libraries!
This is built completely from scratch using only:
- NumPy (for math)
- Matplotlib (for visualization)
- PIL (for image loading)

**No TensorFlow, PyTorch, or Keras!** 🎉
