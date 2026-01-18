import streamlit as st

# 1. إعدادات التصميم والاسم الأصلي
st.set_page_config(page_title="تطبيق الروز الرياضي", page_icon="🌹")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #fff5f8 0%, #f3e5f5 100%); }
    h1, h2, h3 { color: #d81b60 !important; text-align: center; }
    .stButton>button { background-color: #ff4b91; color: white; border-radius: 20px; width: 100%; }
    .info-box { background-color: white; padding: 15px; border-radius: 15px; border-right: 5px solid #d81b60; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("تطبيق الروز الرياضي 🌹")

# 2. عداد الماء (كما في الصورة السابقة)
st.header("💧 مراقب شرب الماء")
if 'water_cups' not in st.session_state: st.session_state.water_cups = 0
col1, col2 = st.columns([2, 1])
with col1: st.subheader(f"الماء: {st.session_state.water_cups} / 12 كوب")
with col2:
    if st.button("➕ إضافة كوب"):
        if st.session_state.water_cups < 12:
            st.session_state.water_cups += 1
            st.rerun()

st.write("---")

# 3. جدول التمارين الأسبوعي والفيديوهات المتجددة
st.header("📅 جدول التمارين الأسبوعي")
day = st.selectbox("اختاري اليوم لعرض تمارينك:", ["السبت", "الأحد", "الاثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة"])

# قاعدة بيانات الفيديوهات لكل يوم (يمكنك تغيير الروابط لروابطك الخاصة)
workout_db = {
    "السبت": ["https://www.youtube.com/watch?v=v7AYKMP6rOE", "https://www.youtube.com/watch?v=1f8yoFFdkBY", "https://www.youtube.com/watch?v=ML68QETssnU"],
    "الأحد": ["https://www.youtube.com/watch?v=8BcPHWG8pI0", "https://www.youtube.com/watch?v=X1T3p_69m5A", "https://www.youtube.com/watch?v=4pLUleLgzZ4"],
    "الاثنين": ["https://www.youtube.com/watch?v=1f8yoFFdkBY", "https://www.youtube.com/watch?v=v7AYKMP6rOE", "https://www.youtube.com/watch?v=ML68QETssnU"],
    "الثلاثاء": ["https://www.youtube.com/watch?v=4pLUleLgzZ4", "https://www.youtube.com/watch?v=8BcPHWG8pI0", "https://www.youtube.com/watch?v=X1T3p_69m5A"],
    "الأربعاء": ["https://www.youtube.com/watch?v=ML68QETssnU", "https://www.youtube.com/watch?v=1f8yoFFdkBY", "https://www.youtube.com/watch?v=v7AYKMP6rOE"],
    "الخميس": ["https://www.youtube.com/watch?v=X1T3p_69m5A", "https://www.youtube.com/watch?v=4pLUleLgzZ4", "https://www.youtube.com/watch?v=8BcPHWG8pI0"],
    "الجمعة": ["https://www.youtube.com/watch?v=v7AYKMP6rOE", "https://www.youtube.com/watch?v=ML68QETssnU", "https://www.youtube.com/watch?v=1f8yoFFdkBY"]
}

num_videos = st.radio("كم فيديو تودين ممارسته اليوم؟", [1, 2, 3], horizontal=True)

st.subheader(f"تمارين يوم {day} ✨")
selected_videos = workout_db[day]
for i in range(num_videos):
    st.video(selected_videos[i])

st.write("---")

# 4. الذكاء الاصطناعي والمستشار الذكي (ترشيح التمارين)
st.header("🧠 مستشار الروز الذكي")
st.write("أخبريني بحالتك الصحية أو هدفك اليوم وسأرشح لكِ ما يناسبك:")
user_goal = st.text_input("مثلاً: أريد تمارين لآلام الظهر، أو تمارين حرق سريعة")
if user_goal:
    st.info(f"بناءً على طلبك '{user_goal}'، أرشح لكِ التركيز على الفيديو الأول اليوم مع زيادة شرب الماء.")

st.write("---")

# 5. الكاميرا والقياسات
st.header("📸 الكاميرا والتحليل")
cam_type = st.radio("نوع الكاميرا:", ["الأمامية", "الخلفية"], horizontal=True)
st.camera_input("التقطي صورة لتحليل الوضعية")

weight = st.number_input("الوزن (كجم):", value=60.0)
height = st.number_input("الطول (سم):", value=160.0)
if st.button("تحليل مؤشر الجسم"):
    bmi = weight / ((height/100)**2)
    st.success(f"مؤشر كتلة جسمك: {bmi:.1f}")

st.markdown("<p style='text-align: center; color: gray;'>جميع الحقوق محفوظة - تطبيق الروز الرياضي 2026</p>", unsafe_allow_html=True)
