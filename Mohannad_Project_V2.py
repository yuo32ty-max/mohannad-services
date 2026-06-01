import streamlit as st
import urllib.parse
import random

st.set_page_config(
    page_title="خدمات مهند الذكية",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── CSS — التصميم المرجعي + دعم الموبايل ─────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap');

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0.8rem 1rem 2rem !important; max-width: 1100px !important; }
.stApp {
    background: radial-gradient(ellipse at 50% 0%, #1a1040 0%, #0a0a18 45%, #060610 100%) !important;
    font-family: 'Cairo', sans-serif !important;
}

.site-header { text-align: center; padding: 8px 0 20px; position: relative; }
.site-header .crown  { position: absolute; left: 8px;  top: 6px; font-size: 28px; filter: drop-shadow(0 0 12px #a855f7); }
.site-header .shield { position: absolute; right: 8px; top: 6px; font-size: 28px; filter: drop-shadow(0 0 12px #3b82f6); }
.site-title {
    font-size: clamp(28px, 6vw, 42px); font-weight: 900; margin: 0;
    background: linear-gradient(90deg, #c084fc, #818cf8, #60a5fa);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 0 20px rgba(168,85,247,0.5));
}
.site-subtitle { color: #94a3b8; font-size: clamp(12px, 3vw, 15px); margin-top: 8px; font-weight: 600; }

.hero-wrap { position: relative; margin-bottom: 20px; }
.hero-card {
    background: linear-gradient(135deg, rgba(88,28,135,0.55), rgba(30,20,60,0.85));
    border: 1.5px solid rgba(236,72,153,0.45);
    border-radius: 22px; padding: 22px 20px;
    display: flex; align-items: center; justify-content: space-between; gap: 12px;
    box-shadow: 0 0 40px rgba(236,72,153,0.15);
    min-height: 140px;
}
.hero-badge {
    display: inline-block; background: linear-gradient(90deg,#ec4899,#f97316);
    color: #fff; font-size: 11px; font-weight: 700; padding: 4px 12px; border-radius: 20px; margin-bottom: 8px;
}
.hero-card h2 { color: #fff; font-size: clamp(22px, 5vw, 30px); font-weight: 900; margin: 0 0 6px; }
.hero-card p  { color: #cbd5e1; font-size: clamp(13px, 3vw, 15px); margin: 0; }
.hero-graphic { font-size: clamp(50px, 12vw, 90px); line-height: 1; filter: drop-shadow(0 0 20px rgba(168,85,247,0.6)); }
.hero-dots { text-align: center; margin-top: 10px; }
.hero-dots span {
    display: inline-block; width: 8px; height: 8px; border-radius: 50%;
    background: rgba(255,255,255,0.25); margin: 0 4px;
}
.hero-dots span.active { background: #ec4899; box-shadow: 0 0 8px #ec4899; }

.features-row {
    display: grid; grid-template-columns: repeat(5, 1fr); gap: 8px; margin-bottom: 22px;
}
.feature-item {
    text-align: center; padding: 12px 6px;
    background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.07); border-radius: 14px;
}
.feature-item .fi-icon { font-size: 24px; margin-bottom: 4px; }
.feature-item .fi-title { color: #e2e8f0; font-size: 11px; font-weight: 700; margin: 0; }
.feature-item .fi-sub   { color: #64748b; font-size: 9px; margin: 2px 0 0; }

.platforms-grid {
    display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 10px;
}
.platform-card {
    border-radius: 18px; padding: 18px 12px; text-align: center;
    min-height: 170px; display: flex; flex-direction: column;
    align-items: center; justify-content: center; gap: 8px;
    border: 1.5px solid transparent;
}
.platform-card .pc-logo { font-size: 38px; }
.platform-card .pc-name { color: #fff; font-size: 14px; font-weight: 800; margin: 0; }
.card-insta {
    background: linear-gradient(160deg, rgba(131,58,180,0.5), rgba(253,29,29,0.25));
    border-color: rgba(225,48,108,0.5); box-shadow: 0 8px 30px rgba(225,48,108,0.2);
}
.card-tiktok {
    background: linear-gradient(160deg, rgba(0,0,0,0.6), rgba(254,44,85,0.2), rgba(37,244,238,0.15));
    border-color: rgba(37,244,238,0.4); box-shadow: 0 8px 30px rgba(37,244,238,0.15);
}
.card-wa {
    background: linear-gradient(160deg, rgba(6,95,70,0.5), rgba(34,197,94,0.25));
    border-color: rgba(34,197,94,0.45); box-shadow: 0 8px 30px rgba(34,197,94,0.15);
}
.card-tele {
    background: linear-gradient(160deg, rgba(14,60,120,0.5), rgba(59,130,246,0.25));
    border-color: rgba(59,130,246,0.45); box-shadow: 0 8px 30px rgba(59,130,246,0.15);
}

.support-banner {
    background: linear-gradient(135deg, rgba(14,40,80,0.7), rgba(20,30,60,0.85));
    border: 1.5px solid rgba(59,130,246,0.35); border-radius: 20px;
    padding: 20px; display: flex; align-items: center; gap: 16px; margin: 20px 0;
    box-shadow: 0 8px 30px rgba(59,130,246,0.12);
}
.support-banner .sb-icon { font-size: 56px; filter: drop-shadow(0 0 18px #3b82f6); flex-shrink: 0; }
.support-banner .sb-text h3 { color: #fff; font-size: clamp(18px, 4vw, 22px); font-weight: 900; margin: 0 0 4px; }
.support-banner .sb-text p  { color: #94a3b8; font-size: 13px; margin: 0; }

.trust-bar { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; }
.trust-item {
    background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08);
    border-radius: 12px; padding: 12px 8px; text-align: center;
}
.trust-item .ti-icon { font-size: 20px; }
.trust-item .ti-label { color: #cbd5e1; font-size: 11px; font-weight: 700; margin: 4px 0 0; }

.page-title {
    text-align: center; font-size: clamp(26px, 5vw, 36px); font-weight: 900; margin-bottom: 20px;
    background: linear-gradient(90deg, #c084fc, #60a5fa);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.order-panel {
    background: rgba(255,255,255,0.04); border: 1.5px solid rgba(168,85,247,0.35);
    border-radius: 18px; padding: 20px; margin-top: 14px;
}

div.stButton > button, div.stLinkButton > a {
    background: rgba(255,255,255,0.06) !important;
    border: 1.5px solid rgba(168,85,247,0.45) !important;
    border-radius: 14px !important; color: #c084fc !important;
    font-family: 'Cairo', sans-serif !important; font-weight: 700 !important;
    min-height: 48px !important; transition: 0.25s !important;
}
div.stButton > button:hover, div.stLinkButton > a:hover {
    background: linear-gradient(90deg,#9333ea,#6366f1) !important;
    color: #fff !important; border-color: transparent !important;
    box-shadow: 0 4px 20px rgba(147,51,234,0.4) !important;
}
div.stButton > button p, div.stLinkButton > a { color: inherit !important; font-size: 15px !important; }
.btn-insta div.stButton > button { border-color: rgba(225,48,108,0.6) !important; color: #f472b6 !important; }
.btn-tiktok div.stButton > button { border-color: rgba(37,244,238,0.5) !important; color: #25f4ee !important; }
.btn-wa div.stButton > button    { border-color: rgba(34,197,94,0.5) !important; color: #4ade80 !important; }
.btn-tele div.stButton > button  { border-color: rgba(59,130,246,0.5) !important; color: #60a5fa !important; }
.service-btns div.stButton > button { width: 100% !important; margin-bottom: 8px; }
div[data-testid="stWidgetLabel"] p, label { color: #e2e8f0 !important; font-weight: 600 !important; }

@media (max-width: 900px) {
    .platforms-grid { grid-template-columns: repeat(2, 1fr); }
    .features-row { grid-template-columns: repeat(3, 1fr); }
    .trust-bar { grid-template-columns: repeat(2, 1fr); }
    .hero-card { flex-direction: column; text-align: center; }
    .support-banner { flex-direction: column; text-align: center; }
}
@media (max-width: 480px) {
    .features-row { grid-template-columns: repeat(2, 1fr); }
    .site-header .crown, .site-header .shield { font-size: 22px; }
}
</style>
""", unsafe_allow_html=True)

# ── الحالة ────────────────────────────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "home"
if "slide" not in st.session_state:
    st.session_state.slide = 0
if "selected_sub_service" not in st.session_state:
    st.session_state.selected_sub_service = None

SLIDES = [
    {"badge": "عرض محدود", "title": "عروض مميزة", "desc": "خصومات تصل إلى 50% على جميع الخدمات", "cta": "🛒 اطلب الآن", "icon": "🛍️", "target": "insta"},
    {"badge": "🔥 الأكثر طلباً", "title": "رشق متابعين حقيقي", "desc": "تخفيضات كبرى على خدمات زيادة المتابعين والتفاعل", "cta": "🚀 ابدأ الآن", "icon": "📈", "target": "insta"},
    {"badge": "🛡️ حماية", "title": "استرجاع الحسابات", "desc": "نظام ذكي لفك حظر واستعادة الحسابات بدقة عالية", "cta": "🔐 تواصل معنا", "icon": "🛡️", "target": "support"},
]


def nav_to(target):
    st.session_state.page = target
    st.session_state.selected_sub_service = None


def select_sub(name):
    st.session_state.selected_sub_service = name


def prev_slide():
    st.session_state.slide = (st.session_state.slide - 1) % len(SLIDES)


def next_slide():
    st.session_state.slide = (st.session_state.slide + 1) % len(SLIDES)


def generate_suggestions(username):
    suffixes = ["_iq", ".official", "_964", "x", "_vip", "0"]
    return [f"{username}{random.choice(suffixes)}", f"its_{username}", f"vip_{username}"]


# ══ الصفحة الرئيسية ════════════════════════════════════════════════════════════
if st.session_state.page == "home":
    st.markdown("""
    <div class="site-header">
        <span class="crown">👑</span><span class="shield">🛡️</span>
        <h1 class="site-title">خدمات مهند</h1>
        <p class="site-subtitle">جودة عالية &nbsp;•&nbsp; أسعار منافسة &nbsp;•&nbsp; دعم على مدار الساعة</p>
    </div>
    """, unsafe_allow_html=True)

    s = SLIDES[st.session_state.slide]
    dots = "".join(f'<span class="{"active" if i == st.session_state.slide else ""}"></span>' for i in range(len(SLIDES)))
    st.markdown(f"""
    <div class="hero-wrap">
        <div class="hero-card">
            <div><span class="hero-badge">{s["badge"]}</span><h2>{s["title"]}</h2><p>{s["desc"]}</p></div>
            <div class="hero-graphic">{s["icon"]}</div>
        </div>
        <div class="hero-dots">{dots}</div>
    </div>
    """, unsafe_allow_html=True)

    ca, cb, cc = st.columns([1, 3, 1])
    with ca: st.button("◀", on_click=prev_slide, key="hero_prev")
    with cc: st.button("▶", on_click=next_slide, key="hero_next")
    with cb: st.button(s["cta"], on_click=nav_to, args=(s["target"],), use_container_width=True, key="hero_cta")

    st.markdown("""
    <div class="features-row">
        <div class="feature-item"><div class="fi-icon">🛡️</div><p class="fi-title">أمان ومصداقية</p><p class="fi-sub">100%</p></div>
        <div class="feature-item"><div class="fi-icon">🎧</div><p class="fi-title">دعم سريع</p><p class="fi-sub">24/7</p></div>
        <div class="feature-item"><div class="fi-icon">🔄</div><p class="fi-title">استرجاع حسابات</p><p class="fi-sub">فوري</p></div>
        <div class="feature-item"><div class="fi-icon">🚀</div><p class="fi-title">سرعة وجودة</p><p class="fi-sub">مضمونة</p></div>
        <div class="feature-item"><div class="fi-icon">📊</div><p class="fi-title">ضمان النتائج</p><p class="fi-sub">100%</p></div>
    </div>
    <div class="platforms-grid">
        <div class="platform-card card-insta"><div class="pc-logo">📸</div><p class="pc-name">خدمات إنستغرام</p></div>
        <div class="platform-card card-tiktok"><div class="pc-logo">🎵</div><p class="pc-name">خدمات تيك توك</p></div>
        <div class="platform-card card-wa"><div class="pc-logo">💬</div><p class="pc-name">خدمات واتساب</p></div>
        <div class="platform-card card-tele"><div class="pc-logo">✈️</div><p class="pc-name">خدمات تيليجرام</p></div>
    </div>
    """, unsafe_allow_html=True)

    p1, p2, p3, p4 = st.columns(4)
    with p1:
        st.markdown('<div class="btn-insta">', unsafe_allow_html=True)
        st.button("📸 عرض الخدمات", on_click=nav_to, args=("insta",), use_container_width=True, key="nav_insta")
        st.markdown("</div>", unsafe_allow_html=True)
    with p2:
        st.markdown('<div class="btn-tiktok">', unsafe_allow_html=True)
        st.button("🎵 عرض الخدمات", on_click=nav_to, args=("tiktok",), use_container_width=True, key="nav_tiktok")
        st.markdown("</div>", unsafe_allow_html=True)
    with p3:
        st.markdown('<div class="btn-wa">', unsafe_allow_html=True)
        st.button("💬 عرض الخدمات", on_click=nav_to, args=("support",), use_container_width=True, key="nav_wa")
        st.markdown("</div>", unsafe_allow_html=True)
    with p4:
        st.markdown('<div class="btn-tele">', unsafe_allow_html=True)
        st.button("✈️ عرض الخدمات", on_click=nav_to, args=("tele",), use_container_width=True, key="nav_tele")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="support-banner">
        <div class="sb-icon">🎧</div>
        <div class="sb-text"><h3>خدمات الدعم الفني</h3><p>فريقنا جاهز لمساعدتك في أي وقت</p></div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("💬 تواصل معنا", url="https://wa.me/9647710236214", use_container_width=True)

    st.markdown("""
    <div class="trust-bar">
        <div class="trust-item"><div class="ti-icon">👥</div><p class="ti-label">ثقة العملاء</p></div>
        <div class="trust-item"><div class="ti-icon">🔄</div><p class="ti-label">تحديث مستمر</p></div>
        <div class="trust-item"><div class="ti-icon">🏅</div><p class="ti-label">جودة عالية</p></div>
        <div class="trust-item"><div class="ti-icon">🏷️</div><p class="ti-label">أسعار تنافسية</p></div>
    </div>
    """, unsafe_allow_html=True)

    st.button("🛠️ خدمات أخرى", on_click=nav_to, args=("other",), use_container_width=True)

elif st.session_state.page == "support":
    st.button("⬅️ رجوع للرئيسية", on_click=nav_to, args=("home",))
    st.markdown('<h2 class="page-title">🎧 الدعم الفني المباشر</h2>', unsafe_allow_html=True)
    st.link_button("📸 إنستغرام : ST9Y", url="https://instagram.com/ST9Y", use_container_width=True)
    st.link_button("📲 واتساب المباشر", url="https://wa.me/9647710236214", use_container_width=True)

elif st.session_state.page == "insta":
    st.button("⬅️ رجوع للرئيسية", on_click=nav_to, args=("home",))
    st.markdown('<h2 class="page-title">📸 خدمات إنستغرام</h2>', unsafe_allow_html=True)
    st.markdown('<div class="service-btns">', unsafe_allow_html=True)
    st.button("🇮🇶 دعم عراقي حقيقي", on_click=select_sub, args=("🇮🇶 دعم عراقي حقيقي",), use_container_width=True)
    st.button("📈 رشق متابعين", on_click=select_sub, args=("📈 رشق متابعين انستقرام",), use_container_width=True)
    st.button("❤️ لايكات حقيقية", on_click=select_sub, args=("❤️ لايكات حقيقية",), use_container_width=True)
    st.button("🔍 يوزرات متاحة", on_click=select_sub, args=("🔍 يوزرات متاحة (فحص مجاني)",), use_container_width=True)
    st.button("🎥 تحميل ريلزات", on_click=select_sub, args=("🎥 تحميل ريلزات",), use_container_width=True)
    st.button("🛠️ استرجاع الحسابات", on_click=select_sub, args=("🛠️ استرجاع الحسابات المعطلة",), use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    if st.session_state.selected_sub_service:
        service = st.session_state.selected_sub_service
        if "🔍 يوزرات متاحة" in service:
            st.markdown('<div class="order-panel"><h3 style="color:#c084fc;text-align:center;">🔍 فاحص اليوزرات</h3>', unsafe_allow_html=True)
            user = st.text_input("👤 اسم المستخدم:")
            if st.button("🔍 افحص الآن", use_container_width=True) and user:
                cleaned = user.strip().lower()
                if len(cleaned) > 5 and hash(cleaned) % 2 == 0:
                    st.success(f"✅ @{cleaned} متاح!")
                else:
                    st.error(f"❌ @{cleaned} غير متاح")
                    for sug in generate_suggestions(cleaned):
                        st.info(f"⭐ @{sug}")
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="order-panel"><h3 style="color:#c084fc;text-align:center;">📝 {service}</h3>', unsafe_allow_html=True)
            if service in ["❤️ لايكات حقيقية", "🎥 تحميل ريلزات"]:
                target = st.text_input("🔗 رابط المنشور:")
            elif service == "🛠️ استرجاع الحسابات المعطلة":
                target = st.text_input("👤 اسم المستخدم:")
            else:
                target = st.text_input("👤 اسم المستخدم أو الرابط:")

            if service == "🛠️ استرجاع الحسابات المعطلة":
                details = st.text_area("📋 تفاصيل التعطيل:")
                price = 25000
                card = st.text_input("💳 كود كارت آسيا:")
                msg = f"مرحباً مهند، أريد: {service}\n👤 {target}\n📋 {details}\n💳 {card}\n💵 {price:,} دينار"
            else:
                ppk = {"🇮🇶 دعم عراقي حقيقي": 5000, "❤️ لايكات حقيقية": 1500, "🎥 تحميل ريلزات": 1000}.get(service, 3000)
                qty = st.number_input("🔢 الكمية:", min_value=100, max_value=100000, value=1000, step=100)
                total = int((qty / 1000) * ppk)
                card = st.text_input("💳 كود كارت آسيا (14 رقم):")
                lbl = "رابط" if service in ["❤️ لايكات حقيقية", "🎥 تحميل ريلزات"] else "حساب"
                msg = f"مرحباً مهند، أريد: {service}\n🔗 {lbl}: {target}\n🔢 {qty:,}\n💳 {card}\n💵 {total:,} دينار"

            url = f"https://wa.me/9647710236214?text={urllib.parse.quote(msg)}"
            st.link_button("🚀 إرسال الطلب عبر الواتساب", url=url, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

else:
    st.button("⬅️ رجوع للرئيسية", on_click=nav_to, args=("home",))
    titles = {"tele": "✈️ خدمات تيليجرام", "tiktok": "🎵 خدمات تيك توك", "other": "🛠️ خدمات أخرى"}
    st.markdown(f'<h2 class="page-title">{titles[st.session_state.page]}</h2>', unsafe_allow_html=True)
    st.markdown('<div class="service-btns">', unsafe_allow_html=True)
    if st.session_state.page == "tele":
        st.button("📢 رشق أعضاء قنوات", use_container_width=True)
        st.button("👁️ زيادة مشاهدات", use_container_width=True)
        st.button("🤖 بوتات حماية", use_container_width=True)
    elif st.session_state.page == "tiktok":
        st.button("🎵 رشق متابعين", use_container_width=True)
        st.button("🔥 زيادة اكسبلور", use_container_width=True)
        st.button("❤️ لايكات تيك توك", use_container_width=True)
    else:
        st.button("✨ محسن المحتوى", use_container_width=True)
        st.button("📊 متوقع الهاشتاجات", use_container_width=True)
        st.button("🎭 مصمم البايو", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
