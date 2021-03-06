## Home Improvement Machine Learning: Predicting House Price After Renovation
#### NYCdatascience machine learning project

Ames is a small city in Iowa with a population of about 65,000 and is the college town of Iowa State University. The Ames housing dataset consists of 2578 house records and includes sale prices and individual house attributes.

The project seeks to predict house prices and the affect of home improvement or renovations on the value of the house. The final product is an online tool for estimating the value of specific home improvements such as remodeling the kitchen or garage, finishing the basement, or adding a bathroom.

The project stakeholders include:
* Real estate agencies using the model as an extra value added service to homeowners
* Used by renovation contractors or home improvement retailers to let customers know the increase in house value after construction
* Homeowners looking to renovate and determine a reasonable price to pay

After rigorous EDA, feature selection and feature engineering, predictions were tested using various models including penalized linear regression, random forest, and various gradient boosting algorithms (SciKit-learn GBR, CatBoost, LightGBM, XGBoost). The final model used in the home renovation app uses [Catboost](https://catboost.ai/).<br> 
Click [here](https://share.streamlit.io/dnie44/nycdatascience_ml_app/app.py) to try the app.
<br>

Presentation slides: [here](https://docs.google.com/presentation/d/1b0HYMokVrJFnWw82tkU5d0Oeu4p8LNlKCCadrlv9b2M/)

### Project Collaborators
[Daniel Nie](https://github.com/dnie44)<br>
[David Kressley](https://github.com/Skipp-py)<br>
[Karl Lundquist](https://github.com/klundquist)<br>
[Tony Pennoyer](https://github.com/tonypennoyer)<br>

### Acknowledgements
* The [Ames Housing dataset](https://www.kaggle.com/c/house-prices-advanced-regression-techniques) compiled by Dean De Cock<br>
* Ames city sectors as per the Ames Convention & Visitors Bureau (https://www.thinkames.com/maps/) <br>

***webapp url***: https://share.streamlit.io/dnie44/nycdatascience_ml_app/app.py <br>
*webapp git*: https://github.com/dnie44/nycdatascience_ML_app.git

