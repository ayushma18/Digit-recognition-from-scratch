#!/usr/bin/env python3
"""
MNIST Dataset Downloader
Automatically downloads MNIST dataset files with multiple mirror fallbacks
"""

import os
import urllib.request
import sys

def download_file(url, filepath):
    """Download a file with progress indication"""
    try:
        print(f"Downloading from: {url}")
        
        def progress_hook(block_num, block_size, total_size):
            downloaded = block_num * block_size
            if total_size > 0:
                percent = min(downloaded * 100.0 / total_size, 100)
                sys.stdout.write(f"\r  Progress: {percent:.1f}% [{downloaded}/{total_size} bytes]")
                sys.stdout.flush()
        
        urllib.request.urlretrieve(url, filepath, progress_hook)
        print("\n  ✓ Download complete!")
        return True
    except Exception as e:
        print(f"\n  ✗ Failed: {e}")
        return False

def download_mnist():
    """Download all MNIST files"""
    
    # List of mirror URLs (in order of preference)
    mirrors = [
        "https://storage.googleapis.com/tensorflow/tf-keras-datasets/",
        "https://github.com/golbin/TensorFlow-MNIST/raw/master/mnist/data/",
        "http://yann.lecun.com/exdb/mnist/",
    ]
    
    files = [
        "train-images-idx3-ubyte.gz",
        "train-labels-idx1-ubyte.gz",
        "t10k-images-idx3-ubyte.gz",
        "t10k-labels-idx1-ubyte.gz"
    ]
    
    # Create data directory
    data_dir = "mnist_data"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        print(f"✓ Created directory: {data_dir}/\n")
    
    # Download each file
    print("="*70)
    print("MNIST DATASET DOWNLOADER")
    print("="*70)
    
    for filename in files:
        filepath = os.path.join(data_dir, filename)
        
        # Skip if already exists
        if os.path.exists(filepath):
            print(f"\n✓ {filename} already exists (skipping)")
            continue
        
        print(f"\n📥 Downloading: {filename}")
        print("-"*70)
        
        # Try each mirror until one works
        downloaded = False
        for mirror in mirrors:
            url = mirror + filename
            if download_file(url, filepath):
                downloaded = True
                break
        
        if not downloaded:
            print(f"\n❌ Failed to download {filename} from all mirrors")
            print("\n🔧 Manual download instructions:")
            print(f"   Visit: https://storage.googleapis.com/tensorflow/tf-keras-datasets/{filename}")
            print(f"   Save to: {os.path.abspath(filepath)}")
            return False
    
    print("\n" + "="*70)
    print("✅ ALL FILES DOWNLOADED SUCCESSFULLY!")
    print("="*70)
    print(f"\nFiles location: {os.path.abspath(data_dir)}/")
    print("\nYou can now run the notebook cells to load and train the model.")
    return True

if __name__ == "__main__":
    success = download_mnist()
    if not success:
        sys.exit(1)
