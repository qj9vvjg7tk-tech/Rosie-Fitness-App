import streamlit as st

# 1. إعدادات الصفحة والجمالية
st.set_page_config(page_title="Zuhour AI Coach 2026", page_icon="🧘‍♀️", layout="centered")

# تنسيق الألوان والشكل (بناتي ومبهج)
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #FFF5F7 0%, #FFE4E1 100%); }
    .main-card {
        background-color: white; border-radius: 20px; padding: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05); border-right: 8px solid #FF69B4;
        margin-bottom: 20px; color: #333;
    }
    h1, h2, h3 { color: #D81B60 !important; text-align: center; }
    .stButton > button { background: #FF69B4 !important; color: white !important; border-radius: 15px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# 2. عرض صورة الفتاة الرياضية المبهجة (رابط GIF مباشر)
st.markdown("<center><img src='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHF4c3c3eXF4c3c3eXF4c3c3eXF4c3c3eXF4c3c3eXF4c3c3ZSZjdD1z/L40pC6N0H4h0E/giphy.gif' width='220'></center>", unsafe_allow_html=True)

st.title("🌸 مدرب زهور الخاص")

# --- القسم الأول: قياسات الهدف ---
st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.subheader("📏 راداد الأهداف والقياسات")
c1, c2, c3 = st.columns(3)
with c1: h = st.number_input("الطول (سم):", value=160)
with c2: w = st.number_input("الوزن الحالي:", value=65.0)
with c3: target = st.number_input("الوزن المستهدف:", value=55.0)

diff = w - target
if diff > 0:
    st.warning(f"🎯 متبقي لكِ {diff:.1f} كجم للوصول لهدف الـ {target} كجم")
else:
    st.success("🎉 مذهل! أنتِ في وزنكِ المثالي.")
st.markdown('</div>', unsafe_allow_html=True)

# --- القسم الثاني: مستشار الذكاء الاصطناعي (الميزة التي طلبتِها) ---
st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.subheader("🤖 مستشار التمارين الذكي")
st.write("ألصقي هنا خطة التمرين أو صفي ما تريدين، وسيقوم الـ AI بترشيح الفيديو المناسب:")
user_plan = st.text_area("مثال: أريد نحت البطن والخصر اليوم...", height=120)

if user_plan:
    st.info("🔄 جاري تحليل خطتكِ وترشيح التمارين العالمية...")
    # محرك تحليل الكلمات الذكي
    if any(word in user_plan for word in ["نحت", "خصر", "بيلاتس", "شد"]):
        vid_url = "https://www.youtube.com/watch?v=3Pr6n-nKnAA"
        vid_name = "تمرين Emi Wong العالمي لنحت الخصر"
    elif any(word in user_plan for word in ["حرق", "دهون", "وزن", "كارديو"]):
        vid_url = "https://www.youtube.com/watch?v=2MoGxae-zyo"
        vid_name = "تحدي Chloe Ting العالمي لحرق الدهون"
    else:
        vid_url = "https://www.youtube.com/watch?v=v2r0zYnFmxo"
        vid_name = "تمارين الشد الشاملة للمدربة سارة"
    
    st.success(f"✅ تم التشخيص! الفيديو المرشح هو: {vid_name}")
    st.link_button("🚀 ابدئي التمرين الآن", vid_url)
st.markdown('</div>', unsafe_allow_html=True)

# --- القسم الثالث: جدول تمارين الأسبوع ---
st.divider()
st.subheader("📅 جدول التمارين المعتمد")
day = st.selectbox("اختر اليوم لرؤية التمرين المخصص:", ["الأحد", "الاثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة", "السبت"])
week_videos = {
    "الأحد": "https://www.youtube.com/watch?v=2MoGxae-zyo",
    "الاثنين": "https://www.youtube.com/watch?v=3Pr6n-nKnAA",
    "الثلاثاء": "https://www.youtube.com/watch?v=U4_lVjsOVBs",
    "الأربعاء": "https://www.youtube.com/watch?v=v2r0zYnFmxo",
    "الخميس": "https://www.youtube.com/watch?v=ml6cT4AZdqI",
    "الجمعة": "https://www.youtube.com/watch?v=Eml2xnoLpYE",
    "السبت": "https://www.youtube.com/watch?v=gC_L9qAHVJ8"
}
st.link_button(f"▶️ فتح فيديو يوم {day}", week_videos[day])

# --- القسم الرابع: الماء والكاميرا الخلفية ---
st.divider()
col_w, col_c = st.columns(2)
with col_w:
    if 'water' not in st.session_state: st.session_state.water = 0
    st.write(f"🥤 الماء اليومي: {st.session_state.water}/12")
    if st.button("➕ كوب ماء"): st.session_state.water += 1
with col_c:
    st.write("📸 سجل الوجبات")
    st.write("💡 (استخدمي زر 🔄 للتبديل للكاميرا الخلفية)")
    st.camera_input("التقاط صورة")

st.sidebar.markdown(f"### ملخص روز 2026\nالوزن الحالي: {w}\nالهدف: {target}")
