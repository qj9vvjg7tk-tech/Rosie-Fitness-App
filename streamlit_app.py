import streamlit as st

# 1. إعدادات التصميم (الوردية الأنيقة)
st.set_page_config(page_title="Zuhour AI Coach", page_icon="🌹")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #fff5f8 0%, #f3e5f5 100%); }
    h1, h2, h3 { color: #d81b60 !important; text-align: center; }
    .stButton>button { background-color: #ff4b91; color: white; border-radius: 20px; width: 100%; }
    .water-box { background-color: #ffe4ed; padding: 20px; border-radius: 15px; text-align: center; border: 1px solid #ffc1d3; }
    </style>
    """, unsafe_allow_html=True)

st.title("Zuhour AI Coach 🌹")

# 2. عداد شرب الماء (التفاعلي)
st.header("💧 مراقب شرب الماء")
if 'water_cups' not in st.session_state:
    st.session_state.water_cups = 0

with st.container():
    st.markdown(f"<div class='water-box'><h3>الماء: {st.session_state.water_cups} / 12 كوب</h3></div>", unsafe_allow_html=True)
    if st.button("➕ إضافة كوب ماء"):
        if st.session_state.water_cups < 12:
            st.session_state.water_cups += 1
            st.rerun()

st.write("---")

# 3. ميزة تبديل الكاميرا (الحل الذي طلبتِه)
st.header("📸 الكاميرا الذكية")
camera_choice = st.radio("اختاري الكاميرا التي تودين استخدامها:", ("الأمامية (سيلفي)", "الخلفية"), horizontal=True)

if camera_choice == "الخلفية":
    st.info("سيتم محاولة فتح الكاميرا الخلفية (يعتمد على دعم متصفحك)")
    picture = st.camera_input("التقطي صورة لوضعية التمرين (خلفية)")
else:
    picture = st.camera_input("التقطي صورة لوضعية التمرين (أمامية)")

st.write("---")

# 4. جدول التمارين واختيار عدد الفيديوهات
st.header("📅 جدول تمارين الأسبوع")
day = st.selectbox("اختر اليوم:", ["السبت", "الأحد", "الاثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة"])
num_videos = st.select_slider("كم تمرين تودين القيام به اليوم؟", options=[1, 2, 3])

# روابط فيديوهات (مجموعة متنوعة)
workout_links = [
    "https://www.youtube.com/watch?v=v7AYKMP6rOE",
    "https://www.youtube.com/watch?v=1f8yoFFdkBY",
    "https://www.youtube.com/watch?v=ML68QETssnU"
]

st.subheader(f"تمارين يوم {day} ✨")
for i in range(num_videos):
    st.video(workout_links[i])

# 5. حساب مؤشر الكتلة
st.header("⚖️ رادار القياسات")
col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("الوزن (كجم):", value=60.0)
with col2:
    height = st.number_input("الطول (سم):", value=160.0)

if st.button("تحليل الجسم"):
    bmi = weight / ((height/100)**2)
    st.success(f"مؤشر كتلة جسمك: {bmi:.1f}")

st.markdown("<p style='text-align: center; color: gray;'>Zuhour AI Coach 2026</p>", unsafe_allow_html=True)
