import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import re
import random

# --- 1. الإعدادات الأساسية ---
st.set_page_config(page_title="Rosie Elite 2026", layout="wide")

# --- 2. القائمة الجانبية ---
with st.sidebar:
    st.title("💎 Rosie Elite")
    menu = st.radio("القائمة:", ["🏠 الركن الرياضي", "📊 الماكروز", "🤖 مستشار AI", "📸 الكاميرا"])

# --- 3. إدارة البيانات ---
if 'water' not in st.session_state: st.session_state.water = 0

# --- 4. الصفحات ---
if menu == "🏠 الركن الرياضي":
    st.header("📅 تمارين اليوم")
    day = st.selectbox("اختر اليوم:", ["السبت", "الأحد", "الاثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة"])
    st.write(f"تمارين يوم {day} جاهزة لك!")
    
    st.subheader("🥤 عداد الماء")
    st.write(f"الأكواب: {st.session_state.water}")
    if st.button("اضافة كوب"):
        st.session_state.water += 1
        st.rerun()

elif menu == "📊 الماكروز":
    st.header("📊 حاسبة الجسم")
    w = st.number_input("الوزن (كجم):", value=70.0)
    h = st.number_input("الطول (سم):", value=170.0)
    if st.button("احسب"):
        bmi = w / ((h/100)**2)
        st.success(f"مؤشر كتلة جسمك هو: {bmi:.1f}")

elif menu == "🤖 مستشار AI":
    st.header("🤖 تحليل الروابط")
    txt = st.text_area("ضع نص الخطة هنا:")
    if txt:
        links = re.findall(r'(https?://[^\s]+)', txt)
        for l in links: st.video(l)

elif menu == "📸 الكاميرا":
    st.header("📸 التوثيق")
    st.camera_input("التقط صورة")

st.write("---")
st.caption("Rosie Fitness 2026 | Powered by iPad M3")
