import streamlit as st

# 1. إعدادات الصفحة والتنسيق الجمالي (تطبيق الروز)
st.set_page_config(page_title="تطبيق الروز الرياضي", page_icon="🌹", layout="wide")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #fff5f8 0%, #f3e5f5 100%); }
    h1, h2, h3 { color: #d81b60 !important; text-align: center; }
    .stButton>button { background-color: #ff4b91; color: white; border-radius: 20px; font-weight: bold; width: 100%; border: none; }
    .stMetric { background-color: white; padding: 10px; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# 2. الواجهة الرئيسية
st.title("تطبيق الروز الرياضي الشامل 🌹")
st.image("https://images.unsplash.com/photo-1518310383802-640c2de311b2?ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80")

# 3. قسم القياسات (الطول والوزن)
st.header("⚖️ حساب مؤشر كتلة الجسم والأهداف")
col_w, col_h, col_res = st.columns(3)
with col_w:
    weight = st.number_input("الوزن الحالي (كجم):", min_value=30.0, max_value=200.0, value=60.0)
with col_h:
    height = st.number_input("الطول الحالي (سم):", min_value=100.0, max_value=250.0, value=160.0)
with col_res:
    if st.button("احسبي الآن"):
        bmi = weight / ((height/100)**2)
        st.success(f"مؤشر كتلتك هو: {bmi:.1f}")

st.write("---")

# 4. جدول التمارين المتغير مع خيار عدد الفيديوهات
st.header("📅 جدول التمارين والمدربين")
c1, c2 = st.columns([2, 1])
with c1:
    day = st.selectbox("اختاري اليوم لعرض تمارينك:", ["السبت", "الأحد", "الاثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة"])
with c2:
    num_vids = st.radio("عدد التمارين المفضلة:", [1, 2, 3], horizontal=True)

# قاعدة بيانات الروابط (تم اختيار فيديوهات شغالة وعالمية وعربية)
workout_db = {
    "السبت": ["https://www.youtube.com/watch?v=2MoGxae-zyo", "https://www.youtube.com/watch?v=kzdv496atj4", "https://www.youtube.com/watch?v=lhotxON97xA"],
    "الأحد": ["https://www.youtube.com/watch?v=Z6jUPvbOviQ", "https://www.youtube.com/watch?v=9_5aT9cXe54", "https://www.youtube.com/watch?v=ML68QETssnU"],
    "الاثنين": ["https://www.youtube.com/watch?v=Ig1TTq_vsPg", "https://www.youtube.com/watch?v=qEZMsECrRGg", "https://www.youtube.com/watch?v=sEDGAXnPpe0"],
    "الثلاثاء": ["https://www.youtube.com/watch?v=v7AYKMP6rOE", "https://www.youtube.com/watch?v=1f8yoFFdkBY", "https://www.youtube.com/watch?v=8BcPHWG8pI0"],
    "الأربعاء": ["https://www.youtube.com/watch?v=mGvzVjuY8SY", "https://www.youtube.com/watch?v=X1T3p_69m5A", "https://www.youtube.com/watch?v=4pLUleLgzZ4"],
    "الخميس": ["https://www.youtube.com/watch?v=BS2euIs5MXI", "https://www.youtube.com/watch?v=2MoGxae-zyo", "https://www.youtube.com/watch?v=Z6jUPvbOviQ"],
    "الجمعة": ["https://www.youtube.com/watch?v=kzdv496atj4", "https://www.youtube.com/watch?v=ML68QETssnU", "https://www.youtube.com/watch?v=Ig1TTq_vsPg"]
}

st.subheader(f"تمارين يوم {day} ✨")
vids = workout_db[day]
for i in range(num_vids):
    st.video(vids[i])

st.write("---")

# 5. الكاميرا وعداد الماء
col_cam, col_wat = st.columns(2)
with col_cam:
    st.header("📸 الكاميرا الذكية")
    cam_type = st.radio("اختاري الكاميرا:", ["الأمامية", "الخلفية"], horizontal=True)
    st.camera_input("التقطي صورة لمتابعة الوضعية")

with col_wat:
    st.header("💧 مراقب شرب الماء")
    if 'water_cup' not in st.session_state: st.session_state.water_cup = 0
    st.metric("أكواب اليوم", f"{st.session_state.water_cup} / 12")
    if st.button("➕ أضيفي كوب ماء"):
        st.session_state.water_cup += 1
        st.rerun()

st.write("---")

# 6. مستشار الذكاء الاصطناعي والتقارير
st.header("🤖 مستشار الروز الذكي (AI Reports)")
st.info("قومي بلصق خطة ChatGPT أو Gemini هنا لتحويلها لجدول منظم:")
ai_report = st.text_area("أو ابحثي عن تمرين معين هنا:", placeholder="مثال: أريد خطة لشد الجسم في شهر...")
if ai_report:
    st.markdown("### 📋 خطتك المقترحة:")
    st.write(ai_report)
    st.success("تم تحديث الخطة في ذكاء التطبيق!")

st.markdown("<p style='text-align: center; color: gray;'>تطبيق الروز الرياضي 2026 - جميع الحقوق محفوظة</p>", unsafe_allow_html=True)
