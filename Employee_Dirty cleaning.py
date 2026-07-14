#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.io.pytables import dropna_doc
#%%
data = pd.read_csv(r"C:\Users\USER\Downloads\employees_dirty_1000.csv")
data.head(10)
#%%
data.shape
#%%
data.dtypes
#%%
null_data = data.isnull().sum()
null_data
#%%
data.columns=(
    data.columns
    .str.replace(' ', ' _ ')
    .str.upper()
    .str.strip()
)
data.columns
#%%
data.head(5)
#%%
data.replace = data.fillna({"FULL_*_NAME":"UNKNOWN_PERSON"})
print(data.replace)
#%%
print(data.replace)
data.head(5)
#%%
#Replace Nan with customise value
data['FULL_NAME'] = data['FULL_NAME'].fillna('Unknown.person')

data['PHONE'] = data['PHONE'].fillna('ooooo-ooooo')

data['SALARY'] = data['SALARY'].fillna(data['SALARY'].median())

data.head(20)
#%%
count = (data['FULL_NAME'] == 'Unknown Person').count()
print("Unknown Person count:", count)
#%%
#Remove empty hire date

data = data.dropna(subset=['HIRE_DATE'])
print("Rows after dropping empty HIRE_DATE:", len(data))
#%%
print("Duplicates count:", data.duplicated().sum())

#%%
data = data.drop_duplicates()
print("Rows after dropping duplicate:", len(data))
#%%
clean = data.isnull().sum()
clean
#%%
data['EMAIL'] = data['EMAIL'].fillna('Unknown@gmail.com')
data['EMAIL'] = data['EMAIL'].str.lower()
data.head(10)
#%%

#%%
data['STATUS']=data['STATUS'].str.title()
data['STATUS']
data.head(20)
#%%
print(np.unique(data['STATUS']))
#%%
print(np.sum(data['SALARY']))
#%%
data['DEPARTMENT'].value_counts().plot(kind='pie',
                                       autopct='%1.1f%%',
                                       colors = ['black','Green','yellow','red','orange','violet'],
                                       explode = [0.1,0,0,0,0,0],
                                        shadow = True
                                       )
                                       #explode = [0,0.2,0,0.2,0,0],
                                       #shadow = True

#plt.title('DEPARTMENT')
plt.show()
#%%
data['DEPARTMENT'] = data['DEPARTMENT'].str.strip().str.title()
data['STATUS'] = data['STATUS'].str.strip().str.capitalize()
data.tail(30)
#%%
import matplotlib.pyplot as plt

dept_salary = data.groupby('DEPARTMENT')['SALARY'].mean()

dept_salary.plot(kind='barh',
                 color='Blue'
                 )
plt.title('Average Salary by Department')

plt.xlabel('Department')
plt.ylabel('Average Salary')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
#%%
city_count = data['CITY'].value_counts()

city_count.plot(kind='bar',
                color='Grey'
                )
plt.title('City Vs Employee',
          color='Red',
          fontsize='20',
          fontweight='bold',
          fontstyle='italic',
          family='times New Roman'
          )
plt.xlabel('City',
           color='Red',
           fontweight='bold',
           fontsize='x-large',
           fontstyle='italic',
           family='Times New Roman')

plt.ylabel('Employee Count',
           color='Red',
           fontweight='bold',
           fontsize='x-large',
           fontstyle='italic',
           family='Times New Roman')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
#%%
data.isnull().sum()
#%%
