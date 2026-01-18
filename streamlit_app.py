import streamlit as st

# 1. إعدادات الهوية البصرية والتصميم (الروز الرياضي)
st.set_page_config(page_title="تطبيق الروز الرياضي", page_icon="🌹", layout="wide")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #fff5f8 0%, #f3e5f5 100%); }
    h1, h2, h3 { color: #d81b60 !important; text-align: center; font-family: 'Arial'; }
    .stButton>button { background-color: #ff4b91; color: white; border-radius: 20px; width: 100%; border: none; font-weight: bold; }
    .report-box { background-color: #ffffff; padding: 20px; border-radius: 15px; border-left: 5px solid #ff4b91; margin: 10px 0; }
    </style>
    """, unsafe_allow_html=True)

# 2. الواجهة الرئيسية والصورة الترحيبية
st.title("تطبيق الروز الرياضي الشامل 🌹")
st.image("https://images.unsplash.com/photo-1518310383802-640c2de311b2?ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80", caption="رفيقتك الذكية نحو الرشاقة والأناقة")

# تقسيم الصفحة إلى أعمدة لمظهر أكثر احترافية
col_main, col_side = st.columns([2, 1])

with col_main:
    # 3. جدول التمارين (مدربين عرب وأجانب - مختارات عالمية)
    st.header("📅 جدول التمارين المتنوع")
    day = st.selectbox("اختر اليوم لاستعراض تمارينك:", ["السبت", "الأحد", "الاثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة"])
    
    # روابط فيديوهات مختارة بعناية (كلوي تينغ، سارة بوب فيت، باميلا ريف)
    workout_links = {
        "السبت": ["https://www.youtube.com/watch?v=2MoGxae-zyo", "https://www.youtube.com/watch?v=kzdv496atj4"], # كلوي تينغ (أجنبي)
        "الأحد": ["https://www.youtube.com/watch?v=lhotxON97xA", "https://www.youtube.com/watch?v=ML68QETssnU"], # سارة بوب فيت (عربي)
        "الاثنين": ["https://www.youtube.com/watch?v=Z6jUPvbOviQ", "https://www.youtube.com/watch?v=9_5aT9cXe54"], # باميلا ريف (أجنبي)
        "الثلاثاء": ["https://www.youtube.com/watch?v=v7AYKMP6rOE", "https://www.youtube.com/watch?v=8BcPHWG8pI0"], # تمارين كارديو متنوعة
        "الأربعاء": ["https://www.youtube.com/watch?v=mGvzVjuY8SY", "https://www.youtube.com/watch?v=Ig1TTq_vsPg"], # يوغا واسترخاء
        "الخميس": ["https://www.youtube.com/watch?v=BS2euIs5MXI", "https://www.youtube.com/watch?v=qEZMsECrRGg"], # مقاومة وشد
        "الجمعة": ["https://www.youtube.com/watch?v=X1T3p_69m5A", "https://www.youtube.com/watch?v=4pLUleLgzZ4"]  # يوم النشاط الحر
    }
    
    selected_vids = workout_links[day]
    st.subheader(f"تمارين يوم {day} ✨")
    for vid in selected_vids:
        st.video(vid)

with col_side:
    # 4. مراقب الماء (الميزة السابقة)
    st.header("💧 مراقب الماء")
    if 'water_count' not in st.session_state: st.session_state.water_count = 0
    st.metric("أكواب اليوم", f"{st.session_state.water_count} / 10")
    if st.button("➕ إضافة كوب"):
        st.session_state.water_count += 1
        st.rerun()
    
    st.write("---")
    
    # 5. الكاميرا والتحليل
    st.header("📸 الكاميرا")
    st.camera_input("التقطي صورة لمتابعة تقدمك")

st.write("---")

# 6. ميزة تقارير الذكاء الاصطناعي (ChatGPT/Gemini) - ميزة احترافية اختيارية
st.header("🤖 مستشار الروز الذكي (تقارير AI)")
st.info("إذا حصلتِ على خطة تدريبية من ChatGPT أو Gemini، يمكنكِ لصقها هنا لتنظيمها داخل التطبيق.")

ai_report = st.text_area("الصقي خطتك التدريبية أو تقريرك الصحي هنا:", height=150, placeholder="مثال: خطة السبعة أيام لحرق الدهون...")

if ai_report:
    st.subheader("📋 خطتك التدريبية المنظمة:")
    st.markdown(f'<div class="report-box">{ai_report}</div>', unsafe_allow_html=True)
    st.success("تم دمج الخطة بنجاح في واجهة التطبيق!")

# تذييل الصفحة
st.markdown("<br><p style='text-align: center; color: #888;'>جميع الحقوق محفوظة - تطبيق الروز الرياضي الذكي 2026</p>", unsafe_allow_html=True)
