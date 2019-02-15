from sklearn import model_selection
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("temp.xls")
#print(df.iloc[:,:13])

df2 = df.iloc[:,1:13]
#print(df2)
df['Max'] = df2.max(axis=1)
df['Min'] = df2.min(axis=1)
#print(df)
print(df2.columns)

year = df["YEAR"]
Max = df["Max"]
Min = df["Min"]
#plt.plot(year, Max)
#plt.scatter(x = year, y = Max, alpha=0.8, edgecolors='r', s=30)
Max.plot()
#df.hist(Max)

'''#plt.plot(year, Max, 'b-', label='Maximum')
#plt.plot(year, Min, 'g-', label='Minimum')

# Create legend.
plt.legend(loc='upper left')
plt.xlabel('Year')
plt.ylabel('Temperature (C)')'''

'''pqr = df2.columns
print(pqr.size)
row = df2.iloc[116:117,:]
print(row)
row.plot(kind='bar')'''
plt.show()