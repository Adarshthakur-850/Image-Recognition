import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import os
import pickle

def train_model(model, x_train, y_train, x_test, y_test, epochs=20, batch_size=64):
    print("Starting training...")
    
    if not os.path.exists("models"):
        os.makedirs("models")
        
    callbacks = [
        EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True),
        ModelCheckpoint('models/cnn_model.h5', monitor='val_accuracy', save_best_only=True)
    ]
    
    history = model.fit(
        x_train, y_train,
        validation_data=(x_test, y_test),
        epochs=epochs,
        batch_size=batch_size,
        callbacks=callbacks,
        verbose=1
    )
    
    # Save training history for plotting
    with open('models/history.pkl', 'wb') as f:
        pickle.dump(history.history, f)
        
    return history
