import gradio as gr
import requests
import pandas as pd

def clean_data(data):
    # Define the mapping for categorical variables
    job_map = {
        "admin.": 0,
        "blue-collar": 1,
        "entrepreneur": 2,
        "housemaid": 3,
        "management": 4,
        "retired": 5,
        "self-employed": 6,
        "services": 7,
        "student": 8,
        "technician": 9,
        "unemployed": 10,
        "unknown": 11
    }

    marital_map = {
        "divorced": 0,
        "married": 1,
        "single": 2,
        "unknown": 3
    }

    education_map = {
        "primary": 0,
        "secondary": 1,
        "tertiary": 2,
        "unknown": 3
    }

    default_map = {
        "no": 0,
        "yes": 1,
        "unknown": 2
    }

    housing_map = {
        "no": 0,
        "yes": 1,
        "unknown": 2
    }

    loan_map = {
        "no": 0,
        "yes": 1,
        "unknown": 2
    }

    contact_map = {
        "cellular": 0,
        "telephone": 1,
        "unknown": 2
    }

    month_map = {
        "apr": 0,
        "aug": 1,
        "dec": 2,
        "feb": 3,
        "jan": 4,
        "jul": 5,
        "jun": 6,
        "mar": 7,
        "may": 8,
        "nov": 9,
        "oct": 10,
        "sep": 11
    }

    poutcome_map = {
        "failure": 0,
        "nonexistent": 1,
        "success": 2,
        "unknown": 3
    }

    # Create a dictionary to store the cleaned data
    cleaned_data = {}

    # Clean the data
    cleaned_data["age"] = data[0]
    cleaned_data["job"] = job_map.get(data[1], 11)
    cleaned_data["marital"] = marital_map.get(data[2], 3)
    cleaned_data["education"] = education_map.get(data[3], 3)
    cleaned_data["default"] = default_map.get(data[4], 2)
    cleaned_data["balance"] = data[5] / 1000
    cleaned_data["housing"] = housing_map.get(data[6], 2)
    cleaned_data["loan"] = loan_map.get(data[7], 2)
    cleaned_data["contact"] = contact_map.get(data[8], 2)
    cleaned_data["day"] = data[9]
    cleaned_data["month"] = month_map.get(data[10], 11)
    cleaned_data["duration"] = data[11] / 100
    cleaned_data["campaign"] = data[12]
    cleaned_data["pdays"] = data[13] / 100
    cleaned_data["previous"] = data[14]
    cleaned_data["poutcome"] = poutcome_map.get(data[15], 3)

    print("Cleaned Data:")
    print(cleaned_data)

    return cleaned_data

def predict(age, job, marital, education, default, balance, housing, loan, contact, day, month, duration, campaign, pdays, previous, poutcome):
    cleaned_data = clean_data([age, job, marital, education, default, balance, housing, loan, contact, day, month, duration, campaign, pdays, previous, poutcome])
    url = "http://localhost:8000/predict/"
    api_data = {"features": list(cleaned_data.values())}
    print("API Request:")
    print(api_data)
    response = requests.post(url, json=api_data)
    prediction = response.json()["prediction"][0]
    return prediction

demo = gr.Interface(
    fn=predict,
    inputs=[
        gr.Number(label="Age"),
        gr.Text(label="Job"),
        gr.Text(label="Marital"),
        gr.Text(label="Education"),
        gr.Text(label="Default"),
        gr.Number(label="Balance"),
        gr.Text(label="Housing"),
        gr.Text(label="Loan"),
        gr.Text(label="Contact"),
        gr.Number(label="Day"),
        gr.Text(label="Month"),
        gr.Number(label="Duration"),
        gr.Number(label="Campaign"),
        gr.Number(label="Pdays"),
        gr.Number(label="Previous"),
        gr.Text(label="Poutcome"),
    ],
    outputs=gr.Text(label="Prediction"),
    title="Bank Marketing Prediction",
    description="This is a demo for bank marketing prediction. Please enter the required information to get the prediction."
)

if __name__ == "__main__":
    demo.launch()