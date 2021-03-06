import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn import linear_model

ah = pd.read_csv('Ames_Housing_Price_Data.csv', index_col=0,low_memory=False)
ar = pd.read_csv('Ames_Real_Estate_Data.csv', index_col=0,low_memory=False)

#---------------------------------------- FIND MISSING DATA ------------------------------------#
missingRows = ah.isnull().any(axis=1)
missingCols = ah.isnull().any(axis=0)
#-----------------------------------------------------------------------------------------------#

#---------------------------------------- DROP COLS WITH HIGH MISSINGNESS ----------------------#
ah = ah.drop(['Alley','FireplaceQu','PoolQC','Fence','MiscFeature','MiscVal'],axis=1)
#-----------------------------------------------------------------------------------------------#

#---------------------------------------- REMOVE ROWS WITH NAs ---------------------------------#
# ah = ah[~missingRows]
#-----------------------------------------------------------------------------------------------#

#---------------------------------------- SEPARATE TARGET VARIABLE -----------------------------#
sale_p = ah.SalePrice
#-----------------------------------------------------------------------------------------------#

#---------------------------------------- ORGANIZE CATAGORICAL FEATURES ------------------------#
# categorical = ah[['MSZoning','Street','LotShape','LandContour','Utilities','LotConfig','LandSlope','Neighborhood',
# 'Condition1','Condition2','BldgType','HouseStyle','OverallQual','OverallCond','YearBuilt','YearRemodAdd','RoofStyle',
# 'RoofMatl','Exterior1st','Exterior2nd','MasVnrType','ExterQual','ExterCond','Foundation','BsmtQual','BsmtCond','BsmtExposure',
# 'BsmtFinType1','BsmtFinType2','Heating','HeatingQC','CentralAir','Electrical','BsmtFullBath','BsmtHalfBath','FullBath','HalfBath','BedroomAbvGr',
# 'KitchenAbvGr','KitchenQual','Functional','Fireplaces','GarageType','GarageFinish','GarageQual','GarageCond','PavedDrive','SaleType','SaleCondition']]
#-----------------------------------------------------------------------------------------------#

#---------------------------------------- neighborhoods to section of town ---------------------#
hoods = ah['Neighborhood']
new_hoods = []

for neigh in hoods :
	if neigh == 'Blueste' :
		new_hoods.append('SW')
	elif neigh == 'Blmngtn' :
		new_hoods.append('NO')
	elif neigh == 'BrDale' :
		new_hoods.append('NO')
	elif neigh == 'BrkSide' :
		new_hoods.append('DT')
	elif neigh == 'ClearCr' :
		new_hoods.append('NO')
	elif neigh == 'CollgCr' :
		new_hoods.append('SW')
	elif neigh == 'Crawfor' :
		new_hoods.append('SW')
	elif neigh == 'Edwards' :
		new_hoods.append('SW')
	elif neigh == 'Gilbert' :
		new_hoods.append('NO')
	elif neigh == 'IDOTRR' :
		new_hoods.append('DT')
	elif neigh == 'MeadowV' :
		new_hoods.append('SE')
	elif neigh == 'Mitchel' :
		new_hoods.append('SE')
	elif neigh == 'NAmes' :
		new_hoods.append('NO')
	elif neigh == 'NoRidge' :
		new_hoods.append('NW')
	elif neigh == 'NPkVill' :
		new_hoods.append('NO')
	elif neigh == 'NridgHt' :
		new_hoods.append('NW')
	elif neigh == 'NWAmes' :
		new_hoods.append('NO')
	elif neigh == 'OldTown' :
		new_hoods.append('DT')
	elif neigh == 'SWISU' :
		new_hoods.append('SW')
	elif neigh == 'Sawyer' :
		new_hoods.append('NW')
	elif neigh == 'SawyerW' :
		new_hoods.append('NW')
	elif neigh == 'Somerst' :
		new_hoods.append('NW')
	elif neigh == 'StoneBr' :
		new_hoods.append('NO')
	elif neigh == 'Timber' :
		new_hoods.append('SW')
	elif neigh == 'Veenker' :
		new_hoods.append('NW')
	elif neigh == 'Greens' :
		new_hoods.append('NW')
	elif neigh == 'GrnHill' :
		new_hoods.append('SO')
	elif neigh == 'Landmrk' :
		new_hoods.append('DT')
	else : print('no match')

ah['city_sec'] = new_hoods 
#-----------------------------------------------------------------------------------------------#

#---------------------------------------- central air to 1 and 0s ------------------------------#
ah['CentralAir'] = ah['CentralAir'].map(lambda x: 0 if x == 'N' else 1)
#-----------------------------------------------------------------------------------------------#

#---------------------------------------- does house have fireplace? -> 1 and 0 ----------------#
ah['gotFire'] = ah['Fireplaces'].map(lambda x: 1 if x >= 1 else 0)
#-----------------------------------------------------------------------------------------------#

#---------------------------------------- simple feature list for test logistic reg ------------#
simpFeatures = ah[['CentralAir','gotFire']]
#-----------------------------------------------------------------------------------------------#

#---------------------------------------- need to do preprocessing before fitting --------------#
# logistic = LogisticRegression(C=1e4, solver='lbfgs', multi_class='auto')
# logistic.fit(simpFeatures,sale_p)
# print(logistic.score(simpFeatures,sale_p))
# /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/sklearn/linear_model/_logistic.py:814: ConvergenceWarning: lbfgs failed to converge (status=1):
# STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.
# Increase the number of iterations (max_iter) or scale the data as shown in:
#     https://scikit-learn.org/stable/modules/preprocessing.html
#-----------------------------------------------------------------------------------------------#