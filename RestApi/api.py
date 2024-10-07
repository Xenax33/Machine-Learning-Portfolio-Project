from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

# Load the trained model
loaded_model = joblib.load('random_forest_model.joblib')

@app.get("/")
def read_root():
    return {"message": "Welcome to the Bank Marketing Model API"}

@app.post("/predict/")
def predict(data: dict):
    try:
        # Convert the input data to a numpy array
        input_data = np.array(data['features']).reshape(1, 16)

        # Make predictions using the loaded model
        prediction = loaded_model.predict(input_data)

        # Return the prediction as a JSON response
        return {"prediction": prediction.tolist()}
    except Exception as e:
        # Return a custom error message to the client
        raise HTTPException(status_code=500, detail=str(e))