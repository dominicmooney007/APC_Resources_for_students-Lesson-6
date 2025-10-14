# test_installation.py
import sys
print(f"Python version: {sys.version}")
print("=" * 50)

# Test each library
try:
    import cv2
    print("✅ OpenCV installed successfully")
    print(f"   OpenCV version: {cv2.__version__}")
except ImportError as e:
    print(f"❌ OpenCV installation failed: {e}")

try:
    import mediapipe as mp
    print("✅ MediaPipe installed successfully")
    print(f"   MediaPipe version: {mp.__version__}")
except ImportError as e:
    print(f"❌ MediaPipe installation failed: {e}")

try:
    import cvzone
    print("✅ CVZone installed successfully")
except ImportError as e:
    print(f"❌ CVZone installation failed: {e}")

try:
    import numpy as np
    print("✅ NumPy installed successfully")
    print(f"   NumPy version: {np.__version__}")
except ImportError as e:
    print(f"❌ NumPy installation failed: {e}")

# Test camera access
try:
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    if ret:
        print("✅ Camera access working")
    else:
        print("⚠️  Camera detected but couldn't capture frame")
except Exception as e:
    print(f"⚠️  Camera test failed: {e}")

print("=" * 50)
print("Installation test complete!")
