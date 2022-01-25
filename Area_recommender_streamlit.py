import pandas as pd
import numpy as np
from joblib import dump, load
import streamlit as st

# Title
st.title("The recommendation of areas to purchase house in Austin")


# Header
st.header("Welcome to Austin area recommender and budget estimator")

# Subheader
st.subheader("Please, choose your parameters for recommendation")

# Plain text
st.text('Please, choose your Age:')

# slider
# first argument takes the title of the slider
# second argument takes the starting of the slider
# last argument takes the end number
Age = st.slider("Age", 26, 70)
 
st.text('Please, choose your gender:')
# Selection box
 
# first argument takes the titleof the selectionbox
# second argument takes options
Gender = st.selectbox("Gender: ",
                     ['M', 'F'])
 

st.text('Please, choose your number of children:')
Dependents = st.selectbox("Number of children: ",
                     [0, 1, 2, 3, 4, 5])

st.text('Please, choose your level of education:')
Education = st.selectbox("Education: ",
                     ['High School', 'Graduate', 'Post-Graduate',
       'Uneducated', 'College', 'Doctorate'])

st.text('Please, choose your marital status:')
Marital_Status = st.selectbox("Marital Status: ",
                     ['Single', 'Married', 'Divorced'])

st.text('Please, choose your income category:')
Income = st.selectbox("Income Category: ",
                     ['Less than $40K', '$40K - $60K', '$60K - $80K',
       '$80K - $120K', '$120K +'])

answers = {'Age':Age,'Gender':Gender,'Dependent_Count':Dependents,'Education_Level':Education,'Marital_Status':Marital_Status,'Income_Category':Income}
data = pd.DataFrame([answers])

pipeline = load('model_recommendation.joblib')

st.write("Zipcode of area in Austin recommended by the model:\n{}".format(int(pipeline.predict(data))))

st.text('Please, select the year you plan to move to Austin:')
Year = st.slider("Year", 2021, 2050)

degree = Year - 2021

annual_house_appreciation_rate = 1.0728

zip_average_house_price = pd.read_csv('zipcode_average_house_price_2021.csv',index_col=0)
mydict = dict(zip(zip_average_house_price.zipcode, zip_average_house_price.average_zip_price))

import math
def roundup(x):
    return int(math.ceil(x / 1000.0)) * 1000

st.write("Average amount of money needed to purchase a house in this area in {} would be {} US dollars".format\
    (Year, roundup(mydict[int(pipeline.predict(data))] * annual_house_appreciation_rate**degree)))