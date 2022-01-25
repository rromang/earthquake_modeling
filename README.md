# Machine Learning Regressions for the Prediction of Earthquake Characteristics/Features

## WORK IN PROGRESS!!

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



