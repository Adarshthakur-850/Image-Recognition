import tensorflow as tf
import numpy as np
import cv2
import os

def load_trained_model(path='models/cnn_model.h5'):
    if not os.path.exists(path):
        print(f"Model not found at {path}")
        return None
    return tf.keras.models.load_model(path)

def predict_image(model, image_path, class_names):
    if not os.path.exists(image_path):
        print("Image file not found.")
        return
        
    # Load and preprocess
    img = cv2.imread(image_path)
    if img is None:
        print("Failed to load image.")
        return 
        
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (32, 32)) 
    img_tensor = img.astype('float32') / 255.0
    img_tensor = np.expand_dims(img_tensor, axis=0) # Add batch dim
    
    # Predict
    preds = model.predict(img_tensor)
    idx = np.argmax(preds)
    label = class_names[idx]
    confidence = preds[0][idx]
    
    print(f"Prediction: {label} ({confidence*100:.2f}%)")
    return label, confidence
