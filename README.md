# Automated Extraction of Caravanserais in Satellite Images using Deep Learning

This study presents a deep learning-based image processing method for the automated extraction of caravanserais in satellite images. A database of 203 caravanserais in Iran was created and the YOLOv5 object detection algorithm was trained using transfer learning. The performance of the trained network was evaluated on 25 new images using the sliding window technique, resulting in a final accuracy of 91.43% mAP_0.5 in extracting the caravanserai locations.

## Requirements

- Deep learning framework (e.g. PyTorch)
- Object detection algorithm (e.g. YOLOv5)

## Usage

1. Clone the repository to your local machine
2. Download the database of 203 caravanserais in Iran and the trained weights
3. Run the code using a deep learning framework with the object detection algorithm

## Results

The trained YOLOv5 algorithm was able to accurately detect caravanserais in satellite images with a final accuracy of 91.43% mAP_0.5.

