# Example Data Pipeline Steps:-->
# Load data,Clean data,Handle missing values,Feature engineering,Train model,Evaluate model,Save model or results

def log_pipeline(func):
    def wrapper(*args, **kwargs):
        print(f"[Log] Starting: {func.__name__}")
        result = func(*args, **kwargs)    # Call the real function with its arguments
        print(f"[Log] Finished: {func.__name__}")
        return result
    return wrapper

@log_pipeline
def clean_data():
    print("Cleaning data...")

@log_pipeline
def feature_engineering():
    print("Creating features...")

clean_data(5,"arish")
feature_engineering(6,"chai")
