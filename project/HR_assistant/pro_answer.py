import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder
from sklearn.linear_model import LogisticRegression
import streamlit as st

# 1. Data Setup
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
df = pd.DataFrame(data) # เปลี่ยนชื่อเป็น df ให้ชินมือ

# 2. Functions
# (เทคนิค: ใส่ @st.cache_data ไว้เลยครับ จะได้โหลดเร็ว)
@st.cache_data
def get_encoders(data):
    # สร้าง Encoder ใหม่ แยกกันชัดเจน
    le = LabelEncoder()
    le.fit(data['Promoted'])
    
    oe = OrdinalEncoder()
    # เลือกเฉพาะ 2 คอลัมน์แรกที่เป็น Text
    oe.fit(data[['Department', 'Education']]) 
    
    return le, oe

@st.cache_data
def train_model(data):
    # เรียก Encoder ที่เตรียมไว้
    le, oe = get_encoders(data)
    
    # สร้างข้อมูลใหม่เพื่อใช้ Train (ไม่ยุ่งกับข้อมูลดิบ)
    X = data.drop('Promoted', axis=1)
    y = le.transform(data['Promoted']) # แปลง y
    
    # แปลง X เฉพาะคอลัมน์ที่เป็น Text
    X[['Department', 'Education']] = oe.transform(X[['Department', 'Education']])

    # สร้างและสอนโมเดล
    lr = LogisticRegression()
    lr.fit(X, y)
    
    return lr

# ฟังก์ชันทำนาย (รับ Encoder เข้ามาด้วย)
def make_prediction(model, oe, user_input):
    # 1. แยกส่วน Text กับ Number
    text_data = pd.DataFrame([user_input[:2]], columns=['Department', 'Education'])
    
    num_data = user_input[2]     # 85
    
    # 2. แปลง Text เป็นตัวเลข
    encoded_text = oe.transform(text_data) # ได้ออกมาเป็น [[0. 1.]]

    # 3. เอาตัวเลขมารวมร่างกัน (Concatenate)
    # รวม [[0, 1]] กับ [[85]] ให้กลายเป็น [[0, 1, 85]]
    # (ใช้ np.hstack คือการเอามาแปะต่อท้ายแนวนอน)
    final_features_np = np.hstack((encoded_text, [[num_data]]))
    
    
    # 4. (จุดสำคัญ!) แปลงกลับเป็น DataFrame พร้อมชื่อคอลัมน์ (แก้ Warning ของ Model)
    # ต้องเรียงชื่อให้เหมือนตอน Train เป๊ะๆ
    feature_names = ['Department', 'Education', 'Performance']
    final_features_df = pd.DataFrame(final_features_np, columns=feature_names)
    
    # 5. ทำนาย
    pred = model.predict(final_features_df)
    return pred[0]

# 3. User Interface
st.header("HR Assistant Program 👔")

with st.expander("See training data"):
    st.dataframe(df)

# สร้างฟอร์ม
with st.form(key="form-key"):
    st.subheader("Employee Info")
    col1, col2 = st.columns(2)
    
    dep = col1.selectbox("Department", options=df['Department'].unique())
    edu = col2.selectbox("Education", options=df['Education'].unique())
    per = st.slider("Performance Score", min_value=0, max_value=100, value=50)
    
    # ปุ่ม Submit
    submit_btn = st.form_submit_button("Predict Promotion", type='primary')

# 4. Logic (ทำงานเมื่อกดปุ่มเท่านั้น)
if submit_btn:
    # เรียกใช้ฟังก์ชันที่เราเขียนไว้
    le, oe = get_encoders(df)
    model = train_model(df)
    
    # เตรียมข้อมูลจากหน้าจอ
    user_data = [dep, edu, per]
    
    # ทำนายผล
    result_index = make_prediction(model, oe, user_data)
    
    # แปลงผลลัพธ์กลับเป็นคำพูด (ใช้ le.inverse_transform ได้นะ)
    result_text = le.inverse_transform([result_index])[0]
    
    if result_text == 'Yes':
        st.success(f"Result: {result_text} - Congratulations! 🎉")
    else:
        st.error(f"Result: {result_text} - Sorry, keep working hard! ✌️")