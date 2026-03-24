import streamlit as st

# 1. إعداد الصفحة - يجب أن يكون أول سطر في الكود
st.set_page_config(
    page_title="Rosie Elite 2026",
    page_icon="💎",
    layout="wide"
)

# 2. تصميم القائمة الجانبية
with st.sidebar:
    st.title("💎 Rosie Elite")
    st.markdown("---")
    menu = st.radio(
        "انتقل بين الأقسام:",
        ["🏠 الصفحة الرئيسية", "⚖️ حاسبة كتلة الجسم", "🥤 سجل شرب الماء", "📸 توثيق التقدم"]
    )
    st.write("---")
    st.caption("تم التطوير بواسطة Rosie v2.0")

# 3. منطق الصفحات
if menu == "🏠 الصفحة الرئيسية":
    st.header("👋 أهلاً بك في رحلتك الجديدة!")
    st.write("هذا التطبيق مصمم خصيصاً لمساعدتك على مراقبة صحتك ولياقتك البدنية.")
    
    # فيديو تحفيزي
    st.subheader("📺 فيديو تمرين مقترح اليوم")
    st.video("https://www.youtube.com/watch?v=2MoGxae-zyo")
    
    st.info("نصيحة اليوم: الاستمرارية أهم من السرعة. ابدأ بخطوات بسيطة!")

elif menu == "⚖️ حاسبة كتلة الجسم":
    st.header("⚖️ احسب مؤشر كتلة جسمك (BMI)")
    
    col1, col2 = st.columns(2)
    with col1:
        weight = st.number_input("الوزن (كيلوجرام):", min_value=10.0, max_value=250.0, value=70.0)
    with col2:
        height = st.number_input("الطول (سنتيمتر):", min_value=50.0, max_value=250.0, value=170.0)
    
    if st.button("احسب الآن"):
        bmi = weight / ((height/100)**2)
        st.metric("مؤشر BMI الخاص بك هو:", f"{bmi:.1f}")
        
        if bmi < 18.5:
            st.warning("تحتاج لزيادة الوزن بشكل صحي.")
        elif 18.5 <= bmi < 25:
            st.success("وزنك مثالي! حافظ على ذلك.")
        else:
            st.error("وزنك زائد قليلاً، ينصح باتباع حمية رياضية.")

elif menu == "🥤 سجل شرب الماء":
    st.header("🥤 تتبع استهلاكك للماء")
    
    if 'water_cups' not in st.session_state:
        st.session_state.water_cups = 0
        
    st.subheader(f"لقد شربت اليوم: {st.session_state.water_cups} أكواب")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("➕ إضافة كوب"):
            st.session_state.water_cups += 1
            st.rerun()
    with col2:
        if st.button("🔄 إعادة العداد للصفر"):
            st.session_state.water_cups = 0
            st.rerun()
            
    # شريط التقدم (الهدف 8 أكواب)
    progress = min(st.session_state.water_cups / 8, 1.0)
    st.progress(progress)

elif menu == "📸 توثيق التقدم":
    st.header("📸 سجل صور يومياتك")
    st.write("التقط صوراً لوجباتك أو للياقتك البدنية لمتابعة تقدمك.")
    picture = st.camera_input("التقط صورة الآن")
    
    if picture:
        st.image(picture, caption="تم التوثيق بنجاح! 💪")

# 4. الفوتر (أسفل الصفحة)
st.markdown("---")
st.center = st.write("© 2026 Rosie Elite Fitness App")
