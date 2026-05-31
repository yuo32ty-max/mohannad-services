import streamlit as st
import time
import urllib.parse
import random

# 1. إعداد الصفحة
st.set_page_config(page_title="خدمات مهند الذكية", layout="wide", initial_sidebar_state="expanded")

# 2. هندسة الألوان والتنسيق (تدمير اللون الأسود وتبييض النصوص بالكامل)
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .block-container { padding-top: 2rem !important; max-width: 95% !important;}
    .stApp { background: #020617 !important; }
    
    /* العنوان الرئيسي المتوهج */
    .huge-title {
        font-size: 50px !important; font-weight: 900 !important;
        color: #00d4ff !important; text-align: center; margin-bottom: 30px;
        text-shadow: 0px 0px 15px rgba(0, 212, 255, 0.6);
        letter-spacing: 1px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. واجهة التطبيق الرئيسية
st.markdown('<h1 class="huge-title">خدمات مهند الذكية</h1>', unsafe_allow_html=True)

st.markdown("""
    <div style="background-color: #0b1528; border: 2px solid #00d4ff; padding: 25px; border-radius: 15px; text-align: center; margin-bottom: 30px; box-shadow: 0px 4px 20px rgba(0,212,255,0.2);">
        <h2 style="color: #00d4ff; font-size: 32px; margin-bottom: 10px;">🔥 عروض الرشق الحصرية</h2>
        <p style="color: #ffffff; font-size: 18px;">تخفيضات كبرى على كافة خدمات زيادة المتابعين والتفاعل</p>
    </div>
""", unsafe_allow_html=True)

# أزرار الأقسام والخدمات
col1, col2, col3, col4, col5 = st.columns(5)

with col5:
    st.button("🎧 الدعم الفني", use_container_width=True)
with col4:
    st.button("🛠️ خدمات أخرى", use_container_width=True)
with col3:
    st.button("🎵 خدمات تيك توك", use_container_width=True)
with col2:
    st.button("📢 خدمات تيليجرام", use_container_width=True)
with col1:
    st.button("📸 خدمات إنستغرام", use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# الإحصائيات بالأسفل
stat1, stat2, stat3 = st.columns(3)

with stat3:
    st.markdown("""
        <div style="background-color: #0b1528; border: 1px solid #1e293b; padding: 20px; border-radius: 12px; text-align: center;">
            <h3 style="color: #00d4ff; font-size: 28px; margin-bottom: 5px;">24/7</h3>
            <p style="color: #94a3b8; font-size: 16px;">دعم فني متواصل</p>
        </div>
    """, unsafe_allow_html=True)

with stat2:
    st.markdown("""
        <div style="background-color: #0b1528; border: 1px solid #1e293b; padding: 20px; border-radius: 12px; text-align: center;">
            <h3 style="color: #00d4ff; font-size: 28px; margin-bottom: 5px;">100%</h3>
            <p style="color: #94a3b8; font-size: 16px;">أمان ومصداقية تامة</p>
        </div>
    """, unsafe_allow_html=True)

with stat1:
    st.markdown("""
        <div style="background-color: #0b1528; border: 1px solid #1e293b; padding: 20px; border-radius: 12px; text-align: center;">
            <h3 style="color: #00d4ff; font-size: 28px; margin-bottom: 5px;">+12,450</h3>
            <p style="color: #94a3b8; font-size: 16px;">طلب مكتمل بنجاح</p>
        </div>
    """, unsafe_allow_html=True)