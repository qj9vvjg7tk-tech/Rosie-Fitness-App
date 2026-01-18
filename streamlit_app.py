import streamlit as st
import re

# 1. إعدادات التصميم والاسم الأصلي
st.set_page_config(page_title="تطبيق الروز الرياضي", page_icon="🌹", layout="wide")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #fff5f8 0%, #f3e5f5 100%); }
    h1, h2, h3 { color: #d81b60 !important; text-align: center; }
    .stButton>button { background-color: #ff4b91; color: white; border-radius: 20px; font-weight: bold; width: 100%; }
    .report-box { background-color: white; padding: 20px; border-radius: 15px; border-right: 5px solid #d81b60; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("تطبيق الروز الرياضي الشامل 🌹")
st.image("https://images.unsplash.com/photo-1518310383802-640c2de311b2?ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80")

# 2. قسم القياسات (الطول والوزن)
st.header("⚖️ القياسات والأهداف")
c_w, c_h, c_b = st.columns(3)
with c_w: weight = st.number_input("الوزن (كجم):", value=60.0)
with c_h: height = st.number_input("الطول (سم):", value=160.0)
with c_b: 
    if st.button("احسبي BMI"):
        bmi = weight / ((height/100)**2)
        st.success(f"مؤشر جسمك: {bmi:.1f}")

st.write("---")

# 3. جدول التمارين اليومي واختيار العدد
st.header("📅 الجدول اليومي العالمي")
day_col, num_col = st.columns([2, 1])
with day_col:
    day = st.selectbox("اختر اليوم:", ["السبت", "الأحد", "الاثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة"])
with num_col:
    num_v = st.radio("عدد التمارين:", [1, 2, 3], horizontal=True)

workout_db = {
    "السبت": ["https://www.youtube.com/watch?v=2MoGxae-zyo", "https://www.youtube.com/watch?v=kzdv496atj4", "https://www.youtube.com/watch?v=lhotxON97xA"],
    "الأحد": ["https://www.youtube.com/watch?v=Z6jUPvbOviQ", "https://www.youtube.com/watch?v=9_5aT9cXe54", "https://www.youtube.com/watch?v=ML68QETssnU"],
    "الاثنين": ["https://www.youtube.com/watch?v=Ig1TTq_vsPg", "https://www.youtube.com/watch?v=qEZMsECrRGg", "https://www.youtube.com/watch?v=sEDGAXnPpe0"],
    "الثلاثاء": ["https://www.youtube.com/watch?v=v7AYKMP6rOE", "https://www.youtube.com/watch?v=1f8yoFFdkBY", "https://www.youtube.com/watch?v=8BcPHWG8pI0"],
    "الأربعاء": ["https://www.youtube.com/watch?v=mGvzVjuY8SY", "https://www.youtube.com/watch?v=X1T3p_69m5A", "https://www.youtube.com/watch?v=4pLUleLgzZ4"],
    "الخميس": ["https://www.youtube.com/watch?v=BS2euIs5MXI", "https://www.youtube.com/watch?v=2MoGxae-zyo", "https://www.youtube.com/watch?v=Z6jUPvbOviQ"],
    "الجمعة": ["https://www.youtube.com/watch?v=kzdv496atj4", "https://www.youtube.com/watch?v=ML68QETssnU", "https://www.youtube.com/watch?v=Ig1TTq_vsPg"]
}

vids = workout_db[day]
for i in range(num_v): st.video(vids[i])

st.write("---")

# 4. الكاميرا والماء (تأكدت من وجودهما)
col_cam, col_wat = st.columns(2)
with col_cam:
    st.header("📸 الكاميرا")
    cam_side = st.radio("نوع الكاميرا:", ["الأمامية", "الخلفية"], horizontal=True)
    st.camera_input("تابعي وضعية تمرينك")
with col_wat:
    st.header("💧 مراقب الماء")
    if 'w_c' not in st.session_state: st.session_state.w_c = 0
    st.metric("أكواب اليوم", f"{st.session_state.w_c} / 12")
    if st.button("➕ إضافة كوب ماء"):
        st.session_state.w_c += 1
        st.rerun()

st.write("---")

# 5. مستشار الروز الذكي (الميزة المصححة لقراءة الروابط)
st.header("🤖 مستشار الروز الذكي (AI Reports)")
st.info("الصقي خطة ChatGPT هنا، وسأقوم بتشغيل الفيديوهات لكِ فوراً!")
ai_plan = st.text_area("ضعي النص هنا (سأقوم باستخراج الفيديوهات منه تلقائياً):", height=150)

if ai_plan:
    st.markdown("### 📋 خطتك المقترحة:")
    st.markdown(f'<div class="report-box">{ai_plan}</div>', unsafe_allow_html=True)
    
    # كود استخراج الروابط وتشغيلها
    links = re.findall(r'(https?://[^\s]+)', ai_plan)
    if links:
        st.subheader("🎥 الفيديوهات المكتشفة في خطتك:")
        for link in links:
            if "youtube.com" in link or "youtu.be" in link:
                st.video(link)

st.markdown("<p style='text-align: center; color: gray;'>تطبيق الروز الرياضي 2026</p>", unsafe_allow_html=True)
