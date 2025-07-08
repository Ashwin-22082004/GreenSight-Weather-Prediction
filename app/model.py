import joblib

MODEL_PATH = "model.joblib"

def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()

def predict(df):
    return model.predict(df)[0]
