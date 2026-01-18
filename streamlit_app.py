import streamlit as st
import re

# 1. إعدادات الهوية البصرية والتصميم (تطبيق الروز)
st.set_page_config(page_title="تطبيق الروز الرياضي", page_icon="🌹", layout="wide")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #fff5f8 0%, #f3e5f5 100%); }
    h1, h2, h3 { color: #d81b60 !important; text-align: center; }
    .stButton>button { background-color: #ff4b91; color: white; border-radius: 20px; font-weight: bold; width: 100%; border: none; }
    .done-box { background-color: #e8f5e9; padding: 15px; border-radius: 15px; border: 1px solid #4caf50; color: #2e7d32; text-align: center; font-weight: bold; margin-top: 10px; }
    .report-box { background-color: white; padding: 20px; border-radius: 15px; border-right: 5px solid #d81b60; margin-top: 10px; }
    .stMetric { background: white; padding: 15px; border-radius: 15px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# 2. الواجهة الرئيسية والصورة
st.title("تطبيق الروز الرياضي الشامل 🌹")
st.image("https://images.unsplash.com/photo-1518310383802-640c2de311b2?ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80", caption="رفيقتك الذكية نحو الرشاقة والأناقة")

# 3. قسم القياسات (الطول والوزن)
st.header("⚖️ رادار القياسات والأهداف")
col_w, col_h, col_bmi = st.columns(3)
with col_w:
    weight = st.number_input("الوزن (كجم):", value=60.0)
with col_h:
    height = st.number_input("الطول (سم):", value=160.0)
with col_bmi:
    if st.button("احسبي مؤشر الجسم"):
        bmi = weight / ((height/100)**2)
        st.success(f"مؤشر جسمك: {bmi:.1f}")

st.write("---")

# 4. جدول التمارين مع (اختيار العدد) و (إشارة الإنجاز ✅)
st.header("📅 جدول التمارين وإشارات الإنجاز")
day_col, num_col = st.columns([2, 1])
with day_col:
    day = st.selectbox("اختر اليوم:", ["السبت", "الأحد", "الاثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة"])
with num_col:
    num_v = st.radio("عدد تمارين اليوم:", [1, 2, 3], horizontal=True)

# قاعدة بيانات الفيديوهات (كلوي تينغ + مدربين عالميين وعرب)
workout_db = {
    "السبت": ["https://www.youtube.com/watch?v=2MoGxae-zyo", "https://www.youtube.com/watch?v=kzdv496atj4", "https://www.youtube.com/watch?v=lhotxON97xA"],
    "الأحد": ["https://www.youtube.com/watch?v=Z6jUPvbOviQ", "https://www.youtube.com/watch?v=9_5aT9cXe54", "https://www.youtube.com/watch?v=ML68QETssnU"],
    "الاثنين": ["https://www.youtube.com/watch?v=Ig1TTq_vsPg", "https://www.youtube.com/watch?v=qEZMsECrRGg", "https://www.youtube.com/watch?v=sEDGAXnPpe0"],
    "الثلاثاء": ["https://www.youtube.com/watch?v=v7AYKMP6rOE", "https://www.youtube.com/watch?v=1f8yoFFdkBY", "https://www.youtube.com/watch?v=8BcPHWG8pI0"],
    "الأربعاء": ["https://www.youtube.com/watch?v=mGvzVjuY8SY", "https://www.youtube.com/watch?v=X1T3p_69m5A", "https://www.youtube.com/watch?v=4pLUleLgzZ4"],
    "الخميس": ["https://www.youtube.com/watch?v=BS2euIs5MXI", "https://www.youtube.com/watch?v=2MoGxae-zyo", "https://www.youtube.com/watch?v=Z6jUPvbOviQ"],
    "الجمعة": ["https://www.youtube.com/watch?v=kzdv496atj4", "https://www.youtube.com/watch?v=ML68QETssnU", "https://www.youtube.com/watch?v=Ig1TTq_vsPg"]
}

selected_vids = workout_db[day]

# عرض التمارين مع خاصية "تم الإنجاز"
for i in range(num_v):
    st.subheader(f"التمرين رقم {i+1} ✨")
    st.video(selected_vids[i])
    if st.checkbox(f"لقد أتممت التمرين رقم {i+1}! ✅", key=f"check_{day}_{i}"):
        st.markdown(f"<div class='done-box'>أحسنتِ يا بطلة! تم تسجيل التمرين رقم {i+1} كإنجاز اليوم 🏆</div>", unsafe_allow_html=True)
    st.write("---")

# 5. الكاميرا (تبديل العدسة) وعداد الماء
col_cam, col_wat = st.columns(2)
with col_cam:
    st.header("📸 الكاميرا الذكية")
    cam_side = st.radio("نوع الكاميرا:", ["الأمامية", "الخلفية"], horizontal=True)
    st.camera_input("صوري وجبتك أو تقدمك")

with col_wat:
    st.header("💧 مراقب شرب الماء")
    if 'water_cups' not in st.session_state: st.session_state.water_cups = 0
    st.metric("أكواب الماء", f"{st.session_state.water_cups} / 12")
    if st.button("➕ إضافة كوب"):
        st.session_state.water_cups += 1
        st.rerun()

st.write("---")

# 6. مستشار الروز الذكي (AI) مع خاصية قراءة الروابط
st.header("🤖 مستشار الروز الذكي (AI Reports)")
st.info("الصقي خطة ChatGPT أو Gemini هنا، وسأقوم بتشغيل الفيديوهات لكِ فوراً!")
ai_text = st.text_area("ضعي النص أو الخطة هنا:", height=150)

if ai_text:
    st.markdown("### 📋 خطتك المنظمة:")
    st.markdown(f'<div class="report-box">{ai_text}</div>', unsafe_allow_html=True)
    
    # استخراج الروابط من نص الذكاء الاصطناعي
    found_links = re.findall(r'(https?://[^\s]+)', ai_text)
    if found_links:
        st.subheader("🎥 فيديوهات الخطة المكتشفة:")
        for link in found_links:
            if "youtube.com" in link or "youtu.be" in link:
                st.video(link)

st.markdown("<p style='text-align: center; color: gray;'>جميع الحقوق محفوظة - تطبيق الروز الرياضي 2026</p>", unsafe_allow_html=True)
