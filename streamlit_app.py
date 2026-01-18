import streamlit as st

# 1. إعدادات الصفحة والألوان (الروز والبنفسجي)
st.set_page_config(page_title="تطبيق الروز الرياضي", page_icon="🌹")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #fff5f8 0%, #f3e5f5 100%);
    }
    h1, h2, h3 { color: #d81b60 !important; text-align: center; }
    .stButton>button { background-color: #d81b60; color: white; border-radius: 20px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# 2. واجهة التطبيق والصورة التي طلبتِها
st.title("تطبيق الروز الرياضي 🌹")

# صورة تعبيرية للياقة البدنية (تشبه طلبك)
st.image("https://images.unsplash.com/photo-1518310383802-640c2de311b2?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80", caption="لياقة وأناقة مع الروز")

st.write("---")

# 3. قسم الكاميرا
st.header("📸 مدرب الكاميرا الذكي")
st.camera_input("التقطي صورة لوضعية تمرينك")

# 4. قسم القياسات (الطول والوزن)
st.header("⚖️ حساب مؤشر الكتلة (BMI)")
col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("الوزن (كجم)", min_value=30.0, max_value=200.0, value=60.0)
with col2:
    height = st.number_input("الطول (سم)", min_value=100.0, max_value=250.0, value=160.0)

if st.button("احسبي المؤشر الآن"):
    bmi = weight / ((height/100)**2)
    st.success(f"مؤشر كتلة جسمك هو: {bmi:.1f}")

# 5. قسم الفيديوهات (الروابط)
st.header("🎥 تمارين مختارة")
st.video("https://www.youtube.com/watch?v=v7AYKMP6rOE")

st.write("---")
st.subheader("مستشار الروز الذكي 🧠")
user_query = st.text_input("اسألي الروز أي سؤال رياضي:")

st.markdown("<p style='text-align: center;'>جميع الحقوق محفوظة - تطبيق الروز 2024</p>", unsafe_allow_html=True)
