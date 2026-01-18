import streamlit as st

# 1. إعدادات الصفحة والاسم الجديد
st.set_page_config(page_title="تطبيق الروز الرياضي", page_icon="🌹")

# 2. تغيير الخلفية لواجهة رسومية (متدرجة الألوان) تدل على النشاط
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #ff9a9e 0%, #fecfef 99%, #fecfef 100%);
    }
    h1 {
        color: #d11141;
        text-align: center;
        font-family: 'Arial';
    }
    </style>
    """, unsafe_allow_html=True)

# الاسم الجديد
st.title("تطبيق الروز الرياضي 🌹")

# 3. حل مشكلة الصورة (استخدام رابط مباشر وموثوق)
st.image("https://img.freepik.com/free-vector/fitness-stats-concept-illustration_114360-5125.jpg", 
         caption="انطلقي مع الروز نحو حياة صحية")

# رادار الأهداف
st.subheader("📊 رادار الأهداف والقياسات")
col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("وزنك الحالي (كجم)", value=65.0)
with col2:
    target = st.number_input("هدفك (كجم)", value=55.0)

diff = weight - target
if diff > 0:
    st.info(f"متبقي لكِ {diff:.1f} كجم للوصول للهدف. استمري!")

# مستشار الروز الذكي
st.subheader("🧠 مستشار الروز الذكي")
user_input = st.text_input("ما هي خطتك أو تمرينك اليوم؟")

if user_input:
    st.write("💡 نصيحة الروز: شرب الماء قبل التمرين بـ 30 دقيقة يحسن أداءك.")
    st.video("https://www.youtube.com/watch?v=1f8yoFFdkBY")
