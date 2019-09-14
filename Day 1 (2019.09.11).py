#!/usr/bin/env python
# coding: utf-8

# In[6]:


print('안녕! 판다스')


# In[7]:


pip list


# In[8]:


import pandas


# In[9]:


df = pandas.read_csv('../data/gapminder.tsv', sep='\t')


# In[10]:


import pandas as pd
df = pd.read_csv('E:/Python_source/doit_pandas-master/data/gapminder.tsv', sep='\t')


# In[11]:


print(df.head())


# In[12]:


print(type(df))


# In[13]:


print(df.shape)


# In[14]:


print(df.columns)


# In[15]:


print(df.dtypes)


# In[16]:


print(df.info())


# In[17]:


country_df = df['country']


# In[18]:


print(type(country_df))


# In[19]:


print(country_df.head())


# In[20]:


print(country_df.tail())


# In[21]:


subset = df[['country','continent','year']]


# In[22]:


print(type(subset))


# In[23]:


print(subset.head())


# In[24]:


print(subset.tail())


# In[25]:


print(df.loc[0])


# In[26]:


print(df.loc[99])


# In[27]:


print(df.loc[-1])


# In[28]:


number_of_rows = df.shape[0]


# In[29]:


last_row_index = number_of_rows - 1


# In[30]:


print(df.loc[last_row_index])


# In[31]:


print(df.tail(n=1))


# In[32]:


print(df.loc[[0, 99, 999]])


# In[33]:


print(df.iloc[1])


# In[34]:


print(df.iloc[99])


# In[35]:


print(df.iloc[-1])


# In[36]:


print(df.iloc[1710])


# In[37]:


print(df.iloc[[0,99,999]])


# In[38]:


subset = df.loc[:, ['year', 'pop']]
print(subset.head())


# In[39]:


subset = df.iloc[:, [2, 4, -1]]
print(subset.head())


# In[40]:


small_range = list(range(5))
print(small_range)


# In[41]:


print(type(small_range))


# In[42]:


subset = df.iloc[:, small_range]
print(subset.head())


# In[43]:


small_range = list(range(3,6))
print(small_range)


# In[44]:


subset = df.iloc[:, small_range]
print(subset.head())


# In[45]:


small_range = list(range(0,6,2))
subset = df.iloc[:, small_range]
print(subset.head())


# In[46]:


subset = df.iloc[:, :3]
print(subset.head())


# In[47]:


subset = df.iloc[:, 0:6:2]
print(subset.head())


# In[48]:


print(df.iloc[[0, 99, 999], [0,3,5]])


# In[49]:


print(df.loc[[0,99,999], ['country','lifeExp','gdpPercap']])


# In[50]:


print(df.loc[10:13, ['country','lifeExp','gdpPercap']])


# In[51]:


print(df.head(n=10))


# In[52]:


print(df.groupby('year')['lifeExp'].mean())


# In[53]:


grouped_year_df = df.groupby('year')
print(type(grouped_year_df))


# In[54]:


print(grouped_year_df)


# In[55]:


grouped_year_df_lifeExp = grouped_year_df['lifeExp']
print(type(grouped_year_df_lifeExp))


# In[56]:


mean_lifeExp_by_year = grouped_year_df_lifeExp.mean()
print(mean_lifeExp_by_year)


# In[57]:


multi_group_var = df.groupby(['year','continent'])[['lifeExp','gdpPercap']].mean()
print(multi_group_var)


# In[58]:


print(type(multi_group_var))


# In[59]:


print(df.groupby('continent')['country'].nunique())


# In[60]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# In[61]:


global_yearly_life_expectancy = df.groupby('year')['lifeExp'].mean()
print(global_yearly_life_expectancy)


# In[62]:


global_yearly_life_expectancy.plot()


# In[63]:


import pandas as pd
s = pd.Series(['banana',42])
print(s)


# In[64]:


s = pd.Series(['Wes Mckinney','Creator of Pandas'])
print(s)


# In[65]:


s = pd.Series(['Wes Mckinney','Creator of Pandas'], index=['Person','Who'])
print(s)


# In[66]:


scientists = pd.DataFrame({
    'Name': ['Rosaline Franklin', 'William Gosset'],
    'Occupation': ['Chemist', 'Statistician'],
    'Born': ['1920-07-25', '1876-06-13'],
    'Died': ['1958-04-16', '1937-10-16'],
    'Age': [37, 61]}
)
print(scientists)


# In[67]:


scientists = pd.DataFrame(
    data={'Occupation': ['Chemist', 'Statistician'],
    'Born': ['1920-07-25', '1876-06-13'],
    'Died': ['1958-04-16', '1937-10-16'],
    'Age': [37, 61]},
    index=['Rosaline Franklin', 'William Gosset'],
    columns=['Occupation', 'Born', 'Age', 'Died']
)
print(scientists)


# In[68]:


from collections import OrderedDict

scientists = pd.DataFrame(OrderedDict([
    ('Name', ['Rosaline Franklin', 'William Gosset']),
    ('Occupation', ['Chemist', 'Statistician']),
    ('Born', ['1920-07-25', '1876-06-13']),
    ('Died', ['1958-04-16', '1937-10-16']),
    ('Age', [37, 61])
])
)
print(scientists)


# In[69]:


scientists = pd.DataFrame(
    data={'Occupation': ['Chemist', 'Statistician'],
    'Born': ['1920-07-25', '1876-06-13'],
    'Died': ['1958-04-16', '1937-10-16'],
    'Age': [37, 61]},
    index=['Rosaline Franklin', 'William Gosset'],
    columns=['Occupation', 'Born', 'Age', 'Died']
)

first_row = scientists.loc['William Gosset']
print(type(first_row))


# In[70]:


print(first_row)


# In[71]:


print(first_row.index)
print(first_row.values)
print(first_row.keys())
print(first_row.index[0])
print(first_row.keys()[0])


# In[72]:


ages = scientists['Age']
print(ages)


# In[73]:


print(ages.mean())
print(ages.min())
print(ages.max())
print(ages.std())


# In[74]:


scientists = pd.read_csv('E:/Python_source/doit_pandas-master/data/scientists.csv')


# In[75]:


ages = scientists['Age']
print(ages.max())


# In[76]:


print(ages.mean())


# In[77]:


print(ages[ages > ages.mean()])


# In[78]:


print(ages>ages.mean())


# In[79]:


manual_bool_values = [True, True, False, False, True, True, False, True]
print(ages[manual_bool_values])


# In[80]:


print(ages + ages)


# In[81]:


print(ages * ages)


# In[82]:


print(ages * 2)


# In[83]:


print(ages + 10)


# In[84]:


print(pd.Series([1,100]))


# In[85]:


print(ages + pd.Series([1,100]))


# In[86]:


rev_ages = ages.sort_index(ascending=False)
print(rev_ages)


# In[87]:


print(ages * 2)


# In[88]:


print(ages + rev_ages)


# In[89]:


print(scientists[scientists['Age']> scientists['Age'].mean()])


# In[90]:


print(scientists.loc[[True, True, False, True]])


# In[91]:


print(scientists * 2)


# In[92]:


print(scientists['Born'].dtype)
print(scientists['Died'].dtype)


# In[93]:


born_datetime = pd.to_datetime(scientists['Born'], format='%Y-%m-%d')
print(born_datetime)


# In[94]:


died_datetime = pd.to_datetime(scientists['Died'], format='%Y-%m-%d')
print(died_datetime)


# In[95]:


scientists['born_dt'], scientists['died_dt'] = (born_datetime, died_datetime)
print(scientists.head())


# In[96]:


print(scientists.shape)


# In[97]:


scientists['age_days_dt'] = (scientists['died_dt'] - scientists['born_dt'])
print(scientists)


# In[98]:


print(scientists['Age'])


# In[99]:


import random

random.seed(42)
random.shuffle(scientists['Age'])
print(scientists['Age'])


# In[100]:


print(scientists.columns)


# In[101]:


scientists_dropped = scientists.drop(['Age'], axis=1)
print(scientists_dropped.columns)


# In[110]:


names = scientists['Name']
names.to_pickle('E:/Python_source/doit_pandas-master/output/scientists_names_series.pickle')


# In[111]:


scientists.to_pickle('E:/Python_source/doit_pandas-master/output/scientists_df.pickle')


# In[112]:


scientists_names_from_pickle = pd.read_pickle('E:/Python_source/doit_pandas-master/output/scientists_names_series.pickle')
print(scientists_names_from_pickle)


# In[113]:


scientists_from_pickle = pd.read_pickle('E:/Python_source/doit_pandas-master/output/scientists_df.pickle')
print(scientists_from_pickle)


# In[114]:


names.to_csv('E:/Python_source/doit_pandas-master/output/scientists_names_series.csv')
scientists.to_csv('E:/Python_source/doit_pandas-master/output/scientists_df.tsv', sep='\t')


# In[116]:


pip install xlwt


# In[117]:


pip install openpyxl


# In[ ]:




