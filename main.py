from src.data_loader import load_data, get_class_names
from src.model import build_cnn_model
from src.train import train_model
from src.evaluate import evaluate_model
from src.visualization import plot_history, plot_misclassified

def main():
    print("Starting Image Recognition Pipeline...")
    
    (x_train, y_train), (x_test, y_test) = load_data()
    class_names = get_class_names()
    
    model = build_cnn_model(input_shape=x_train.shape[1:], num_classes=10)
    model.summary()
    
    history = train_model(model, x_train, y_train, x_test, y_test, epochs=3, batch_size=64)
    
    plot_history(history)
    
    y_pred, y_true = evaluate_model(model, x_test, y_test, class_names)
    
    plot_misclassified(x_test, y_true, y_pred, class_names)
    
    print("Pipeline completed. Model and plots saved.")

if __name__ == "__main__":
    main()
