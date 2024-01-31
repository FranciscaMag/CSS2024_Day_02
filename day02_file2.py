# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:53:31 2024

@author: Francisca Thimothy
"""

import pandas as pd
file =pd.read_csv("iris.csv")

"""
Absolute path:
    data_02/iris.csv
    """
    
#column_names = ['sepal_length', 'sepal_width', 'petal_length', 'class']
 #look up hoqw to add column name (from google)
 
#file = pd.read_csv("C:/Users/Francisca Thimothy/CSS2024_Day02/Geospatial Data.txt", sep=";")

#file = pd.read_excel("Geospatial Data.txt")
#file = pd.read_json("C:/Users/Francisca Thimothy/CSS2024_Day02/student_data.json")
print (file)

url="https://github.com/Asabele240701/css4_day02/blob/main/effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv"
#df = dataframe


df = pd.read_csv("country_data_index.csv", index_col=0)

df = pd.read_excel("residentdoctors.xlsx")
print(df)

df["LOWER_AGE"] = df["AGEDIST"]. str.extract ( '(\d+)-')
print(df.info())

x = [1,2,3]
y = x[1:]
print(y)

x = {'a': 1, 'b': 2}
x.update({'c': 3})
print(x)

x = {'a': 1, 'b': 2}
x.update({'c': 3})
print(x)

x = [1,2,3]
y = x[1:]
print(y)

x = {'a': 1, 'b': 2}
del x['a']
print(x)


"""
Regular expressions
"""

"""working with dates
"""

df = pd.read_csv("time_series_data.csv")
df = pd.read_csv("time_series_data.csv" ,index_col=0)
print(df.info())

df['Date'] = pd.to_datetime(df['Date'])
print(df.info())

df['Date'] = pd.to_datetime(df['Date'],format ="%d-%m-%Y")
print(df.info())

df['Year'] = df ['Date'].dt.year

"""
.str
.extract
.astype
"""

df = pd.read_csv("patient_data_dates.csv")


df = pd.read_csv("patient_data_dates.csv" , index_col=0)
print(df.info())
df.drop(index=26, inplace=True)
df['Date'] = pd.to_datetime(df['Date'])
print(df.info())

avg_cal = df ["Calories"].mean()
df["Calories"].fillna(avg_cal, inplace =True)

"""
best practices
"""
df.dropna(inplace = True)

df.loc[7,'Duration'] = 45
df = df.reset_index(drop=True)


df['Duration'] = df['Duration'].replace([450],50)
print(df)

#df.loc[7, 'Duration'] = 45

#pd. set_option('display.max_rows' , None)
df = pd.read_csv("C:/Users/Francisca Thimothy/CSS2024_Day02/iris.csv")
print(df.columns)

col_names = df.columns.tolist()
print(col_names)


df["sepal_length_sq"] = df["sepal_length"]**2


df["sepal_length_sq"] = df["sepal_length"].apply(lambda x: x**2)


grouped = df.groupby("class")
mean_square_values = grouped["sepal_length_sq"].mean()
print(mean_square_values)


df1 = pd.read_csv("data_o2/person_split1.csv")
df2 = pd.read_csv("data_o2/person_split1.csv")


####################
df1 = pd.read_csv('person_work.csv')
df2 = pd.read_csv('person_education.csv')
df_merge = pd.merge(df1,df2,on="id")

df["class"] = df["class"].str.replace("Iris-", "")


sepal_abv_5 = df[df['sepal_length'] > 5]
df = df[df['sepal_length'] > 5]

df= df[df["class"] == "virginica"]

df.to_csv("pulsar.csv")

url = "https://raw.githubusercontent.com/alexandrehsd/Predicting-Pulsar-Stars/master/pulsar_stars.csv"
df = pd.read_csv(url)















