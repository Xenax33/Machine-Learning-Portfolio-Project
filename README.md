# HOW TO RUN THE MODEL

# Step 1:-
  Run the data_cleaning.py file inside the data cleaning folder. It will export a cleaned csv file.

# Step 2:-
  Run the model_building.py file inside model building folder.Replace the path with the path of the cleaned data csv file at line no 10. It will train the model on the cleaned data and export the model file.

# Step 3:-
  Open the api.py file inside the RestApi folder and open replace the path of the model exported by the model_building.py at line no 8 and then run this command in the terminal uvicorn api:app --reload. It will start a server at localhost port no 8000 with a post api which will get the data as json and then predict the deposit value based on the data.

# Step 4:-
  Run the app.py file and it will provide a UI where you can enter the values of the variables and then it will call the api at localhost:8000 and get the prediction and show the result.
