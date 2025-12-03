import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.linear_model import LogisticRegression
import streamlit as st
data = {
    'Department': ['Sales', 'IT', 'HR', 'IT', 'Sales', 'IT', 'HR', 'Sales', 'IT', 'Sales', 
                   'HR', 'IT', 'Sales', 'Sales', 'IT', 'HR', 'IT', 'Sales', 'HR', 'IT'],
    'Education': ['Bachelor', 'Master', 'PhD', 'Bachelor', 'Master', 'PhD', 'Bachelor', 'Bachelor', 'Master', 'PhD',
                  'Master', 'Bachelor', 'Master', 'PhD', 'Bachelor', 'Master', 'PhD', 'Bachelor', 'Master', 'PhD'],
    'Performance': [85, 90, 78, 45, 88, 95, 60, 50, 92, 98, 
                    70, 48, 89, 94, 55, 75, 96, 52, 80, 91],
    'Promoted': ['Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes',
                 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'Yes']
}

data = pd.DataFrame(data)

@st.cache_data
def target_encoder (data):
    l_encode = LabelEncoder()
    l_encode.fit(data['Promoted'])
    
    return l_encode

@st.cache_data
def feature_encoder(data):
    x_cols = data.columns[0:2]
    ore = OrdinalEncoder()
    ore.fit(data[x_cols].values)
 
    return ore

@st.cache_data
def data_encode(data,_x_encoder,_y_encoder):
    x_cols = data.columns[0:2]
    data[x_cols] = _x_encoder.transform(data[x_cols])
    data['Promoted']  = _y_encoder.transform(data['Promoted'])

    return data

@st.cache_resource
def train_model(encoded_data):
    lr = LogisticRegression()
    x = encoded_data.drop('Promoted',axis=1)
    y = encoded_data['Promoted']
    lr.fit(x.values,y)
    
    return lr


def predict_data(_model,_x_encoder,_x_data):
    x_data_2d = np.array(_x_data[:2]).reshape(1,-1)
    encode_data = _x_encoder.transform(x_data_2d)
    data_for_predict = np.append(encode_data,x_data[2])
    predict = _model.predict([data_for_predict])

    return predict



st.header("HR Assistent Program")

with st.expander("See full table"):
    st.dataframe(data)

with st.form(key="form-key"):
    st.subheader("Input Form")
    dep =st.selectbox("Department",options=data['Department'].unique())
    edu = st.selectbox("Education",options=data['Education'].unique())
    per = st.slider("Performance",min_value=0,max_value=100)
    
    submitted = st.form_submit_button("Enter",type='primary')
if submitted:
    y_encoder = target_encoder(data)
    x_encoder = feature_encoder(data)

    encoded_data = data_encode(data,x_encoder,y_encoder)

    lgr = train_model(encoded_data)
    x_data = [dep,edu,per]


    pred =predict_data(lgr,x_encoder,x_data)
   
    st.write(f"You will be promoted" if pred ==1 else "You will not be promoted")