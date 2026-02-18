# 📤 Image Upload Instructions

## 🎯 HOW TO TEST YOUR HANDWRITTEN DIGIT

### Method 1: Using the Notebook (Recommended)

1. **Open the notebook**
   ```
   digit_recognition_from_scratch.ipynb
   ```

2. **Run all cells** (from top to bottom)
   - This will train the neural network (~2-5 minutes)
   - You'll see training progress and accuracy

3. **Scroll to the END of the notebook**
   - Find the section: **"Test Your Own Image Now!"**

4. **Place your image file**
   - Drag and drop your digit image into this folder
   - Or save it directly here

5. **Update the cell**
   ```python
   my_image = "your_image_name.png"  # Change this!
   invert = True  # True for black on white, False for white on black
   ```

6. **Run the cell** ▶️
   - You'll instantly see: "The uploaded handwritten digit is recognized as: X"
   - Plus visualizations and confidence scores!

---

### Method 2: Using Python Script (After Training)

After you've trained the model in the notebook:

```bash
python test_digit.py my_digit.png
```

Or for white digit on black background:
```bash
python test_digit.py my_digit.png False
```

---

## 📁 Where to Put Your Image

Save your image in this folder:
```
/home/ayushma/test/AI/Digit_Recognition/
```

Supported formats: PNG, JPG, JPEG

---

## ✅ What You'll See

### Input
Your handwritten digit image (any size)

### Output
```
======================================================================
The uploaded handwritten digit is recognized as: 7
======================================================================
Confidence: 98.42%

Top 3 Most Likely Digits:
  1. Digit 7: 98.42% ████████████████████████████████████████
  2. Digit 1:  1.23% █
  3. Digit 9:  0.15% 
```

Plus a visual display with:
- Your original image
- Processed 28×28 version
- Probability bar chart

---

## 🎨 Tips for Best Results

### ✓ DO:
- Use a dark/thick pen or marker
- Draw the digit clearly and centered
- Use good lighting if taking a photo
- Make the digit fill most of the image
- Use a plain background

### ✗ DON'T:
- Use very thin or faint lines
- Include multiple digits in one image
- Use heavily textured backgrounds
- Take blurry photos

---

## 🔧 Troubleshooting

### "Image not found" error
- Check the filename matches exactly (including extension)
- Make sure the image is in the correct folder
- Filenames are case-sensitive!

### Wrong prediction
- Try changing the `invert` setting
- Make sure the digit is clear and centered
- Check if the image has good contrast

### Low confidence
- Redraw the digit more clearly
- Use a thicker pen
- Ensure better lighting
- Crop the image closer to the digit

---

## 🚀 Quick Start Command

If you just want to test right away:

1. Save your digit image as `my_digit.png` in this folder
2. Open the notebook
3. Run ALL cells
4. At the bottom, find the test section and run it!

That's it! 🎉

---

## 📊 Expected Performance

- **Training Accuracy**: ~97-98%
- **Test Accuracy**: ~95-97%
- **Prediction Time**: Instant (<0.1s)
- **Model Size**: ~100KB

Built from scratch with NO deep learning frameworks! ✨
