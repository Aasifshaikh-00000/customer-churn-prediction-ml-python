# gender --> 1 female   0 male
# churn -->  1 yes      0 no
# scaler is exported as scaler.pkl
# model is exported as model.pkl
# order of the x --> ['Age', 'Gender', 'Tenure', 'MonthlyCharges']


import streamlit as st
import numpy as np
import joblib

scaler = joblib.load(r"d:\workplace@123\churn prediction project\scaler.pkl")
model = joblib.load(r"d:\workplace@123\churn prediction project\model.pkl")


st.title('CHURN PREDICTION APP')

st.divider()

st.write('Please Enter the values and hit the predict button to get the prediction')

st.divider()

Age = st.number_input('Enter Age',min_value=10, max_value=100)

Tenure = st.number_input('Enter Tenure',min_value=0,max_value=130,value=30)

Monthly_charges = st.number_input('Enter monthly charges',min_value=10,max_value =200)

Gender =st.selectbox('Select the Gender',['Male','Female'])

st.divider()

predictbutton = st.button('PREDICT')

st.divider()

if predictbutton:
    gender_selected = 1 if Gender == 'Female' else 0

    x =['Age','Gender','Tenure','Monthly_charges']
    x1 = np.array(x)

    x_array = scaler.transform([x1])

    prediction = model.predict(x_array)[0]

    predicted = 'Churn' if prediction == 1 else 'Not Churn' 

    st.write(f'Predicted : Chances are Customer might {predicted}.') 

else:
    st.write('Please enter the values first !!!')





