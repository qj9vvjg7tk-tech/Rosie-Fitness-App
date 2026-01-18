import streamlit as st

# 1. إعدادات التصميم والألوان الكاملة
st.set_page_config(page_title="تطبيق الروز الرياضي", page_icon="🌹")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #fff5f8 0%, #f3e5f5 100%);
    }
    h1, h2, h3 { color: #d81b60 !important; text-align: center; }
    .exercise-box {
        background-color: white;
        padding: 15px;
        border-radius: 15px;
        border-right: 5px solid #d81b60;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. الواجهة والصورة
st.title("تطبيق الروز الرياضي 🌹")
st.image("https://images.unsplash.com/photo-1518310383802-640c2de311b2?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80")

# 3. الأدوات التفاعلية (جديد)
st.header("📸 مدرب الكاميرا والحاسبة")
tab1, tab2 = st.tabs(["الكاميرا الذكية", "حساب الوزن والطول"])

with tab1:
    st.camera_input("التقطي صورة لوضعية التمرين")

with tab2:
    weight = st.number_input("الوزن (كجم)", value=60.0)
    height = st.number_input("الطول (سم)", value=160.0)
    if st.button("احسبي المؤشر"):
        bmi = weight / ((height/100)**2)
        st.success(f"مؤشر كتلة جسمك: {bmi:.1f}")

st.write("---")

# 4. جدول الأيام والتمارين (التي كانت موجودة سابقاً)
st.header("📅 جدولك الأسبوعي للتمارين")
day = st.selectbox("اختاري اليوم لعرض التمارين:", 
                  ["السبت", "الأحد", "الاثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة"])

exercises = {
    "السبت": {"task": "تمارين كارديو وحرق دهون", "video": "https://www.youtube.com/watch?v=v7AYKMP6rOE"},
    "الأحد": {"task": "تمارين شد البطن والخصر", "video": "https://www.youtube.com/watch?v=v7AYKMP6rOE"},
    "الاثنين": {"task": "تمارين الجزء السفلي (أرجل)", "video": "https://www.youtube.com/watch?v=v7AYKMP6rOE"},
    "الثلاثاء": {"task": "راحة واستشفاء (يوم اليوغا)", "video": "https://www.youtube.com/watch?v=v7AYKMP6rOE"},
    "الأربعاء": {"task": "تمارين شد الذراعين والظهر", "video": "https://www.youtube.com/watch?v=v7AYKMP6rOE"},
    "الخميس": {"task": "تمارين كامل الجسم (هيت)", "video": "https://www.youtube.com/watch?v=v7AYKMP6rOE"},
    "الجمعة": {"task": "مشي حر ونشاط خارجي", "video": "https://www.youtube.com/watch?v=v7AYKMP6rOE"}
}

st.markdown(f"<div class='exercise-box'><h3>تمرين يوم {day}</h3><p style='text-align:center;'>{exercises[day]['task']}</p></div>", unsafe_allow_html=True)
st.video(exercises[day]['video'])

# 5. المستشار الذكي
st.write("---")
st.subheader("مستشار الروز الذكي 🧠")
user_query = st.text_input("اسألي الروز أي سؤال رياضي:")

st.markdown("<p style='text-align: center;'>جميع الحقوق محفوظة - تطبيق الروز 2026</p>", unsafe_allow_html=True)
