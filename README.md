<<<<<<< HEAD
# Image Recognition (CNN)

A Convolutional Neural Network (CNN) trained on CIFAR-10 to classify images into 10 categories (airplane, car, bird, cat, etc.).

## Project Structure
- `models/`: Best trained model (`cnn_model.h5`).
- `plots/`: Training logs and Confusion Matrix.
- `src/`: Code modules.

## Architecture
Custom CNN with 3 Blocks:
- Conv2D + BatchNormalization + ReLU + MaxPool + Dropout
- Final Dense layers with Softmax.

## Results
- **Metrics**: Accuracy, Precision, Recall, F1.
- **Visuals**: Check `plots/` for training curves.

## Installation
```bash
pip install -r requirements.txt
```

## Usage
Run the pipeline:
```bash
python main.py
```
To predict on a single image:
```python
from src.inference import load_trained_model, predict_image
model = load_trained_model()
predict_image(model, "path/to/image.jpg", class_names)
```
=======
# Image-Recognition
ml project
>>>>>>> d3b4e92561e807c2ab6dbbc22168f4cbd1f64d9c
