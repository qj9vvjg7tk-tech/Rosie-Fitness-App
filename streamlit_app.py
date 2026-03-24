with col_stats:
        st.header("🥤 مراقب السوائل")
        st.metric("أكواب الماء", f"{st.session_state.water_cups} / 12")
        if st.button("➕ إضافة كوب ماء"):
            st.session_state.water_cups += 1
            st.rerun()
        
        st.write("---")
        # رسم بياني للنشاط (Gauge Chart)
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = st.session_state.water_cups,
            gauge = {'axis': {'range': [None, 12]}, 'bar': {'color': "#00d2ff"}},
            title = {'text': "معدل شرب الماء اليوم"}
        ))
        st.plotly_chart(fig, use_container_width=True)

elif menu == "📊 محلل الجسم والماكروز":
    st.header("📊 التحليل الذكي للكتلة والتغذية")
    c1, c2 = st.columns(2)
    with c1:
        w = st.number_input("الوزن الحالي (كجم):", value=70.0)
        h = st.number_input("الطول الحالي (سم):", value=170.0)
    with c2:
        age = st.number_input("العمر:", value=19)
        goal = st.selectbox("هدفك النهائي:", ["خسارة وزن (تنشيف)", "بناء عضل (تضخيم)", "محافظة"])
    
    if st.button("تحليل البيانات الآن"):
        # حساب BMI
        height_m = h / 100
        bmi = w / (height_m ** 2)
        st.subheader(f"مؤشر كتلة جسمك (BMI): {bmi:.1f}")
        
        if bmi < 18.5: st.warning("الحالة: وزن تحت الطبيعي - ننصح بزيادة السعرات.")
        elif 18.5 <= bmi < 25: st.success("الحالة: وزن مثالي! استمر على هذا النهج.")
        else: st.error("الحالة: زيادة في الوزن - ننصح بنظام غذائي وكارديو.")
        
        st.write("---")
        st.subheader("توزيع العناصر الغذائية المقترح (Macros)")
        dist = {"خسارة وزن (تنشيف)": [40, 30, 30], "بناء عضل (تضخيم)": [30, 50, 20], "محافظة": [30, 40, 30]}
        labels = ['بروتين', 'كارب', 'دهون']
        fig = go.Figure(data=[go.Pie(labels=labels, values=dist[goal], hole=.4)])
        st.plotly_chart(fig)

elif menu == "🤖 مستشار الـ AI":
    st.header("🤖 مستشار الروز الذكي (AI Reports)")
    st.info("قم بلصق أي تقرير من ChatGPT وسأقوم باستخراج الفيديوهات لك تلقائياً!")
    ai_text = st.text_area("ضع الخطة المكتوبة هنا:", height=200)
    
    if ai_text:
        st.markdown("<div class='report-box'>", unsafe_allow_html=True)
        st.markdown(ai_text)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # استخراج روابط يوتيوب
        links = re.findall(r'(https?://[^\s]+)', ai_text)
        found_yt = [l for l in links if "youtube" in l or "youtu.be" in l]
        
        if found_yt:
            st.subheader("🎥 الفيديوهات المكتشفة في النص:")
            for link in found_yt:
                st.video(link)

elif menu == "📸 التقدم والكاميرا":
    st.header("📸 سجل التقدم البصري")
    st.warning("ملاحظة لمستخدمي iPad: الكاميرا الافتراضية قد تفتح الجهة الأمامية، يرجى تدوير الجهاز إذا لزم الأمر.")
    cam_photo = st.camera_input("التقطي صورة لوجبتك أو لتقدم جسمك اليوم")
    if cam_photo:
        st.image(cam_photo, caption="تم التوثيق بنجاح! 🌟")

# --- 5. الفوتر (Footer) ---
st.markdown("<br><hr><center>Rosie Elite Fitness v2.0 | 2026 | Powered by iPad M3 Performance</center>", unsafe_allow_html=True)
