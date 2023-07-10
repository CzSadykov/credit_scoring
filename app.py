import streamlit as st
import numpy as np
from sklearn.preprocessing import StandardScaler
import pandas as pd
import pickle
import plotly.express as px
import matplotlib.pyplot as plt

with open('model/best_lgb.pkl', 'rb') as f:
    model = pickle.load(f)

st.set_page_config(
  page_title='Credit scoring dummy service',
  page_icon='🏦')

st.header('💸 Credit scoring dummy service 💸')
st.write('Made by CzSadykov. Just for fun.')

tab1, tab2 = st.tabs(["🗃 Prediction model", "📈 Underlying data"])

tab1.subheader("Predict a 90+ day bank delinquency")
tab1.write('Type in any values to get your prediction')

#default values

age = 21
balance2credit_ratio = 0.0
monthly_income = 0.0
spending2income_ratio = 0.0
open_debt = 0
count_dependents = 0.0
count_dlq_30_59_days = 0
count_dlq_60_89_days = 0
count_dlq_90_days_plus = 0

input_age = tab1.number_input('Age', min_value=21, max_value=109, step=1, value=age)

input_balance2credit_ratio = tab1.number_input("Customer's balance to credit limit ratio (in decimals)",
min_value=0.0,
step=0.0,
max_value=1.0,
value=monthly_income)


input_monthly_income = tab1.number_input('Monthly income (in $)',
min_value=0.0,
step=0.0,
max_value=1000000000.0,
value=monthly_income)

input_spending2income_ratio = tab1.number_input("Rate of monthly expensions to income (in decimals)",
min_value=0.0,
step=0.0,
max_value=2.0,
value=spending2income_ratio)

input_spending2income_ratio = input_spending2income_ratio / 100

input_open_debt = tab1.number_input('Number of open loans and credit cards',
min_value=0,
step=0,
max_value=100,
value=open_debt)

input_count_dependents = tab1.number_input('Number of dependents',
min_value=0.0,
step=1.0,
max_value=20.0,
value=count_dependents)

input_count_dlq_30_59_days = tab1.number_input('How many times 30-59 days past due in the last 2 years?',
min_value=0,
step=1,
max_value=100,
value=count_dlq_30_59_days)

input_count_dlq_60_89_days = tab1.number_input('How many times 60-89 days past due in the last 2 years?',
min_value=0,
step=1,
max_value=100,
value=count_dlq_60_89_days)

input_count_dlq_90_days_plus = tab1.number_input('How many times 90+ days past due in the last 2 years?',
min_value=0,
step=1,
max_value=100,
value=count_dlq_90_days_plus)

get = tab1.button('Get prediction!')

tab1.subheader('Results: ')
tab1.empty()

df = pd.read_csv('data/preprocessed_data.csv', lineterminator='\n')

def data_preprocessing(data):
    features = df.drop(columns='dlq_90_days_plus')
    target = df['dlq_90_days_plus']
    scaler = StandardScaler()
    scaler.fit(features)
    data = scaler.transform(data)
    return data

if get:
    user_data = {
        'balance2credit_ratio': [input_balance2credit_ratio],
        'age': [input_age],
        'count_dlq_30-59_days': [input_count_dlq_30_59_days], 
        'spending2income_ratio': [input_spending2income_ratio], 
        'monthly_income': [input_monthly_income],
        'open_debt': [input_open_debt],
        'count_dlq_90_days_plus': [input_count_dlq_90_days_plus],
        'count_dlq_60-89_days': [input_count_dlq_60_89_days],
        'count_dependents': [input_count_dependents],
        }

    data = data_preprocessing(pd.DataFrame.from_dict(user_data))
    prob = model.predict_proba(data)[0,1]
    is_rejected = prob > 0.3

    if is_rejected:
        tab1.error('⛔ Credit is **not** approved ⛔.')  
        tab1.write(f"The risk of customer's 90+ day delinquency is about {prob:.2%}.")
    else:
        tab1.balloons()
        tab1.success('🎉 Credit is **approved**! 🎉')
        tab1.write(f"The risk of customer's 90+ day delinquency is only {prob:.2%}.")

tab2.subheader("Explore some of the data we used to teach the model")

df['dlq_90_days_plus'] = df['dlq_90_days_plus'].replace({0:'diligent customers',
1:'deviant customers'})

tab2.write('Age distribution:')

fig = px.histogram(df['age'],
color=df['dlq_90_days_plus'],
opacity=0.7,
labels={'value' : 'age'})

tab2.plotly_chart(fig, theme="streamlit", use_container_width=True)

tab2.divider()

tab2.write('Balance-to-credit ratio distribution:')


fig = px.histogram(df['balance2credit_ratio'],
color=df['dlq_90_days_plus'],
opacity=0.7,
labels={'value' : 'balance-to-credit ratio'})

tab2.plotly_chart(fig, theme="streamlit", use_container_width=True)

tab2.divider()

tab2.write('Spending-to-income ratio distribution:')

fig = px.histogram(df['spending2income_ratio'],
color=df['dlq_90_days_plus'],
opacity=0.7,
labels={'value' : 'spending-to-income ratio'})

tab2.plotly_chart(fig, theme="streamlit", use_container_width=True)

tab2.divider()

tab2.write('Monthly income distribution:')

fig = px.histogram(df['monthly_income'],
color=df['dlq_90_days_plus'],
opacity=0.7,
labels={'value' : 'monthly income'})

tab2.plotly_chart(fig, theme="streamlit", use_container_width=True)

tab2.divider()

tab2.write('Number of dependents distribution:')

fig = px.histogram(df['count_dependents'],
color=df['dlq_90_days_plus'],
opacity=0.7,
labels={'value' : 'number of dependents'})

tab2.plotly_chart(fig, theme="streamlit", use_container_width=True)
