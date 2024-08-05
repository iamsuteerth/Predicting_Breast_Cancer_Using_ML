#load libraries
import numpy as np         # linear algebra
import pandas as pd        # data processing, CSV file I/O (e.g. pd.read_csv)
# Read the file "data.csv" and print the contents.
df = pd.read_csv('data/data.csv', index_col=False)
df.head()
# Save the cleaner version of dataframe with "id" for future analyis
df.to_csv('data/data_clean_id.csv')

# Id column is redundant and not useful, we want to drop it
df.drop('id', axis =1, inplace=True)
# df.drop('Unnamed: 0', axis=1, inplace=True)
df.head(3)

# Review data types with "info()".
df.info()
# Check for missing variables
df.isnull().any()
df.diagnosis.unique()

# Save the cleaner version of dataframe for future analyis
df.to_csv('data/data_clean.csv')

from scipy.stats import norm
import seaborn as sns # data visualization
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (15,8) 
plt.rcParams['axes.titlesize'] = 'large'

# usind clean data with "id"
df = pd.read_csv('data/data_clean_id.csv', index_col=False)
df.drop('Unnamed: 0',axis=1, inplace=True)
df.head(3)

#basic descriptive statistics
df.describe()

df_temp = df.copy()
df_temp.drop("diagnosis", axis = 1, inplace=True);
df_temp.skew()

df.diagnosis.unique()

# Group by diagnosis and review the output.
diag_gr = df.groupby('diagnosis', axis=0)
pd.DataFrame(diag_gr.size(), columns=['# of observations'])

#lets get the frequency of cancer diagnosis
sns.set_style("white")
sns.set_context({"figure.figsize": (10, 8)})
sns.countplot(df['diagnosis'],label='Count',palette="Set3")

#Break up columns into groups, according to their suffix designation 
#(_mean, _se,and __worst) to perform visualisation plots off. 
#Join the 'ID' and 'Diagnosis' back on
df_id_diag=df.loc[:,["id","diagnosis"]]
df_diag=df.loc[:,["diagnosis"]]

#For a merge + slice:
df_mean=df.iloc[:,1:11]
df_se=df.iloc[:,11:22]
df_worst=df.iloc[:,23:]

print(df_id_diag.columns)
#print(data_mean.columns)
#print(data_se.columns)
#print(data_worst.columns)

#Plot histograms of CUT1 variables
hist_mean=df_mean.hist(bins=10, figsize=(15, 10),grid=False,)

#Any individual histograms, use this:
#df_cut['radius_worst'].hist(bins=100)

#Plot histograms of _se variables
hist_se=df_se.hist(bins=10, figsize=(15, 10),grid=False,)

#Plot histograms of _worst variables
hist_worst=df_worst.hist(bins=10, figsize=(15, 10),grid=False,)

#Density Plots
plt = df_mean.plot(kind= 'density', subplots=True, layout=(4,3), sharex=False, sharey=False, fontsize=12, figsize=(15,10))

#Density Plots
plt = df_se.plot(kind= 'density', subplots=True, layout=(4,3), sharex=False, sharey=False, fontsize=12, figsize=(15,10))

#Density Plots
plt = df_worst.plot(kind= 'kde', subplots=True, layout=(4,3), sharex=False, sharey=False, fontsize=5, figsize=(15,10))

# box and whisker plots
plt=df_mean.plot(kind= 'box' , subplots=True, layout=(4,4), sharex=False, sharey=False, fontsize=12)

# box and whisker plots
plt=df_se.plot(kind= 'box' , subplots=True, layout=(4,4), sharex=False, sharey=False, fontsize=12)

# box and whisker plots
plt=df_worst.plot(kind= 'box' , subplots=True, layout=(4,4), sharex=False, sharey=False, fontsize=12)

plt.style.use('fivethirtyeight')
sns.set_style("white")

df = pd.read_csv('data/data_clean.csv', index_col=False)
df.drop('Unnamed: 0',axis=1, inplace=True)

df_temp = df_mean.copy()
df_temp.drop("diagnosis", axis = 1, inplace=True);

# Compute the correlation matrix
corr = df_temp.corr()

# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=bool)
mask[np.triu_indices_from(mask)] = True

# Set up the matplotlib figure
df, ax = plt.subplots(figsize=(8, 8))
plt.title('Breast Cancer Feature Correlation')

# Generate a custom diverging colormap
cmap = sns.diverging_palette(260, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, vmax=1.2, square='square', cmap=cmap, mask=mask, 
            ax=ax,annot=True, fmt='.2g',linewidths=2)

plt.style.use('fivethirtyeight')
sns.set_style("white")

df = pd.read_csv('data/data_clean.csv', index_col=False)
g = sns.PairGrid(df[[df.columns[1],df.columns[2], df.columns[3], df.columns[4], df.columns[5], df.columns[6]]], hue='diagnosis')

g = g.map_diag(plt.hist)
g = g.map_offdiag(plt.scatter, s = 3)