#!/usr/bin/env python3
"""
Verify MNIST Dataset - Check if we have digits (not Fashion-MNIST)
"""

import gzip
import numpy as np
import matplotlib.pyplot as plt

def load_and_display_sample():
    """Load and display a sample to verify it's digits"""
    
    print("="*70)
    print("VERIFYING MNIST DATASET")
    print("="*70)
    
    # Load a few images
    with gzip.open('mnist_data/train-images-idx3-ubyte.gz', 'rb') as f:
        magic = int.from_bytes(f.read(4), 'big')
        num_images = int.from_bytes(f.read(4), 'big')
        rows = int.from_bytes(f.read(4), 'big')
        cols = int.from_bytes(f.read(4), 'big')
        
        print(f"\nDataset Info:")
        print(f"  Magic number: {magic} (should be 2051 for images)")
        print(f"  Number of images: {num_images}")
        print(f"  Image size: {rows}x{cols}")
        
        data = np.frombuffer(f.read(), dtype=np.uint8)
        images = data.reshape(num_images, rows, cols)
    
    # Load labels
    with gzip.open('mnist_data/train-labels-idx1-ubyte.gz', 'rb') as f:
        magic = int.from_bytes(f.read(4), 'big')
        num_labels = int.from_bytes(f.read(4), 'big')
        labels = np.frombuffer(f.read(), dtype=np.uint8)
    
    print(f"\nLabel Info:")
    print(f"  Magic number: {magic} (should be 2049 for labels)")
    print(f"  Number of labels: {num_labels}")
    print(f"  Label range: {labels.min()} to {labels.max()}")
    print(f"  Sample labels: {labels[:20]}")
    
    # Display sample images
    fig, axes = plt.subplots(2, 5, figsize=(12, 5))
    fig.suptitle('VERIFICATION: Are these HANDWRITTEN DIGITS (0-9)?', 
                 fontsize=14, fontweight='bold')
    
    for i, ax in enumerate(axes.flat):
        ax.imshow(images[i], cmap='gray')
        ax.set_title(f'Label: {labels[i]}', fontsize=11, fontweight='bold')
        ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('mnist_verification.png', dpi=100, bbox_inches='tight')
    plt.show()
    
    print("\n" + "="*70)
    print("✓ Verification image saved: mnist_verification.png")
    print("\nCHECK THE IMAGE ABOVE:")
    print("  ✓ CORRECT: You should see handwritten DIGITS (0-9)")
    print("  ✗ WRONG: If you see clothing (shirts, shoes, etc), we have Fashion-MNIST")
    print("="*70)

if __name__ == "__main__":
    load_and_display_sample()
