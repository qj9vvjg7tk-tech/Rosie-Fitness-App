import streamlit as st
import re

# 1. إعدادات الصفحة والتصميم
st.set_page_config(page_title="تطبيق الروز الرياضي", page_icon="🌹", layout="wide")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #fff5f8 0%, #f3e5f5 100%); }
    h1, h2, h3 { color: #d81b60 !important; text-align: center; }
    .stButton>button { background-color: #ff4b91; color: white; border-radius: 20px; font-weight: bold; width: 100%; border: none; }
    .report-box { background-color: white; padding: 20px; border-radius: 15px; border-right: 5px solid #d81b60; margin-top: 10px; direction: rtl; }
    </style>
    """, unsafe_allow_html=True)

st.title("تطبيق الروز الرياضي الشامل 🌹")
st.image("https://images.unsplash.com/photo-1518310383802-640c2de311b2?ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80")

# 2. القياسات (الطول والوزن)
st.header("⚖️ القياسات والأهداف")
c_w, c_h, c_b = st.columns(3)
with c_w: weight = st.number_input("الوزن (كجم):", value=60.0)
with c_h: height = st.number_input("الطول (سم):", value=160.0)
with c_b: 
    if st.button("احسبي BMI"):
        bmi = weight / ((height/100)**2)
        st.success(f"مؤشر جسمك: {bmi:.1f}")

st.write("---")

# 3. جدول التمارين اليومي
st.header("📅 الجدول اليومي المعتاد")
day = st.selectbox("اختر اليوم:", ["السبت", "الأحد", "الاثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة"])
num_v = st.radio("عدد التمارين:", [1, 2, 3], horizontal=True)

workout_db = {
    "السبت": ["https://www.youtube.com/watch?v=2MoGxae-zyo", "https://www.youtube.com/watch?v=kzdv496atj4", "https://www.youtube.com/watch?v=lhotxON97xA"],
    "الأحد": ["https://www.youtube.com/watch?v=Z6jUPvbOviQ", "https://www.youtube.com/watch?v=9_5aT9cXe54", "https://www.youtube.com/watch?v=ML68QETssnU"]
}
vids = workout_db.get(day, workout_db["السبت"])
for i in range(num_v): st.video(vids[i])

st.write("---")

# 4. الكاميرا والماء
col_cam, col_wat = st.columns(2)
with col_cam:
    st.header("📸 الكاميرا")
    cam_side = st.radio("العدسة:", ["الأمامية", "الخلفية"], horizontal=True)
