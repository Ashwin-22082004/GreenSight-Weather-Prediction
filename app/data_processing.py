import pandas as pd

def load_data(path="data/climate_sample.csv"):
    return pd.read_csv(path)
