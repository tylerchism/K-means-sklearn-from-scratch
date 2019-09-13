import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np 
from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd 

'''
Pclass Passenger Class (1 = 1st; 2 = 2nd; 3 = 3rd)
survival Survival (0 = No; 1 = Yes)
name Name
sex Sex
age Age
sibsp Number of Siblings/Spouses Aboard
parch Number of Parents/Children Aboard
ticket Ticket Number
fare Passenger Fare (British pound)
cabin Cabin
embarked Port of Embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)
boat Lifeboat
body Body Identification Number
home.dest Home/Destination
'''

df = pd.read_excel('titanic.xls')

## shows data types and in particular if there are any objects
## which are not numerical values but things like sex
#print(df.dtypes)

print(df.head())

df.drop(['body', 'name'], 1, inplace=True)


