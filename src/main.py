# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 14:05:28 2018

@author: Martin
"""

# importation des library 

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing
from sklearn import datasets
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import linear_model


# importation de mon dict nommé valeur
from dictionnary import*
# chargement des data
data_train=pd.read_csv("../data/train.csv")

# séparation des features selon qualitatives ou quantitatives
def separated_qualitativeVSquantitative (data):
    feature=data.columns
    objet_features=[]
    number_features=[]
    for col in feature:
        if data[col].dtype=="object":
            objet_features.append(col)
        else:
            number_features.append(col)
    # data quantitative
    data_feature_digital=data.loc[:,number_features]
    # data qualitative
    data_feature_qualitatives=data.loc[:,objet_features]
    return (data_feature_digital,data_feature_qualitatives)

data_feature_digital,data_feature_qualitatives=separated_qualitativeVSquantitative(data_train)
# data quantitative

def selections_Y(data,nom_du_Y):
    y=data.loc[:,[nom_du_Y]]
    return y

y=selections_Y(data_feature_digital,"SalePrice")

# traitement des donnees quantitatives
#data_feature_digital.info()
#feature_na=["LotFrontage","MasVnrArea","GarageYrBlt"]
#data_digital_nan=data_feature_digital.drop(columns=feature_na)
def selection_tenth_feature_most_correlative(data):
    correlation=data.corr(method='pearson')
    correlation = correlation['SalePrice'].abs().sort_values(ascending= False)
    print(correlation)
    # ajout de la matrice
   
    
selection_tenth_feature_most_correlative(data_feature_digital)
 


interesting_numeric_variable=data_train.loc[:,["Id","OverallQual","GrLivArea","GarageCars","GarageArea",
                                               "TotalBsmtSF","1stFlrSF","FullBath","TotRmsAbvGrd","YearBuilt"]]

interesting_numeric_variable=interesting_numeric_variable.rename(columns={"OverallQual":"Quality_house","GrLivArea" : "superficieMaison","GarageCars":"Capacite_garage_voiture",
                                                                          "GarageArea":"superficie_garage","TotalBsmtSF":"superfice_sousol","1stFlrSF":"superficie_rdc",
                                                                          "FullBath":"NbrsSDB","TotRmsAbvGrd":"nmbrePiece","YearBuilt":"anneeConstruction"})
data_train=data_train.rename(columns={"OverallQual":"Quality_house","GrLivArea" : "superficieMaison","GarageCars":"Capacite_garage_voiture",
                                                                          "GarageArea":"superficie_garage","TotalBsmtSF":"superfice_sousol","1stFlrSF":"superficie_rdc",
                                                                          "FullBath":"NbrsSDB","TotRmsAbvGrd":"nmbrePiece","YearBuilt":"anneeConstruction"})

print( "les 10 premières features les plus corrélées : ")
print(interesting_numeric_variable.columns)


#visualisation de ses features

def scatter_numerical_variables_and_saleprice(data, col):
    Grid_SalePrice = pd.concat([data["SalePrice"], data[col]], axis=1)
    Grid_SalePrice.plot.scatter(x=col, y='SalePrice')
    
#afficher les graphiques
for feature in interesting_numeric_variable:
    scatter_numerical_variables_and_saleprice(data_train,feature)
    

# traitement donnees test
test_n=pd.read_csv("../data/test.csv")
test=test_n.loc[:,["Id","OverallQual","GrLivArea","GarageCars","GarageArea",
                                               "TotalBsmtSF","1stFlrSF","FullBath","TotRmsAbvGrd","YearBuilt",]]
def na_rows(df):
    return df.columns[df.isna().any()] 

## remplace les NAN par 0 car pas de garage ni sous-sol
test=test.fillna(0)
print(interesting_numeric_variable)
#

def model_data_test(X,Y,model_pred): 
    X_train, X_test, y_train, y_test = train_test_split(X,Y, test_size=0.3, random_state=0)
    model = model_pred
    model.fit(X_train, y_train)
        # check the accuracy on the training set
    accuracy_train=model.score(X_train, y_train)
    print("the accurucy on the training set is %f"%(accuracy_train))
    predi=model.predict(X_test)
    accuracy_test=model.score(X_test,y_test)
    print(X_test.columns)
    print("the accurucy on the tesx set is %f"%(accuracy_test))
    
model_data_test(interesting_numeric_variable,y,linear_model.LinearRegression())

# Appliquer le modèle sur les données test et création d'un fichier pour Kaggle 


def prediction_test_tocsv(Y_test,model_entrainé,f_output):
    predict =model_entrainé.predict(test)
    houses_id = pd.DataFrame(Y_test['Id'])
    data = pd.DataFrame({'Id' :Y_test.Id,'SalePrice' : np.reshape(predict, (-1))})
    data = data.set_index('Id')
    title=f_output
    data.to_csv('../output/'+title)
    print (" Le fichier ",title," a été creer et est prêt pour une soumission Kaggle")

prediction_test_tocsv(test,model,'fichtest.csv')

# nettoyer données qualitative

#def Encoding_qualitatives_feature(data)
for col in data_feature_qualitatives.columns:
        col_type = data_feature_qualitatives[col].dtype
        if col_type == 'object' and col in valeur:
            #p(col+' unique',unique)
            if valeur[col]['type'] == 'num':
                map_array = valeur[col]['values']
                print('map_array',map_array)
                #to_map = dict(zip(map_array[::-1],range(len(map_array))))
                data_train[col] = data_train[col].map(map_array)
            elif valeur[col]['type'] == 'onehot':
                data_train = pd.concat([data_train, pd.get_dummies(data_train[col], prefix=col)], axis=1)
                data_train = data_train.drop(col, axis=1)
            else:
                print('unrecognized type!!!!!!!')

print(data_train)
#
#  