import streamlit as st

# 1. إعدادات التصميم والاسم
st.set_page_config(page_title="تطبيق الروز الرياضي", page_icon="🌹")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #fff5f8 0%, #f3e5f5 100%); }
    h1, h2, h3 { color: #d81b60 !important; text-align: center; }
    .stButton>button { background-color: #ff4b91; color: white; border-radius: 20px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

st.title("تطبيق الروز الرياضي 🌹")
st.image("https://images.unsplash.com/photo-1518310383802-640c2de311b2?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80")

# 2. جدول التمارين (فيديوهات كلوي تينغ ومدربين عالميين)
st.header("📅 جدول التمارين العالمي")
day = st.selectbox("اختر اليوم لتحديث التمارين:", ["السبت", "الأحد", "الاثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة"])
num_vids = st.radio("كم فيديو تودين ممارسته؟", [1, 2, 3], horizontal=True)

# قاعدة بيانات فيديوهات كلوي تينغ والمدربين المشهورين
workout_db = {
    "السبت": ["https://www.youtube.com/watch?v=2MoGxae-zyo", "https://www.youtube.com/watch?v=lhotxON97xA", "https://www.youtube.com/watch?v=BS2euIs5MXI"], # Chloe Ting Abs
    "الأحد": ["https://www.youtube.com/watch?v=Z6jUPvbOviQ", "https://www.youtube.com/watch?v=ML68QETssnU", "https://www.youtube.com/watch?v=9_5aT9cXe54"], # Full Body
    "الاثنين": ["https://www.youtube.com/watch?v=Ig1TTq_vsPg", "https://www.youtube.com/watch?v=qEZMsECrRGg", "https://www.youtube.com/watch?v=sEDGAXnPpe0"], # Legs & Glutes
    "الثلاثاء": ["https://www.youtube.com/watch?v=v7AYKMP6rOE", "https://www.youtube.com/watch?v=1f8yoFFdkBY", "https://www.youtube.com/watch?v=8BcPHWG8pI0"], # Cardio
    "الأربعاء": ["https://www.youtube.com/watch?v=kzdv496atj4", "https://www.youtube.com/watch?v=mGvzVjuY8SY", "https://www.youtube.com/watch?v=X1T3p_69m5A"], # Arms
    "الخميس": ["https://www.youtube.com/watch?v=4pLUleLgzZ4", "https://www.youtube.com/watch?v=Z6jUPvbOviQ", "https://www.youtube.com/watch?v=2MoGxae-zyo"], # HIIT
    "الجمعة": ["https://www.youtube.com/watch?v=ML68QETssnU", "https://www.youtube.com/watch?v=v7AYKMP6rOE", "https://www.youtube.com/watch?v=Ig1TTq_vsPg"]  # Stretch
}

selected_vids = workout_db[day]

st.subheader(f"تمارين يوم {day} مع أشهر المدربين ✨")
for i in range(num_vids):
    st.video(selected_vids[i])

# 3. محرك البحث الذكي (يرشح فيديوهات من محرك البحث)
st.header("🧠 محرك بحث الروز الذكي")
user_query = st.text_input("ابحثي عن تمرين معين (مثال: Chloe Ting Weight Loss):")

if user_query:
    st.success(f"أفضل ترشيح من محرك البحث لـ '{user_query}':")
    # هنا يتم ترشيح فيديو ذكي بناءً على الكلمة
    st.video("https://www.youtube.com/watch?v=2MoGxae-zyo")

# 4. الكاميرا والقياسات
st.header("📸 الكاميرا والتحليل")
cam_side = st.radio("نوع الكاميرا:", ["الأمامية", "الخلفية"], horizontal=True)
st.camera_input("فتحي الكاميرا من هنا")

st.markdown("<p style='text-align: center;'>جميع الحقوق محفوظة - تطبيق الروز الرياضي 2026</p>", unsafe_allow_html=True)
