import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder # เรียกเครื่องมือแปลงร่าง

# 1. สร้างข้อมูลจำลอง (มีแต่ตัวหนังสือ)
df = pd.DataFrame({
    'Shirt_Size': ['S', 'M', 'L', 'M', 'S', 'XL', 'L'],
    'Color': ['Red', 'Blue', 'Green', 'Blue', 'Red', 'Black', 'Green']
})

print("--- ข้อมูลดิบ ---")
print(df)

# ==========================================
# วิธีที่ 1: ใช้ Pandas factorize (ตามหนังสือหน้า 80)
# ==========================================
# มันจะคืนค่ามา 2 อย่าง: ตัวเลข และ รายชื่อคำศัพท์เดิม (เราเอาแค่ตัวเลข คือ [0])
df['Size_Code_Pandas'] = pd.factorize(df['Shirt_Size'])[0]

# ==========================================
# วิธีที่ 2: ใช้ Scikit-Learn LabelEncoder (แบบในคลิป)
# ==========================================
encoder = LabelEncoder()

# สั่งให้จำและแปลงทันที (fit_transform)
df['Color_Code_Sklearn'] = encoder.fit_transform(df['Color'])

print("\n--- หลังแปลงร่างแล้ว ---")
print(df)

# (แถม) เช็คหน่อยว่าเลขไหนคือสีอะไร?
print("\nถอดรหัสสี:", list(enumerate(encoder.classes_)))