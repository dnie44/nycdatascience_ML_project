import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn import linear_model

ah = pd.read_csv('Ames_Housing_Price_Data.csv', index_col=0,low_memory=False)
ar = pd.read_csv('Ames_Real_Estate_Data.csv', index_col=0,low_memory=False)


#---------------------------------------- SEPARATE TARGET VARIABLE -----------------------------#
sale_p = ah.SalePrice
#-----------------------------------------------------------------------------------------------#

#---------------------------------------- DROP COLS WITH HIGH MISSINGNESS ----------------------#
ah = ah.drop(['Alley','FireplaceQu','PoolQC','Fence','MiscFeature','MiscVal','SalePrice'],axis=1)
#-----------------------------------------------------------------------------------------------#

#---------------------------------------- FIND MISSING DATA ------------------------------------#
missingRows = ah.isnull().any(axis=1)
missingCols = ah.isnull().any(axis=0)
#-----------------------------------------------------------------------------------------------#

#---------------------------------------- REMOVE ROWS WITH NAs ---------------------------------#
ah = ah[~missingRows]
#-----------------------------------------------------------------------------------------------#

#---------------------------------------- ORGANIZE CATAGORICAL FEATURES ------------------------#
categorical = ah[['MSZoning','Street','LotShape','LandContour','Utilities','LotConfig','LandSlope','Neighborhood',
'Condition1','Condition2','BldgType','HouseStyle','OverallQual','OverallCond','YearBuilt','YearRemodAdd','RoofStyle',
'RoofMatl','Exterior1st','Exterior2nd','MasVnrType','ExterQual','ExterCond','Foundation','BsmtQual','BsmtCond','BsmtExposure',
'BsmtFinType1','BsmtFinType2','Heating','HeatingQC','CentralAir','Electrical','BsmtFullBath','BsmtHalfBath','FullBath','HalfBath','BedroomAbvGr',
'KitchenAbvGr','KitchenQual','Functional','Fireplaces','GarageType','GarageFinish','GarageQual','GarageCond','PavedDrive','SaleType','SaleCondition']]

# for feature in categorical:
#     print(ah[feature].value_counts())
#     print('')
#-----------------------------------------------------------------------------------------------#
























# print('The columns with missingness are %s' %(ah.columns[missingCols]))
# print('The columns with missingness are %s' %(ah.columns[missingCols]))