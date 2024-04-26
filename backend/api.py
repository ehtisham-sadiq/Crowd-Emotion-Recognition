# This file defines the FastAPI application. It includes:
# Importing necessary libraries (FastAPI, uvicorn)
# Defining FastAPI routes for handling model prediction requests.
# Functions to receive image/video data from the request body.
# Logic for pre-processing the input data (can call functions from utils/preprocessing.py).
# Loading the trained PyTorch model (potentially from models/model.py).
# Performing emotion recognition using the loaded model.
# Returning the predicted emotion(s) in the respose