# Machine Learning Regressions for the Prediction of Earthquake Characteristics/Features
----------------------------
## WORK IN PROGRESS!!
----------------------------
API can be found: https://earthquake-ml-app.herokuapp.com
----------------------------
### Note: Part of the inspiration/ideas for some of the modeling machine learning code came from: https://www.kaggle.com/chenzecharya/earthquake-random-forest.

## Part One: Creation of Databases and Deployment of Earthquake API
### Objectives:
- Obtain the information from: https://www.usgs.gov/programs/earthquake-hazards/earthquakes
- Place the information collected as part of a database to be accessed for training the model(s).
- Create and deploy an API with the information.
- Maintain the database and the API by updating and adding the new earthquake information monthly.
### Steps:
1. Import the necessary dependencies.
<img width="549" alt="Screen Shot 2022-01-24 at 8 06 23 PM" src="https://user-images.githubusercontent.com/80008461/150903583-3e748aa4-4798-4e49-83b2-6e336cdc0cd6.png">

2. Create connections to the databases.
<img width="913" alt="Screen Shot 2022-01-24 at 8 09 24 PM" src="https://user-images.githubusercontent.com/80008461/150903827-2e5e1fc6-bc5f-409a-9d6a-2ecec39db76d.png">

3. Pull data from USGS website.
<img width="1102" alt="Screen Shot 2022-01-24 at 8 37 49 PM" src="https://user-images.githubusercontent.com/80008461/150906570-f67a5e49-ed04-466e-ab3c-5355bfa5b179.png">

4. Copy data from csv or PostgreSQL (data was collected already and placed in a PostgreSQL database table) to new sqlite database created.
<img width="1105" alt="Screen Shot 2022-01-24 at 8 39 58 PM" src="https://user-images.githubusercontent.com/80008461/150906898-97c45f7e-29f0-420b-bd7d-a9aac6f76999.png">

5. Append the new data obtained from the USGS to both databases.
<img width="805" alt="Screen Shot 2022-01-24 at 8 43 07 PM" src="https://user-images.githubusercontent.com/80008461/150915935-f9c1d9a2-ec9c-44a2-bff8-0afe0ce5c7fb.png">

6. Read the data from the database tables into dataframes and check for duplicate rows and drop those values.
<img width="967" alt="Screen Shot 2022-01-24 at 10 19 21 PM" src="https://user-images.githubusercontent.com/80008461/150915897-4bd729fd-ef8f-4a41-a139-f1794dae3bdc.png">

7. Replace the tables with the new tables without duplicates and save a csv copy of the table.
<img width="827" alt="Screen Shot 2022-01-24 at 10 21 58 PM" src="https://user-images.githubusercontent.com/80008461/150916064-66127375-c14b-4253-9a9f-3e3b4dab2b08.png">

8. Work with the python file to create the API.
    - Before running the code, modify the database table to assign primary key to the id for each row of earthquake.
        - Using SQLite Studio, primary key was assigned:
        <img width="418" alt="Screen Shot 2022-01-25 at 6 05 24 PM" src="https://user-images.githubusercontent.com/80008461/151086346-a270b69c-6d29-42d5-8101-f3f5c7afa774.png">
        
        - The resulting query was generated and applied:
        ![Screen Shot 2022-01-25 at 6 19 53 PM](https://user-images.githubusercontent.com/80008461/151087101-c09e8edf-e44c-417c-9668-ffb7d800d05f.png)
        ![Screen Shot 2022-01-25 at 6 21 01 PM](https://user-images.githubusercontent.com/80008461/151087134-6e1605a6-8188-4835-b6c7-86635e93545a.png)
        ![Screen Shot 2022-01-25 at 6 21 18 PM](https://user-images.githubusercontent.com/80008461/151087156-8cd82010-8388-4399-accc-1d2e9df70216.png)

        - Run python code to test the API app is working in a development server:
        <img width="505" alt="Screen Shot 2022-01-25 at 6 23 25 PM" src="https://user-images.githubusercontent.com/80008461/151087331-553af950-899c-404a-b80c-9b79f8f0fee7.png">
        
        - Deployment with Heroku: https://earthquake-ml-app.herokuapp.com.

## Part Two: Creating the code for machine learning with data extracted from USGS and loaded to database.
### Objectives:
- Practice the best machine learning models that will work with the data use.
    - understand how things like NaN or the data type could affect a modeling approach.
- Load data from the created database and run models with it to practice connecting directly to a SQL database.

### Initial work/background:
- Choosing a ML algorithm for Earthquake Modeling:
    - **Problem**: Use obtained metrics from earthquake monitoring/measurement data from USGS to determine which of the metrics have better predictive capabilities.
    - **Goal**: Predictive. Models to be used should be supervised learning or semi-supervised.
    - **Data** (variables of interest) is numeric: Regression type of models are required for supervised learning models.
        - Data obtained from USGS can be used for training model and predict outcomes.



