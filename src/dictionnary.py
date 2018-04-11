# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 15:09:20 2018

@author: Martin
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 15:13:12 2018
@author: Martin
"""

valeur = {}

valeur['MSZoning'] = { 
 
 'values' : {
		
       'A':0, 
       'C':1,
       'FV':2,
       'I':3,
       'RH':4,
       'RL':5,
       'RP':6,
       'RM':7
},
'type':'onehot'
}

valeur['Street'] = { 
 
 'values' : {
       'Grvl':0,
       'Pave':1
},
'type':'num'
}
       	
valeur['Alley'] = { 
 
 'values' : {

       'Grvl':0,
       'Pave':1,
       'nan':-1
},
'type':'num'
}

valeur['LotShape'] = { 
 
 'values' : {
       'Reg' : 0,
       'IR1' : 1,
       'IR2' : 2,
       'IR3' : 3 
},
'type':'num'
}

valeur['LandContour'] = { 
 
 'values' : {

       'Lvl': 0,
       'Bnk': 1,
       'HLS': 2,
       'Low': 3
},
'type':'num'
}
		
valeur['Utilities'] = { 
 
 'values' : {
       'AllPub' : 0,
       'NoSeWa' : 1
},
'type':'num'
}
    	
	
valeur['LotConfig'] = { 
 
 'values' : {

       'Inside': 0,
       'Corner': 1,
       'CulDSac': 2,
       'FR2': 3,
       'FR3': 4 
},
'type':'onehot'
} 
	
valeur['LandSlope'] = { 
 
 'values' : {
		
       'Gtl':0,
       'Mod':1,
       'Sev':2
},
'type':'num'
}
	
valeur['Neighborhood'] = { 
 
 'values' : {

       'Blmngtn':0,
       'Blueste':1,
       'BrDale':2,
       'BrkSide':3,
       'ClearCr':4,
       'CollgCr':5,
       'Crawfor':6,
       'Edwards':7,
       'Gilbert':8,
       'IDOTRR':9,
       'MeadowV':10,
       'Mitchel':11,
       'Names':12,
       'NoRidge':13,
       'NPkVill':14,
       'NridgHt':15,
       'NWAmes':16,
       'OldTown':17,
       'SWISU':18,
       'Sawyer':19,
       'SawyerW':20,
       'Somerst':21,
       'StoneBr':22,
       'Timber':23,
       'Veenker':24
},
'type':'onehot'
}
			
valeur['Condition1'] = { 
 
 'values' : {
	
       'Artery' : 0,
       'Feedr' : 1,
       'Norm' : 2,
       'RRNn' : 3,
       'RRAn' : 4,
       'PosN' : 5,
       'PosA' : 6,
       'RRNe' : 7,
       'RRAe' : 8
},
'type':'onehot'
}

valeur['Condition2'] = { 
 
 'values' : {
		
       'Artery':0,
       'Feedr':1,
       'Norm':2,
       'RRNn':3,
       'RRAn':4,
       'PosN':5,
       'PosA':6,
       'RRNe':7,
       'RRAe':8
},
'type':'onehot'
}
	
valeur['BldgType'] = { 
 
 'values' : {
		
       '1Fam': 0,
       '2FmCon': 1,
       'Duplx': 2,
       'TwnhsE': 3,
       'TwnhsI': 4,
},
'type':'num'
}
       
	
valeur['HouseStyle'] = { 
 
 'values' : {
       '1Story':0,
       '1.5Fin':1,
       '1.5Unf':2,
       '2Story':3,
       '2.5Fin':4,
       '2.5Unf':5,
       'SFoyer':6,
       'SLvl':7
},
'type':'num'
}
	
valeur['RoofStyle'] = { 
 'values' : {

       'Flat' : 0,
       'Gable' : 1,
       'Gambrel' : 2,
       'Hip': 3,
       'Mansard' : 4,
       'Shed' : 5
},
'type':'num'
}
		
valeur['RoofMatl'] = { 
 
 'values' : {

       'ClyTile': 0,
       'CompShg': 1,
       'Membran': 2,
       'Metal': 3,
       'Roll': 4,
       'Tar&Grv': 5,
       'WdShake': 6,
       'WdShngl': 7
},
'type':'onehot'
}

		
valeur['Exterior1st'] = { 
 
 'values' : {

       'AsbShng' : 0,
       'AsphShn' : 1,
       'BrkComm': 2,
       'BrkFace' : 3,
       'CBlock' : 4,
       'CemntBd' : 5,
       'HdBoard' : 6,
       'ImStucc' : 7,
       'MetalSd' : 8,
       'Other' : 9,
       'Plywood' : 10,
       'PreCast' : 11,
       'Stone' : 12,
       'Stucco' : 13,
       'VinylSd' : 14,
       'Wd Sdng' : 15,
       'WdShing' : 16
},
'type':'onehot'
}

	
valeur['Exterior2nd'] = { 
 
 'values' : {

       'AsbShng' : 0,
       'AsphShn' : 1,
       'BrkComm' : 2,
       'BrkFace' : 3,
       'CBlock' : 4,
       'CemntBd' : 5,
       'HdBoard' : 6,
       'ImStucc' : 7,
       'MetalSd' : 8,
       'Other' : 9,
       'Plywood' : 10,
       'PreCast' : 11,
       'Stone' : 12,
       'Stucco' : 13,
       'VinylSd' : 14,
       'Wd Sdng' : 15,
       'WdShing' : 16
},
'type':'onehot'
}
	
valeur['MasVnrType'] = { 
    'values' : {
    
        'BrkFace':1,
        'BrkCmn':0,
       'CBlock':2,
       'None':3,
       'Stone':4
},
'type':'onehot'
}
	

valeur['ExterQual'] = { 
 
 'values' : {
		
       'Ex' : 4,
       'Gd' : 3,
       'TA' : 2,
       'Fa' : 1,
       'Po' : 0
},
'type':'num'
}
		
valeur['ExterCond'] = { 
 
 'values' : {

       'Ex' : 4,
       'Gd' : 3,
       'TA' : 2,
       'Fa' : 1,
       'Po' : 0
},
'type':'num'
}	
    
		
valeur['Foundation'] = { 
 
 'values' : {
		
       'BrkTil' : 0,
       'CBlock' : 1,
       'PConc' : 2,
       'Slab' : 3,
       'Stone' : 4,
       'Wood' : 5
},
'type':'onehot'
}
		
valeur['BsmtQual'] = { 
 
 'values' : {
       
       'Ex' : 4,
       'Gd' : 3,
       'TA' : 2,
       'Fa' : 1,
       'Po' : 0,
       'NA' : -1
},
'type':'num'
}

		
valeur['BsmtCond'] = { 
 
 'values' : {

  
       'Ex' : 4,
       'Gd' : 3,
       'TA' : 2,
       'Fa' : 1,
       'Po' : 0,
       'NA' : -1
},
'type':'num'
}
	
valeur['BsmtExposure'] = { 
 
 'values' : {

       'Gd' : 3,
       'Av'  : 2,
       'Mn' : 1,
       'No' : 0,
       'NA' : -1
},
'type':'num'
}
	
valeur['BsmtFinType1'] = { 
 
 'values' : {

       'GLQ' : 5,
       'ALQ' : 4,
       'BLQ' : 3,
       'Rec' : 2,
       'LwQ' : 1,
       'Unf' : 0,
       'NA' : -1
},
'type':'onehot'
}
		

valeur['BsmtFinType2'] = { 
 
 'values' : {


       'GLQ' : 5,
       'ALQ' : 4,
       'BLQ' : 3,
       'Rec' : 2,
       'LwQ' : 1,
       'Unf' : 0,
       'NA' : -1
},
'type':'onehot'
}
valeur['Heating'] = { 
 
 'values' : {
		
       'GasA' : 0,
       'Floor' : 1,
       'GasW' : 2,
       'Grav' : 3,
       'OthW' : 4,
       'Wall' : 5
},
'type':'onehot'
}

valeur['HeatingQC'] = { 
 
 'values' : {

       'Ex' : 4,
       'Gd' : 3,
       'TA' : 2,
       'Fa' : 1,
       'Po' : 0,
},
'type':'num'
}
      

		
valeur['CentralAir'] = { 
 
 'values' : {

       'N': 0,
       'Y': 1
},
'type':'num'
}
		
valeur['Electrical'] = { 

 'values' : {

       'SBrkr':0,
       'FuseA':1,
       'FuseF':2,
       'FuseP':3,
       'Mix':4
},
'type':'onehot'
}

valeur['KitchenQual'] = { 
 
 'values' : {

       'Ex' : 4,
       'Gd' : 3,
       'TA' : 2,
       'Fa' : 1,
       'Po' : 0
},
'type':'num'
}

      

valeur['Functional'] = { 
 
 'values' : {

       'Typ':0,
       'Min2': 1,
       'Mod': 2,
       'Maj1': 3,
       'Maj2': 4,
       'Sev': 5,
       'Sal': 6
},
'type':'num'
}
	
valeur['FireplaceQu'] = { 
 
 'values' : {

       'Ex' : 4,
       'Gd' : 3,
       'TA' : 2,
       'Fa' : 1,
       'Po' : 0,
       'NA' : -1
},
'type':'num'
}

valeur['GarageType'] = { 
 
 'values' : {
		
       '2Types' : 6,
       'Attchd' : 5,
       'Basment' : 4,
       'BuiltIn' : 3,
       'CarPort' : 2,
       'Detchd' : 1,
       'NA' : 0 
},
'type':'onehot'
}
		
		
valeur['GarageFinish'] = { 
 
 'values' : {

       'Fin': 3,
       'RFn': 2,
       'Unf': 1,
       'NA': 0
},
'type':'num'
}
	
valeur['GarageQual'] = { 
 
 'values' : {

       'Ex' : 4,
       'Gd' : 3,
       'TA' : 2,
       'Fa' : 1,
       'Po' : 0,
       'NA' : -1
},
'type':'num'
}
	
valeur['GarageCond'] = { 
 
 'values' : {

       'Ex' : 4,
       'Gd' : 3,
       'TA' : 2,
       'Fa' : 1,
       'Po' : 0,
       'NA' : -1
},
'type':'num'
}
		
valeur['PavedDrive'] = { 
 
 'values' : {

       'Y' : 0,
       'P' : 1,
       'N' : 2
       },
       'type':'onehot'
}
		


valeur['PoolQC'] = { 
 
 'values' : {

       'Ex' : 4,
       'Gd' : 3,
       'TA' : 2,
       'Fa' : 1,
       'NA' : 0
},
'type':'num'
}
		
valeur['Fence'] = { 
 
 'values' : {
		
       'GdPrv' : 3, 
       'MnPrv' : 2, 
       'GdWo' : 1, 
       'MnWw' : 0, 
       'NA' : -1 
},
'type':'num'
}
	
valeur['MiscFeature'] = { 
 
 'values' : {
		
       'Elev' : 4,
       'Gar2' : 3,
       'Othr' : 2,
       'Shed' : 1,
       'TenC' : 0,
       'NA' : -1
       },
       'type':'num'
       }


valeur['SaleType'] = { 
 
 'values' : {
		
       'WD': 0,
       'CWD': 1,
       'VWD': 2,
       'New': 3,
       'COD': 4,
       'Con':5,
       'ConLw': 6,
       'ConLI': 7,
       'ConLD': 8,
       'Oth': 9
  },
       'type':'num'
       }

valeur['SaleCondition'] = { 
 
 'values' : {

       'Normal': 0,
       'Abnorml': 1,
       'AdjLand': 2,
       'Alloca': 3,
       'Family': 4,
       'Partial': 5
},
       'type':'num'
}