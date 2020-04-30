# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 19:51:27 2020

@author: prego-j
"""

from scipy import stats
import statsmodels.api as sm
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np


data = pd.read_csv('final.csv')
df = pd.DataFrame(data,columns = ['Time','Sales','Advertising','Price','Competitor_Advertising'])


#df.hist()
Ad = pd.DataFrame(df['Advertising'])
Sales = pd.DataFrame(df['Sales'])


#plt = df.plot(x = 'Advertising', y = 'Sales', kind = 'scatter')


model = LinearRegression()

df.insert (4,'LnSales',np.log(df['Sales']),False)
df.insert(5,'Ln(Ad)',np.log(df['Advertising']),False)
df.insert(6,'Ln(Comp)',np.log(df['Competitor_Advertising']),False)
df.insert(7,'Ln(Price)',np.log(df['Price']),False)

print(df)

LnSales = pd.DataFrame(df['LnSales'])
LnAd = pd.DataFrame(df['Ln(Ad)'])
LnComp = pd.DataFrame(df['Ln(Comp)'])
LnPrice = pd.DataFrame(df['Ln(Price)'])

##MODEL 1     ########################################################################

X1 = pd.DataFrame(np.c_[df['Ln(Ad)'],df['Ln(Price)']],columns = ['Ln(Ad)','Ln(Price)']) 

model.fit(X1,LnSales)
r_sque =  model.score(X1,LnSales)

print('Model 1')
print('Ln(Ad), Ln(Price) vs. Ln(Sales):''\n\n''R_sque:', r_sque)
print('Intercept:', model.intercept_)
print('Elasticity:', model.coef_)
#p-value
c1 = sm.add_constant(X1)
est = sm.OLS(LnSales,c1)
print('Model 1 p-value:',est.fit().f_pvalue)

##MODEL 2    ########################################################################


X2 = pd.DataFrame(np.c_[df['Ln(Ad)'],df['Ln(Comp)'],df['Ln(Price)']],columns = ['Ln(Ad)','Ln(Comp)','Ln(Price)']) 


model.fit(X2,LnSales)
r_sque =  model.score(X2,LnSales)
print('\n')
print('Model 2')
print('Ln(Ad),Ln(Comp),Ln(Price) vs. Ln(Sales):''\n\n''R_sque:', r_sque)
print('Intercept:', model.intercept_)
print('Elasticity:', model.coef_)
#p-values
c2 = sm.add_constant(X2)
est = sm.OLS(LnSales,c2)
print('Model 2 p-value:',est.fit().f_pvalue)



##MODEL 3########################################################################

X3 = pd.DataFrame(np.c_[df['Ln(Ad)'],df['Ln(Comp)'],df['Ln(Price)'],df['Time']],columns = ['Ln(Ad)','Ln(Comp)','Ln(Price)','Time']) 


model.fit(X3,LnSales)
r_sque =  model.score(X3,LnSales)
print('\n')
print('Model 3')
print('Ln(Ad),Ln(Comp),Ln(Price),Time vs. Ln(Sales):''\n\n''R_sque:', r_sque)
print('Intercept:', model.intercept_)
print('Elasticity:', model.coef_)
#p-values
c3 = sm.add_constant(X3)
est = sm.OLS(LnSales,c3)
print('Model 3 p-value:',est.fit().f_pvalue)


##############################################################################























