import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Reading the Dataset 
df=pd.read_csv('number_of_arrests.csv')

# Perviewing the data
print(df.head())
# Now we are printing the columns within the dataset
print(df.columns)
# Determing assymmetry within dataset by finding out number of missing values
print(df.count())
# from the observed result it is clear that Notes field have missing 
# Our final result will be in the form of Correlation and for that we need to fill the - values
# number of arrests with numeric values
df[' Number of arrests '] = df[' Number of arrests '].str.replace('-','0')
# for our research it is critical to fill the missing values to generate symmetrical dataset

df['Notes'].fillna('N/A', inplace=True)
print(df['Notes'].head())
print(df[' Number of arrests '].head())

# now dropping the missing rows 
df.dropna(inplace=True)
# Now notes field also have similar number of values.
print(df.count())
# We will categorise the data on the basis of Population by ethnicity
Edf=df['Ethnicity'].value_counts()
Edf.plot(kind='bar')
plt.show()
print(Edf)
# Finding Geography wise number of arrests
Geography_Wise=df.groupby('Geography').size().sort_values(ascending = False)
Geography_Wise.plot(kind='bar',x='Geography',y='Number of arrests')
plt.show()
# We will categorise the data on the basis of Date(Yearwise)

Year_of_arrest=df.groupby('Time').size().sort_values(ascending = False)
Year_of_arrest.plot(kind='bar',x='Years',y='Number of arrests')
plt.show()
# Now calculating the person who are arrested with White colour
df1=df[df['Ethnicity']=='White']
Ethnicity_count = df1.groupby('Ethnicity').size().sort_values(ascending=False).rename('counts').reset_index()
print(Ethnicity_count['counts'].sum())
# Now calculating the person who are arrested with Other colour

df2=df[df['Ethnicity']!='White']
Ethnicity_count1 = df2.groupby('Ethnicity').size().sort_values(ascending=False).rename('counts').reset_index()
print(Ethnicity_count1['counts'].sum())

# Visualising the result of white and other colour people arrest
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
Ethnicity_Type = ['White','Others']
Val = [Ethnicity_count['counts'].sum(),Ethnicity_count1['counts'].sum()]
ax.bar(Ethnicity_Type,Val)
plt.show()

# Yearwise Plot of number of arrests of White
Year_wise_white=df1.groupby('Time').size().sort_values(ascending=False).rename('counts').reset_index()
Year_wise_white.plot(kind='bar',x='Time',y='counts')
# Yearwise arrests of non white
Year_wise_non_white=df2.groupby('Time').size().sort_values(ascending=False).rename('counts').reset_index()
Year_wise_non_white.plot(kind='bar',x='Time',y='counts')
# Finding correlation between other people and arrest

print(Ethnicity_count1.corr(method='kendall'))