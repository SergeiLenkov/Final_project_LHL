import pandas as pd
import numpy as np
from joblib import dump, load


import inquirer
questions = [
inquirer.Text('Age', 
                message="Please, type in your age"),
inquirer.List('Gender',
                message="Please, select your gender:",
                choices=['M', 'F']),
inquirer.List('Dependent_Count',
                message="Please, select number of dependents:",
                choices=[0, 1, 2, 3, 4, 5]),
inquirer.List('Education_Level',
                message="Please, select your level of education:",
                choices=['High School', 'Graduate', 'Post-Graduate',
       'Uneducated', 'College', 'Doctorate']),
inquirer.List('Marital_Status',
                message="Please, select your marital status:",
                choices=['Single', 'Married', 'Divorced']),
inquirer.List('Income_Category',
                message="Please, select your income category:",
                choices=['Less than $40K', '$40K - $60K', '$60K - $80K',
       '$80K - $120K', '$120K +'])
]

answers = inquirer.prompt(questions)

answers['Age'] = int(answers['Age'])

data = pd.DataFrame([answers])

pipeline = load('/home/sergei/Desktop/LighthouseLabs/Re_enter_bootcamp/Final_Project/final_project_houseprice_git/model_recommendation.joblib')

print("zipcode of area in Austin recommended by the model:\n{}".format(int(pipeline.predict(data))))

questions2 = [
inquirer.Text('Year', 
                message="Please, type in the year you plan to move to Austin")
]

answers = inquirer.prompt(questions2)

answers['Year'] = int(answers['Year'])

degree = answers['Year'] - 2021

annual_house_appreciation_rate = 1.0728

zip_average_house_price = pd.read_csv('/home/sergei/Desktop/LighthouseLabs/Re_enter_bootcamp/Final_Project/final_project_houseprice_git/zipcode_average_house_price_2021.csv',index_col=0)
mydict = dict(zip(zip_average_house_price.zipcode, zip_average_house_price.average_zip_price))

import math
def roundup(x):
    return int(math.ceil(x / 1000.0)) * 1000

print("Average amount of money needed to purchase a house in this area in {} would be {} US dollars".format\
    (answers['Year'], roundup(mydict[int(pipeline.predict(data))] * annual_house_appreciation_rate**degree)))