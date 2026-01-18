import streamlit as st

# 1. إعدادات الاسم والتنسيق
st.set_page_config(page_title="تطبيق الروز الرياضي", page_icon="🌹")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #fff5f8 0%, #f3e5f5 100%); }
    h1, h2, h3 { color: #d81b60 !important; text-align: center; }
    .stButton>button { background-color: #ff4b91; color: white; border-radius: 20px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# 2. واجهة التطبيق وصورة الفتاة الرياضية (التي طلبتِها)
st.title("تطبيق الروز الرياضي 🌹")
# هذه الصورة تعبر عن الرشاقة والأناقة الرياضية
st.image("https://images.unsplash.com/photo-1518310383802-640c2de311b2?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80", caption="لياقة وأناقة مع الروز")

st.write("---")

# 3. جدول التمارين المتغير يومياً (روابط فيديوهات مختلفة)
st.header("📅 جدول التمارين المتجدد")
day = st.selectbox("اختاري اليوم:", ["السبت", "الأحد", "الاثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة"])
num_vids = st.radio("كم فيديو تودين ممارسته اليوم؟", [1, 2, 3], horizontal=True)

# قاعدة بيانات الفيديوهات (كل يوم له روابطه الخاصة)
workout_links = {
    "السبت": ["https://www.youtube.com/watch?v=v7AYKMP6rOE", "https://www.youtube.com/watch?v=1f8yoFFdkBY", "https://www.youtube.com/watch?v=ML68QETssnU"],
    "الأحد": ["https://www.youtube.com/watch?v=8BcPHWG8pI0", "https://www.youtube.com/watch?v=X1T3p_69m5A", "https://www.youtube.com/watch?v=4pLUleLgzZ4"],
    "الاثنين": ["https://www.youtube.com/watch?v=kzdv496atj4", "https://www.youtube.com/watch?v=mGvzVjuY8SY", "https://www.youtube.com/watch?v=2MoGxae-zyo"],
    "الثلاثاء": ["https://www.youtube.com/watch?v=v7AYKMP6rOE", "https://www.youtube.com/watch?v=ML68QETssnU", "https://www.youtube.com/watch?v=8BcPHWG8pI0"],
    "الأربعاء": ["https://www.youtube.com/watch?v=X1T3p_69m5A", "https://www.youtube.com/watch?v=4pLUleLgzZ4", "https://www.youtube.com/watch?v=mGvzVjuY8SY"],
    "الخميس": ["https://www.youtube.com/watch?v=2MoGxae-zyo", "https://www.youtube.com/watch?v=kzdv496atj4", "https://www.youtube.com/watch?v=v7AYKMP6rOE"],
    "الجمعة": ["https://www.youtube.com/watch?v=8BcPHWG8pI0", "https://www.youtube.com/watch?v=X1T3p_69m5A", "https://www.youtube.com/watch?v=4pLUleLgzZ4"]
}

selected_day_vids = workout_links[day]

st.subheader(f"تمارين يوم {day} ✨")
for i in range(num_vids):
    st.video(selected_day_vids[i])

st.write("---")

# 4. المستشار الذكي (ترشيح بناءً على الحالة)
st.header("🧠 مستشار الروز الذكي")
user_input = st.text_input("صفي حالتك أو هدفك (مثال: أريد تمارين كارديو):")
if user_input:
    st.success(f"بناءً على طلبك لـ '{user_input}'، أرشح لكِ البدء بالفيديو الأول مع شرب كوب ماء إضافي.")

# 5. الكاميرا والقياسات
st.header("📸 الكاميرا والتحليل")
cam_side = st.radio("تبديل الكاميرا:", ["الأمامية", "الخلفية"], horizontal=True)
st.camera_input("فتحي الكاميرا من هنا")

st.markdown("<p style='text-align: center;'>جميع الحقوق محفوظة - تطبيق الروز الرياضي 2026</p>", unsafe_allow_html=True)
