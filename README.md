# Crowd Emotion Recognition with PyTorch
This project implements a system for crowd emotion recognition using PyTorch, aiming to automatically classify the emotions present within a crowd image or video. This has applications in sentiment analysis, public safety monitoring, and audience engagement studies.

# Project Goal:

The model aims to analyze visual cues from a crowd to infer the overall emotional state. This could involve recognizing facial expressions of individuals within the crowd, but could also extend to broader features like body language, posture, and crowd density. By analyzing these visual elements, the model can learn to classify emotions like happiness, anger, sadness, or neutrality.

# Dependencies:

- Python 3.x
- PyTorch
- torchvision (optional, for leveraging pre-trained models like ResNet or VGG)
- scikit-image (for image processing and manipulation)
- tqdm (for progress bars during training)

# Getting Started:

## 1. Clone the repository:
`git clone https://github.com/ehtisham-sadiq/crowd-emotion-recognition.git`

## 2. Prepare the Dataset:
- Download a publicly available crowd emotion dataset (e.g., CrowdNet, UCF101) or create your own with appropriate labeling for different emotions.
- Preprocess the data:
  - Resize images to a consistent size.
  - Apply data augmentation techniques (e.g., random cropping, flipping) to improve model robustness.
  - Convert categorical labels (e.g., "happy", "sad") to numerical representations for training.

# Project Structure:
- `data/`: Stores the training, validation, and test datasets after preprocessing.
- `models/`: Contains Python code defining and training the emotion recognition model.
  - Define your own architecture (e.g., Convolutional Neural Network (CNN) with multiple convolutional layers and pooling) or leverage a pre-trained model like ResNet and fine-tune it for crowd emotion classification.
- `utils/`: Includes utility functions used throughout the project for data loading, preprocessing, and helper functions for model training and evaluation.
- `train.py`: Script that handles training the chosen model on the prepared dataset, defining the loss function (e.g., cross-entropy) and optimizer (e.g., Adam) for learning.
- `evaluate.py`: Script for assessing the model's performance on a separate test set using metrics like accuracy, precision, recall, and F1-score for each emotion category.
- `predict.py` (Optional): Script to make predictions on unseen crowd images or videos. This script would load the trained model and process the new data to predict the most likely emotion present in the crowd.
- `README.md` (This file)

# Running the Project:

## 1. Running the Project:
`python3 train.py`
- This script will train the model for a specified number of epochs, saving checkpoints periodically to track progress and allow for resuming training if needed.

## 2. Evaluate the model:
`python3 evaluate.py`
- This script evaluates the trained model on the test set and provides performance metrics to gauge its effectiveness in recognizing crowd emotions.

## 3. Make predictions :
`python3 predict.py`
- This script allows you to use the trained model to predict the emotion of a new crowd image or video you provide.

# Contributors:
- ![Ehtisham Sadiq](https://github.com/ehtisham-sadiq)
- ![Dilbar]()
- ![Zunaira]()
- ![Ansha]()




