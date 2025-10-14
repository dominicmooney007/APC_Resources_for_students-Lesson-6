# CVZone Library Functions Reference

A comprehensive guide to all functions and capabilities available in the CVZone computer vision library.

---

## 🤲 Hand Tracking Module (`HandTrackingModule`)

### Core Detection Functions:
- `HandDetector()` - Initialize hand detector with configuration parameters
- `findHands(img, draw, flipType)` - Detect hands and landmarks in image
- `fingersUp(myHand)` - Count which fingers are raised (returns list of 0s and 1s)
- `findDistance(p1, p2, img, color, scale)` - Calculate distance between two landmarks
- `findPosition(img, handNo, draw)` - Get positions of all hand landmarks

### Hand Tracking Capabilities:
- **Detect up to 2 hands** simultaneously
- **Track 21 landmarks per hand** (fingertips, joints, palm)
- **Identify hand type** (left/right hand classification)
- **Calculate finger states** (extended/folded for each finger)
- **Measure distances** between any landmarks
- **Get bounding boxes** around detected hands
- **Find hand center points** for positioning

---

## 😊 Face Detection Module (`FaceDetectionModule`)

### Detection Functions:
- `FaceDetector()` - Initialize face detector
- `findFaces(img, draw)` - Detect faces with bounding boxes

### Face Detection Capabilities:
- **Detect multiple faces** with confidence scores
- **Get face bounding boxes** with coordinates
- **Support for different detection ranges** (2m short-range, 5m long-range)
- **Extract face center coordinates** for tracking
- **Confidence-based filtering** for reliable detection

---

## 🎭 Face Mesh Module (`FaceMeshModule`)

### Mesh Detection Functions:
- `FaceMeshDetector()` - Initialize face mesh detector
- `findFaceMesh(img, draw)` - Find 468 facial landmarks
- `findDistance(p1, p2, img)` - Calculate distance between facial landmarks

### Face Mesh Capabilities:
- **Track 468 facial landmarks** (detailed face mapping)
- **Detect up to 2 faces** simultaneously
- **Real-time face mesh rendering** with connections
- **Calculate distances** between any facial points
- **Support for facial expression analysis**
- **Eye, mouth, nose, eyebrow landmark groups**

---

## 🧍 Pose Estimation Module (`PoseModule`)

### Pose Detection Functions:
- `PoseDetector()` - Initialize pose detector
- `findPose(img, draw)` - Detect pose landmarks and connections
- `findPosition(img, draw, bboxWithHands)` - Get landmark positions
- `findDistance(p1, p2, img, color, scale)` - Calculate distance between pose points
- `findAngle(p1, p2, p3, img, color, scale)` - Calculate angle between three points
- `angleCheck(myAngle, targetAngle, offset)` - Check if angle matches target

### Pose Estimation Capabilities:
- **Detect 33 body landmarks** (head to toe mapping)
- **Calculate joint angles** for biomechanical analysis
- **Measure distances** between body points
- **Body bounding box detection** (with/without hands)
- **Pose classification support** for exercise analysis
- **Real-time pose tracking** and rendering

---

## 🤖 Classification Module (`ClassificationModule`)

### Classification Functions:
- `Classifier(modelPath, labelsPath)` - Load Keras/TensorFlow model
- `getPrediction(img, draw, pos, scale, color)` - Classify image with confidence

### Classification Capabilities:
- **Load custom trained models** (Keras .h5 format)
- **Real-time image classification** with confidence scores
- **Support for Teachable Machine models**
- **Multi-class prediction** with probability distribution
- **Visual feedback** with labels and confidence display
- **Custom model integration** for specific applications

---

## 🎬 Selfie Segmentation Module (`SelfiSegmentationModule`)

### Segmentation Functions:
- `SelfiSegmentation(model)` - Initialize segmentation model
- `removeBG(img, imgBg, cutThreshold)` - Remove/replace background

### Segmentation Capabilities:
- **Real-time background removal** from selfies/portraits
- **Background replacement** with solid colors or images
- **Adjustable segmentation sensitivity** via threshold
- **Support for different model types** (general vs landscape)

---

## 🎨 Color Detection Module (`ColorModule`)

### Color Detection Functions:
- `ColorFinder(trackBar)` - Initialize color detector
- `initTrackbars()` - Create HSV adjustment trackbars
- `getTrackbarValues()` - Get current HSV threshold values
- `update(img, myColor)` - Detect specific color in image

### Color Detection Capabilities:
- **HSV-based color detection** for robust color tracking
- **Interactive trackbars** for real-time HSV tuning
- **Generate color masks** for object isolation
- **Multi-color detection** support
- **Real-time color tracking** with contour detection

---

## 📊 Plot Module (`PlotModule`)

### Plotting Functions:
- `LivePlot(w, h, yLimit, interval, invert, char)` - Initialize live plotter
- `update(y, color)` - Update plot with new data point
- `drawBackground()` - Draw plot grid and background

### Plotting Capabilities:
- **Real-time data visualization** on video feed
- **Customizable graph parameters** (size, limits, colors)
- **Live updating plots** for sensor data
- **Grid and label display** for readability

---

## 📡 Serial Communication Module (`SerialModule`)

### Serial Functions:
- `SerialObject(portNo, baudRate, digits, max_retries)` - Initialize serial connection
- `sendData(data)` - Send data to connected device
- `getData()` - Receive data from connected device

### Serial Communication Capabilities:
- **Arduino/microcontroller communication**
- **Auto-detect available serial ports**
- **Send/receive formatted data** (multiple values)
- **Error handling and retry logic**
- **Bidirectional communication** support

---

## ⏱️ FPS Module (`FPS`)

### FPS Functions:
- `FPS(avgCount)` - Initialize FPS counter
- `update(img, pos, bgColor, textColor, scale, thickness)` - Calculate and display FPS

### FPS Capabilities:
- **Real-time FPS calculation** for performance monitoring
- **Averaged FPS display** over multiple frames
- **Customizable visual display** (position, colors, size)
- **Performance optimization** guidance

---

## 🎛️ PID Controller Module (`PID`)

### PID Functions:
- `PID(pidVals, targetVal, axis, limit)` - Initialize PID controller
- `update(cVal)` - Calculate PID output based on current value
- `draw(img, cVal)` - Visualize PID control on image

### PID Control Capabilities:
- **Proportional-Integral-Derivative control** implementation
- **Real-time control calculations** for servo/motor positioning
- **Visual PID debugging** with target visualization
- **Output limiting** for safe operation

---

## 🛠️ Utility Functions (`Utils`)

### Image Processing Utilities:
- `stackImages(imgList, cols, scale)` - Combine multiple images in grid layout
- `cornerRect(img, bbox, l, t, colorR, colorC)` - Draw stylized corner rectangles
- `putTextRect(img, text, pos, scale, thickness)` - Add text with background rectangle
- `overlayPNG(imgBack, imgFront, pos)` - Overlay transparent PNG images
- `rotateImage(imgInput, angle, scale, keepSize)` - Rotate images with options

### Computer Vision Utilities:
- `findContours(img, imgPre, minArea, filter)` - Detect and filter shape contours
- `downloadImageFromUrl(url, keepTransparency)` - Download images from URLs

### Utility Capabilities:
- **Multi-image display** for debugging and comparison
- **Professional UI elements** (rounded rectangles, overlays)
- **Text rendering** with customizable backgrounds
- **Image manipulation** (rotation, scaling, overlays)
- **Contour detection** for shape analysis
- **Web image integration** for dynamic content

---

## 🔧 Advanced Integration Features

### Multi-Module Combinations:
- **Hand + Face tracking** for comprehensive interaction
- **Pose + Classification** for exercise analysis
- **Color + Hand tracking** for augmented reality applications
- **Face Mesh + Pose** for full-body avatar control

### Real-World Applications:
- **Gesture control systems** for smart home automation
- **Exercise and fitness trainers** with form analysis
- **Interactive art installations** responding to human presence
- **Accessibility tools** for hands-free computer control
- **Security systems** with multi-modal authentication
- **Educational tools** for interactive learning
- **Gaming interfaces** with natural human input
- **Industrial automation** with human-machine interaction

---

## 📱 Platform Compatibility

### Supported Hardware:
- **Raspberry Pi** (all models with camera support)
- **Desktop computers** (Windows, Mac, Linux)
- **Mobile devices** (with appropriate adaptations)
- **Industrial cameras** and specialized hardware

### Integration Capabilities:
- **GPIO control** for hardware interfacing
- **Serial communication** with microcontrollers
- **Network connectivity** for IoT applications
- **Database integration** for data logging
- **Web interfaces** for remote control
- **Mobile app integration** for user interfaces

---

## 🚀 Quick Start Examples

### Basic Hand Tracking:
```python
from cvzone.HandTrackingModule import HandDetector
import cv2

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    
    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        print(f"Fingers up: {fingers.count(1)}")
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)
```

### Face Detection:
```python
from cvzone.FaceDetectionModule import FaceDetector
import cv2

cap = cv2.VideoCapture(0)
detector = FaceDetector()

while True:
    success, img = cap.read()
    img, bboxs = detector.findFaces(img)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)
```

### Background Removal:
```python
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import cv2

cap = cv2.VideoCapture(0)
segmentor = SelfiSegmentation()

while True:
    success, img = cap.read()
    imgOut = segmentor.removeBG(img, (255, 0, 255))
    
    cv2.imshow("Image", imgOut)
    cv2.waitKey(1)
```

---

## 📦 Installation

```bash
pip install cvzone
```

**Dependencies:**
- opencv-python
- numpy
- mediapipe

---

## 📚 Resources

- **GitHub Repository**: [https://github.com/cvzone/cvzone](https://github.com/cvzone/cvzone)
- **Website**: [https://www.computervision.zone/](https://www.computervision.zone/)
- **Documentation**: Check the Examples folder for practical implementations

---

## 🔧 System Requirements

- Python 3.6+
- Webcam or video input device
- Sufficient CPU for real-time processing (GPU optional)
- Operating System: Windows, macOS, Linux

---

*This reference document provides a complete overview of CVZone's capabilities for computer vision applications, from basic detection to complex multi-modal interactive systems.*
