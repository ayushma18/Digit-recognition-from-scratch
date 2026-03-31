# Handwritten Digit Recognition From Scratch

A neural network that recognizes handwritten digits (0-9), built entirely from scratch using only NumPy — no TensorFlow, PyTorch, or Keras.

## How It Works

- Trains a neural network (ReLU + Softmax) on the MNIST dataset (60,000 training images)
- Achieves ~95-97% accuracy on the test set
- Accepts your own handwritten digit images for prediction
- Training takes ~2-5 minutes; prediction is instant

**No ML libraries used** — only NumPy (math), Matplotlib (visualization), and PIL (image loading).

---

## Project Structure

```
Digit-recognition-from-scratch/
├── digit_recognition_from_scratch.ipynb   # Main notebook — train & predict
├── requirements.txt                       # Python dependencies
└── mnist_data/                            # Created automatically on first run
```

---

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip

---

### Linux Setup

**1. Clone the repository**
```bash
git clone <repo-url>
cd Digit-recognition-from-scratch
```

**2. Create and activate a virtual environment**
```bash
python3 -m venv myenv
source myenv/bin/activate
```

**3. Install dependencies**

Install only the core packages needed to run the notebook:
```bash
pip install numpy matplotlib pillow jupyter
```

Or install everything from requirements.txt:
```bash
pip install -r requirements.txt
```

**4. Launch the notebook**
```bash
jupyter notebook digit_recognition_from_scratch.ipynb
```

The notebook will automatically download the MNIST dataset (~55 MB) on first run.

---

### Windows Setup

**1. Clone the repository**
```cmd
git clone <repo-url>
cd Digit-recognition-from-scratch
```

**2. Create and activate a virtual environment**
```cmd
python -m venv myenv
myenv\Scripts\activate
```

> If you get a script execution policy error in PowerShell, run:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

**3. Install dependencies**

Install only the core packages needed to run the notebook:
```cmd
pip install numpy matplotlib pillow jupyter
```

Or install everything from requirements.txt:
```cmd
pip install -r requirements.txt
```

**4. Launch the notebook**
```cmd
jupyter notebook digit_recognition_from_scratch.ipynb
```

The notebook will automatically download the MNIST dataset (~55 MB) on first run.

---

## Training the Model

Once the notebook is open in your browser:

1. Run all cells from top to bottom — this downloads the data, trains the network, and saves the model
2. Training takes about 2-5 minutes
3. A live Gradio interface launches at the end so you can draw and test digits directly in the browser

---

## Testing Your Own Image

At the end of the notebook, find the **"Test Your Own Image"** section:

1. Place your image file in the same folder as the notebook
2. Update the filename in the cell:
   ```python
   my_image = "your_digit.png"
   ```
3. Set the color inversion:
   ```python
   invert = True   # black digit on white background (most common)
   invert = False  # white digit on black background
   ```
4. Run the cell

**Expected output:**
```
============================================================
The uploaded handwritten digit is recognized as: 5
============================================================
Confidence Level: 98.76%
```

---

## Image Preparation Tips

- Draw a single digit (0-9) clearly on paper and photograph it, or create a digital image
- Accepted formats: PNG, JPG, JPEG
- The digit should be centered and clearly visible
- Use a dark/thick pen for best results
- Crop the image to focus on the digit
- Good lighting helps if using a photo

---

## Troubleshooting

**MNIST download fails (404 error)**

The notebook tries multiple mirrors automatically. If all fail, download these files manually:
- `train-images-idx3-ubyte.gz`
- `train-labels-idx1-ubyte.gz`
- `t10k-images-idx3-ubyte.gz`
- `t10k-labels-idx1-ubyte.gz`

From: `https://storage.googleapis.com/tensorflow/tf-keras-datasets/`

Save all four files into the `mnist_data/` folder, then re-run the notebook.

---

**Wrong prediction**

- Check the `invert` setting — this is the most common cause
  - Black digit on white paper → `invert=True`
  - White digit on black background → `invert=False`
- Make sure the digit is clearly visible and reasonably centered

---

**Low confidence score**

- Draw the digit more clearly with a thicker pen
- Crop the image so the digit fills most of the frame
- Ensure good lighting when photographing

---

**Jupyter not found**

```bash
pip install jupyter notebook
```

---

## How the Neural Network Works

1. **Input**: 28×28 grayscale image → flattened to 784 values, normalized to [0, 1]
2. **Hidden layers**: configurable architecture with ReLU activation (default: 784 → 256 → 128 → 10)
3. **Output layer**: 10 neurons with Softmax activation (one per digit)
4. **Training**: mini-batch gradient descent with backpropagation, cross-entropy loss, hyperparameter tuning via random search
5. **Prediction**: digit with the highest probability is returned

---

## Dependencies

Core requirements (minimal install):
| Package | Purpose |
|---------|---------|
| numpy | All math and matrix operations |
| matplotlib | Visualizing training progress and predictions |
| pillow | Loading and preprocessing image files |
| jupyter | Running the notebook |

The `requirements.txt` includes additional packages (gradio, fastapi, etc.) from the development environment — you do not need all of them to run the notebook.
