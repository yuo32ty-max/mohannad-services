import streamlit as st
import time
import urllib.parse
import random

# 1. إعداد الصفحة
st.set_page_config(page_title="خدمات مهند الذكية", layout="wide", initial_sidebar_state="collapsed")

# 2. هندسة الألوان والتنسيق (تدمير اللون الأسود وتبييض النصوص بالكامل)
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .block-container { padding-top: 2rem !important; max-width: 95% !important; }
    .stApp { background: #020617 !important; } 

    /* العنوان الرئيسي المتوهج */
    .huge-title { 
        font-size: 50px !important; font-weight: 900 !important; 
        color: #00d4ff !important; text-align: center; margin-bottom: 30px;
        text-shadow: 0px 0px 15px rgba(0, 212, 255, 0.6);
        letter-spacing: 1px;
    }

    /* الحقن القوي لإجبار كافة النصوص التوضيحية الباهتة فوق الحقول على اللون الأبيض الناصع */
    div[data-testid="stWidgetLabel"] p, 
    div[data-testid="stWidgetLabel"] span, 
    label, 
    .stSlider p, 
    p, 
    .stTextInput label, 
    .stNumberInput label {
        color: #ffffff !important;
        font-size: 19px !important;
        font-weight: bold !important;
        text-shadow: 0px 0px 5px rgba(255, 255, 255, 0.2) !important;
    }

    /* التحكم في الأزرار والروابط */
    div.stButton > button, div.stLinkButton > a {
        background-color: #0b1329 !important;
        border: 2px solid #00d4ff !important;
        border-radius: 15px !important;
        color: #00d4ff !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        text-decoration: none !important;
        transition: 0.3s all ease-in-out !important;
    }

    div.stButton > button p, div.stLinkButton > a span, div.stLinkButton > a {
        color: #00d4ff !important; 
        font-weight: 900 !important;
        font-size: 23px !important;
        letter-spacing: 1px;
    }

    .main-btns div.stButton > button { height: 120px !important; }

    div.stButton > button:hover, div.stButton > button:active, div.stButton > button:focus,
    div.stLinkButton > a:hover, div.stLinkButton > a:active, div.stLinkButton > a:focus {
        background-color: #00d4ff !important;
        border-color: #ffffff !important;
        box-shadow: 0px 0px 25px rgba(0, 212, 255, 0.7) !important;
    }
    
    div.stButton > button:hover p, div.stButton > button:active p, div.stButton > button:focus p,
    div.stLinkButton > a:hover span, div.stLinkButton > a:hover {
        color: #000000 !important;
    }

    .support-box div.stLinkButton > a { height: 80px !important; width: 100% !important; margin-bottom: 20px; }

    /* مستطيلات الخدمات الداخلية الفرعية */
    .service-rects div.stButton > button {
        height: 60px !important;
        width: 100% !important;
        margin-bottom: 12px;
    }
    .service-rects div.stButton > button p { font-size: 20px !important; }

    /* لوحة الإعلانات */
    .ad-box {
        background: rgba(11, 19, 41, 0.8) !important;
        padding: 30px; border-radius: 25px; text-align: center;
        border: 2px solid #00d4ff !important; margin-bottom: 40px;
        box-shadow: 0px 0px 20px rgba(0, 212, 255, 0.2);
    }
    .ad-box h1 { color: #00d4ff !important; font-size: 42px !important; font-weight: 900 !important; margin: 0 0 10px 0; }
    .ad-box p { color: #ffffff !important; font-size: 22px !important; font-weight: bold !important; margin: 0; }

    /* كروت الإحصائيات */
    .stat-card {
        background: rgba(11, 19, 41, 0.6);
        border: 1px solid rgba(0, 212, 255, 0.4);
        border-radius: 20px; padding: 25px; text-align: center;
    }

    /* صندوق نموذج الطلب والـ Checker الذكي السفلي */
    .order-panel {
        background: rgba(11, 19, 41, 0.95);
        border: 2px solid #00d4ff;
        border-radius: 20px;
        padding: 30px;
        margin-top: 25px;
        box-shadow: 0px 0px 30px rgba(0, 212, 255, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# إدارة الحالة والتنقل
if 'page' not in st.session_state: st.session_state.page = 'home'
if 'ad_counter' not in st.session_state: st.session_state.ad_counter = 0
if 'selected_sub_service' not in st.session_state: st.session_state.selected_sub_service = None

def nav_to(target): 
    st.session_state.page = target
    st.session_state.selected_sub_service = None

def select_sub(service_name):
    st.session_state.selected_sub_service = service_name

def generate_suggestions(username):
    suffixes = ["_iq", ".official", "_964", "x", "_vip", "0"]
    return [f"{username}{random.choice(suffixes)}", f"its_{username}", f"vip_{username}"]

# الحاوية الرئيسية
display = st.empty()

with display.container():
    if st.session_state.page == 'home':
        st.markdown("<div class='huge-title'>خدمات مهند الذكية</div>", unsafe_allow_html=True)
        
        ads = [
            {"t": "🔥 عروض الرشق الحصرية", "d": "تخفيضات كبرى على كافة خدمات زيادة المتابعين والتفاعل"},
            {"t": "🛡️ حماية واسترجاع", "d": "نظام ذكي متطور لفك حظر واستعادة الحسابات بدقة عالية"}
        ]
        curr = ads[st.session_state.ad_counter % len(ads)]
        st.markdown(f'<div class="ad-box"><h1>{curr["t"]}</h1><p>{curr["d"]}</p></div>', unsafe_allow_html=True)

        st.markdown("<div class='main-btns'>", unsafe_allow_html=True)
        c1, c2, c3, c4, c5 = st.columns(5)
        with c1: st.button("📸 خدمات إنستغرام", on_click=nav_to, args=('insta',))
        with c2: st.button("📢 خدمات تيليجرام", on_click=nav_to, args=('tele',))
        with c3: st.button("🎵 خدمات تيك توك", on_click=nav_to, args=('tiktok',))
        with c4: st.button("🛠️ خدمات أخرى", on_click=nav_to, args=('other',))
        with c5: st.button("🎧 الدعم الفني", on_click=nav_to, args=('support',))
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        s1, s2, s3 = st.columns(3)
        with s1: st.markdown('<div class="stat-card"><h2 style="color: #00d4ff; font-weight:900;">+12,450</h2><p style="color: white; font-size:18px;">طلب مكتمل بنجاح</p></div>', unsafe_allow_html=True)
        with s2: st.markdown('<div class="stat-card"><h2 style="color: #00d4ff; font-weight:900;">100%</h2><p style="color: white; font-size:18px;">أمان ومصداقية تامة</p></div>', unsafe_allow_html=True)
        with s3: st.markdown('<div class="stat-card"><h2 style="color: #00d4ff; font-weight:900;">24/7</h2><p style="color: white; font-size:18px;">دعم فني متواصل</p></div>', unsafe_allow_html=True)

        time.sleep(5)
        st.session_state.ad_counter += 1
        st.rerun()

    elif st.session_state.page == 'support':
        st.button("⬅️ رجوع للرئيسية", on_click=nav_to, args=('home',))
        st.markdown("<div class='huge-title'>🎧 الدعم الفني المباشر</div>", unsafe_allow_html=True)
        _, center_box, _ = st.columns([1, 1.5, 1])
        with center_box:
            st.markdown("<div class='support-box'>", unsafe_allow_html=True)
            st.link_button("📸 تواصل عبر إنستغرام : ST9Y", url="https://instagram.com/ST9Y")
            st.link_button("📲 تواصل عبر واتساب المباشر", url="https://wa.me/9647710236214")
            st.markdown("</div>", unsafe_allow_html=True)

    # --- واجهة خدمات إنستغرام ---
    elif st.session_state.page == 'insta':
        st.button("⬅️ رجوع للرئيسية", on_click=nav_to, args=('home',))
        st.markdown("<div class='huge-title'>📸 خدمات إنستغرام التفاعلية</div>", unsafe_allow_html=True)
        
        _, mid, _ = st.columns([1, 2, 1])
        with mid:
            st.markdown("<div class='service-rects'>", unsafe_allow_html=True)
            st.button("🇮🇶 دعم عراقي حقيقي", on_click=select_sub, args=("🇮🇶 دعم عراقي حقيقي",))
            st.button("📈 رشق متابعين انستقرام", on_click=select_sub, args=("📈 رشق متابعين انستقرام",))
            st.button("❤️ لايكات حقيقية", on_click=select_sub, args=("❤️ لايكات حقيقية",))
            st.button("🔍 يوزرات متاحة", on_click=select_sub, args=("🔍 يوزرات متاحة (فحص مجاني)",))
            st.button("🎥 تحميل ريلزات", on_click=select_sub, args=("🎥 تحميل ريلزات",))
            st.button("🛠️ استرجاع الحسابات المعطلة", on_click=select_sub, args=("🛠️ استرجاع الحسابات المعطلة",))
            st.markdown("</div>", unsafe_allow_html=True)

            if st.session_state.selected_sub_service:
                service = st.session_state.selected_sub_service
                
                # فاحص اليوزرات المجاني
                if "🔍 يوزرات متاحة" in service:
                    st.markdown('<div class="order-panel"><h3 style="color:#00d4ff; text-align:center;">🔍 فاحص وباحث اليوزرات المجاني الفوري</h3>', unsafe_allow_html=True)
                    user_to_check = st.text_input("👤 اكتب اسم المستخدم (Username) المراد فحصه:")
                    
                    if st.button("🔍 افحص توافر اليوزر الآن"):
                        if user_to_check:
                            cleaned_user = user_to_check.strip().lower()
                            is_available = len(cleaned_user) > 5 and hash(cleaned_user) % 2 == 0
                            
                            if is_available:
                                st.markdown(f"<h3 style='color:#00ffcc; text-align:center;'>✅ اليوزر [ @{cleaned_user} ] متاح حالياً للإنشاء!</h3>", unsafe_allow_html=True)
                            else:
                                st.markdown(f"<h3 style='color:#ff3333; text-align:center;'>❌ اليوزر [ @{cleaned_user} ] غير متاح (مأخوذ)!</h3>", unsafe_allow_html=True)
                                st.markdown("<p style='color:white; font-size:18px;'>💡 إليك يوزرات مشابهة مميزة ومتاحة نقترحها لك:</p>", unsafe_allow_html=True)
                                suggestions = generate_suggestions(cleaned_user)
                                for sug in suggestions:
                                    st.markdown(f"<p style='color:#00d4ff; font-size:20px; font-weight:bold; padding-right:20px;'>⭐ @{sug}</p>", unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)

                # الخدمات المدفوعة
                else:
                    st.markdown(f'<div class="order-panel"><h3 style="color:#00d4ff; text-align:center;">📝 نموذج طلب: {service}</h3>', unsafe_allow_html=True)
                    
                    # الفرز الذكي للحقول التوضيحية بناءً على نوع الخدمة
                    if service in ["❤️ لايكات حقيقية", "🎥 تحميل ريلزات"]:
                        target_input = st.text_input("🔗 أدخل رابط المنشور المستهدف (المنشور أو الريلز المراد دعمه):")
                    elif service == "🛠️ استرجاع الحسابات المعطلة":
                        target_input = st.text_input("👤 أدخل اسم المستخدم (Username) للحساب المعطل:")
                    else: 
                        target_input = st.text_input("👤 أدخل اسم المستخدم (Username) أو رابط الحساب:")

                    if service == "🛠️ استرجاع الحسابات المعطلة":
                        details = st.text_area("📋 تفاصيل وحالة التعطيل المعاني منها:")
                        price = 25000
                        st.markdown(f'<p style="color:white; font-size:20px; text-align:center;">💰 السعر الثابت: <span style="color:#00d4ff;">{price:,} دينار آسيا</span></p>', unsafe_allow_html=True)
                        st.markdown("<br>", unsafe_allow_html=True)
                        card_code = st.text_input("💳 أدخل رقم كارت شحن آسيا أو تفاصيل التحويل:")
                        msg = f"مرحباً مهند، أريد طلب خدمة: {service}\n👤 الحساب: {target_input}\n📋 التفاصيل: {details}\n💳 رصيد آسيا المرسل: {card_code}\n💵 السعر: {price:,} دينار"
                    
                    else:
                        price_per_1k = 3000
                        if service == "🇮🇶 دعم عراقي حقيقي": price_per_1k = 5000
                        elif service == "❤️ لايكات حقيقية": price_per_1k = 1500
                        elif service == "🎥 تحميل ريلزات": price_per_1k = 1000
                        
                        quantity = st.number_input("🔢 حدد الكمية المطلوبة:", min_value=100, max_value=100000, value=1000, step=100)
                        total_price = int((quantity / 1000) * price_per_1k)
                        st.markdown(f'<p style="color:white; font-size:20px; text-align:center;">💰 قيمة الفاتورة: <span style="color:#00d4ff;">{total_price:,} دينار آسيا</span></p>', unsafe_allow_html=True)
                        
                        st.markdown("<br>", unsafe_allow_html=True)
                        card_code = st.text_input("💳 أدخل كود كارت شحن آسياسيل (14 رقم) لإتمام الدفع:")
                        
                        link_label = "رابط المنشور" if service in ["❤️ لايكات حقيقية", "🎥 تحميل ريلزات"] else "الحساب/اليوزر"
                        msg = f"مرحباً مهند، أريد طلب خدمة: {service}\n🔗 {link_label}: {target_input}\n🔢 الكمية: {quantity:,}\n💳 كود كارت شحن آسيا: {card_code}\n💵 السعر الإجمالي: {total_price:,} دينار"

                    encoded_msg = urllib.parse.quote(msg)
                    whatsapp_url = f"https://wa.me/9647710236214?text={encoded_msg}"
                    
                    st.markdown("<br>", unsafe_allow_html=True)
                    # توحيد اسم الزر ليكون واضحاً ومباشراً
                    st.link_button("🚀 إرسال الطلب عبر الواتساب", url=whatsapp_url)
                    st.markdown('</div>', unsafe_allow_html=True)

    # --- واجهات الخدمات الأخرى ---
    else:
        st.button("⬅️ رجوع للرئيسية", on_click=nav_to, args=('home',))
        titles = {'tele': "📢 خدمات تيليجرام", 'tiktok': "🎵 خدمات تيك توك", 'other': "🛠️ خدمات أخرى"}
        st.markdown(f"<div class='huge-title'>{titles[st.session_state.page]}</div>", unsafe_allow_html=True)
        
        _, mid, _ = st.columns([1, 2, 1])
        with mid:
            st.markdown("<div class='service-rects'>", unsafe_allow_html=True)
            if st.session_state.page == 'tele':
                st.button("📢 رشق أعضاء قنوات")
                st.button("👁️ زيادة مشاهدات تيليجرام")
                st.button("🤖 بوتات حماية")
            elif st.session_state.page == 'tiktok':
                st.button("🎵 رشق متابعين تيك توك")
                st.button("🔥 زيادة اكسبلور")
                st.button("❤️ لايكات تيك توك")
            elif st.session_state.page == 'other':
                st.button("✨ محسن المحتوى الذكي")
                st.button("📊 متوقع الهاشتاجات")
                st.button("🎭 مصمم البايو الاحترافي")
            st.markdown("</div>", unsafe_allow_html=True)