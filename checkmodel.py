import tensorflow.compat.v2
from keras.models import load_model

model = load_model(r'C:\Users\SID\Downloads\Stock_Market_Prediction_ML\Stock Predictions Model.keras')
print(model.summary())

# import os

# file_path = r'C:\Users\SID\Downloads\Stock_Market_Prediction_ML\Stock Predictions Model.keras'
# print("File exists:", os.path.exists(file_path))
# print("File size:", os.path.getsize(file_path))
