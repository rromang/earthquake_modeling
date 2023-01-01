# Machine Learning Regressions for the Prediction of Earthquake Characteristics/Features
----------------------------


### Note: Part of the inspiration/ideas for some of the modeling machine learning code came from: https://www.kaggle.com/chenzecharya/earthquake-random-forest.

## Creating the code for machine learning with data extracted from USGS and loaded to database.
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

----------------------------

### Results from Extra Trees Regression Model

![extratrees_lat_linear_sns](https://user-images.githubusercontent.com/80008461/210184747-2ed178e5-115a-422b-82c5-83b594bc03e2.png)
Linear regression for the actual vs predicted values in model that was fed with magnitude, longitude, depth and, time as features to predict the latitude.

![extratrees_lon_linear_sns](https://user-images.githubusercontent.com/80008461/210184816-da964234-7b2a-4469-bcc3-6f598ca38284.png)
Linear regression for the the actual vs predicted values in model that was fed with magnitude, latitude, depth and, time as features to predict the longitude.

![extratrees_mag_linear_sns](https://user-images.githubusercontent.com/80008461/210184835-06fd38fb-be1a-4f1b-a127-8bdd44d52b38.png)
Linear regression for the actual vs predicted values in the model that was fed with longitude, latitude, depth and, time as features to predict the magnitude.

The same process was done for predicting time using latitude, longitude, depth and magnitude. As expected, the model was not able to perform well with an R-squared of 0.029. For the other features the performed decently and was the regression of actual vs predicted values was relatively good. However, the magnitude error showed that the accuracy was not as good for these 2 features.
