import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder
from sklearn.ensemble import GradientBoostingClassifier

URL = "mushrooms.csv"
COLS = ['class', 'odor', 'gill-size', 'gill-color', 'stalk-surface-above-ring',
       'stalk-surface-below-ring', 'stalk-color-above-ring',
       'stalk-color-below-ring', 'ring-type', 'spore-print-color']

# Function to read the data
@st.cache_data
def read_csv(csv,cols):
    df = pd.read_csv(csv)
    df = df[cols]
    
    return df

# Function to fit the LabelEncoder
@st.cache_resource
def y_encode(data):
    class_encode = LabelEncoder()
    class_encode.fit(data['class'])
    
    return class_encode

# Function to fit the OrdinalEncoder
@st.cache_resource
def x_encode(data):
    x_ordinal = OrdinalEncoder()
    x_cols = data.columns[1:]
    x_ordinal.fit(data[x_cols])
    
    return x_ordinal

# Function to encode data
@st.cache_data(show_spinner="Encoding data...")
def encode_data(data,_x_encode,_y_encode):
    data['class'] = _y_encode.transform(data['class'])
    x_cols = data.columns[1:]
    data[x_cols] = _x_encode.transform(data[x_cols])

    return data


# Function to train the model
@st.cache_resource
def train_model(data):
    X = data.drop(['class'],axis=1)
    y = data['class']
    
    gbc = GradientBoostingClassifier(max_depth=5, random_state=42)
    gbc.fit(X,y)
    
    return gbc

# Function to make a prediction
@st.cache_data(show_spinner="Making a prediction...")
def predic_data(_model,_X_encoder,X_pred):
    features = [each[0] for each in X_pred]
    features = np.array(features).reshape(1,-1)
    encoded_features = _X_encoder.transform(features)

    pred = _model.predict(encoded_features)

    return pred[0]

if __name__ == "__main__":
    st.title("Mushroom classifier 🍄")
    
    # Read the data
    with st.form("key_form"):
        st.subheader("Step 1: Select the values for prediction")

        col1, col2, col3 = st.columns(3)

        with col1:
            odor = st.selectbox('Odor', ('a - almond', 'l - anisel', 'c - creosote', 'y - fishy', 'f - foul', 'm - musty', 'n - none', 'p - pungent', 's - spicy'))
            stalk_surface_above_ring = st.selectbox('Stalk surface above ring', ('f - fibrous', 'y - scaly', 'k - silky', 's - smooth'))
            stalk_color_below_ring = st.selectbox('Stalk color below ring', ('n - brown', 'b - buff', 'c - cinnamon', 'g - gray', 'o - orange', 'p - pink', 'e - red', 'w - white', 'y - yellow'))
        with col2:
            gill_size = st.selectbox('Gill size', ('b - broad', 'n - narrow'))
            stalk_surface_below_ring = st.selectbox('Stalk surface below ring', ('f - fibrous', 'y - scaly', 'k - silky', 's - smooth'))
            ring_type = st.selectbox('Ring type', ('e - evanescente', 'f - flaring', 'l - large', 'n - none', 'p - pendant', 's - sheathing', 'z - zone'))
        with col3:
            gill_color = st.selectbox('Gill color', ('k - black', 'n - brown', 'b - buff', 'h - chocolate', 'g - gray', 'r - green', 'o - orange', 'p - pink', 'u - purple', 'e - red', 'w - white', 'y - yellow'))
            stalk_color_above_ring = st.selectbox('Stalk color above ring', ('n - brown', 'b - buff', 'c - cinnamon', 'g - gray', 'o - orange', 'p - pink', 'e - red', 'w - white', 'y - yellow'))
            spore_print_color = st.selectbox('Spore print color', ('k - black', 'n - brown', 'b - buff', 'h - chocolate', 'r - green', 'o - orange', 'u - purple', 'w - white', 'y - yellow'))
        pred_btn = st.form_submit_button("Predict", type="primary")

        st.subheader("Step 2: Ask the model for a prediction")

        
    # If the button is clicked:
    # 1. Fit the LabelEncoder
    # 2. Fit the OrdinalEncoder
    # 3. Encode the data
    # 4. Train the model
    if pred_btn:
        data = read_csv(URL,COLS)
        class_encoded = y_encode(data)
        x_encoded = x_encode(data)
        encoded_data = encode_data(data,x_encoded,class_encoded)
        gbc =train_model(encoded_data)
        x_pred = [odor, 
                gill_size, 
                gill_color, 
                stalk_surface_above_ring, 
                stalk_surface_below_ring, 
                stalk_color_above_ring, 
                stalk_color_below_ring, 
                ring_type, 
                spore_print_color]
    
    # 5. Make a prediction
        pred = predic_data(gbc, x_encoded, x_pred)
    # 6. Format the prediction to be a nice text
        nice_pred = "The mushroom is poisonous 🤢" if pred == 1 else "The mushroom is edible 🍴"
    # 7. Output it to the screen
        st.write(nice_pred)