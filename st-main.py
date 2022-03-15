import pandas as pd              # data manipulation
import numpy as np               # math operations on arrays / random number gen
import matplotlib.pyplot as plt  # visualization package
import seaborn as sns            # visualization package
from math import ceil, floor     # math rounding operationS
import streamlit as st           # web app
import os                        # handle png image

# ) Displaying page title & subtitle
st.title("Data Visualization Dashboard :bar_chart: ")
st.subheader("for EDA (Exploration Data Analysis)")
st.subheader(" ")
#new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">New image</p>'
st.markdown(":arrow_forward: This dashboard visualizes count plot on categorical variables and distribution plot on numerical variables.")
st.markdown(":arrow_forward: The plots assist you to understand your initial data condition e.g. classes presence, shape of distribution, etc.")
st.markdown(":arrow_forward: You may upload your own **.csv** file - preferrably without any Index/ID/Key/Unique-value-rows column.")
st.markdown(":arrow_forward: Max file size: **200MB**")
st.markdown(":arrow_forward: For wide screen view, select ≡ > Settings > Wide mode ")
st.subheader(" ")

# ) Read Data
df = pd.read_csv('WA_Fn-UseC_-Sales-Win-Loss.csv')

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
      # Can be used wherever a "file-like" object is accepted:
        df_upload = pd.read_csv(uploaded_file)
        st.write(df_upload)
        df = df_upload
st.markdown(" ")


# ------------------------
# INITIALIZE PLOT SETTING
#-------------------------
# Defining function to set figure size
def figure(a,b):
    sns.set(rc={'figure.figsize':(a,b)})

figure(15,10)
plt_cols = 3                                                           # Customized no. of columns in subplot
    
    
# CATEGORICAL VARIABLES
# ---------------------
df_string = df.loc[:,df.dtypes == 'object']

plt_rows = ceil(len(df_string.columns)/plt_cols)                       # Set the no. of rows in subplot by dividing: 
                                                                       #  roundup(no. of variables / no. of columns)
fig1, axes = plt.subplots(plt_rows,plt_cols)
fig1.suptitle("Countplots of Categorical Variables \n (x-axis: Variable) \n (y-axis: Count of samples)", 
             fontsize="x-large")
axes = axes.ravel()


for i in range(0, len(df_string.columns)):
    sns.countplot(df_string.iloc[:,i], ax=axes[i])                     # Plot countplot for each categorical variable
    axes[i].set_title('Countplot of ' + df_string.columns[i], size=15) # Set title of every subplot
    axes[i].tick_params(axis='x', labelrotation=90, pad=0)             # Rotate x-axis of every subplot
    axes[i].set_xlabel('')                                             # Turn off subplots' x-axis titles for tidiness
fig1.tight_layout(rect=[0, 0, 1, 0.88])                                # Adjust tight_layout to accommodate suptitle

# save image, display it, and delete after usage.
plt.savefig('fig1',dpi=1000)
# st.image('fig1.png')


# ---------------------
# NUMERICAL VARIABLES
# ---------------------
df_numeric0 = df.loc[:, df.dtypes!='object']

# Check presence of Index / index 
#  and drop those columns
id_cols = ['Index', 'index']
df_numeric = df_numeric0.loc[:, ~df_numeric0.columns.isin(id_cols)]

plt_rows = ceil(len(df_numeric.columns)/plt_cols)             # Set the no. of rows in subplot by dividing: 
                                                              #  roundup(no. of variables / no. of columns)
fig2, axes = plt.subplots(plt_rows,plt_cols)
fig2.suptitle("Distribution Plots of Numerical Variables \n (x-axis: Variable) \n (y-axis: Distribution proportion)", 
             fontsize="x-large")
axes = axes.ravel()


for i in range(0, len(df_numeric.columns)):
    sns.distplot(df_numeric.iloc[:,i], ax=axes[i])            # Plot countplot for each categorical variable
    axes[i].set_title(df_numeric.columns[i], size=15)         # Set title of every subplot
    axes[i].tick_params(axis='x', labelrotation=90, pad=0)    # Rotate x-axis of every subplot
    axes[i].set_xlabel('')                                    # Turn off subplots' x-axis titles for tidiness
fig2.tight_layout(rect=[0, 0, 1, 0.88])                       # Adjust tight_layout to accommodate suptitle

# save image, display it, and delete after usage.
plt.savefig('fig2',dpi=1000)


# ---------------------
# DASHBOARD DISPLAY
#----------------------
# Displaying results for Categorical Variables
st.subheader("Categorical Variables")
result1 = st.container()
with result1:
    result1.image('fig1.png')
    result1.markdown("Head of the dataframe that contains only categorical variables:")
    result1.dataframe(df_string.head())
    result1.markdown(" ")
    
# Displaying results for Numerical Variables
st.subheader(" ")
st.subheader("Numerical Variables")
result2 = st.container()
with result2:
    result2.image('fig2.png')    
    result2.markdown("Head of the dataframe that contains only numerical variables:")
    result2.dataframe(df_numeric0.head())
    
    
# ) Delete displayed images from system
os.remove('fig1.png')
os.remove('fig2.png')
    