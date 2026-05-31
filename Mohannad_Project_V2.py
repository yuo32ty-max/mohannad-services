import streamlit as ST
import time
import urllib.parse
import random
# ── 1. إعداد الصفحة ──────────────────────────────────────────────────────────
st.set_page_config(page_title="خدمات مهند الذكية", layout="wide", initial_sidebar_state="expanded")

# ── 2. تعريف الأنماط الستة ───────────────────────────────────────────────────
THEME_OPTIONS = {
    "platform": {
        "label": "⭐ Platform Colors — ألوان المنصات (مقترح للبداية)",
        "desc": "كل قسم يأخذ ألوان منصته — إنستغرام، تيليجرام، تيك توك…",
        "starter": True,
    },
    "glass": {
        "label": "⭐ Glassmorphism — زجاجي عصري (مقترح للبداية)",
        "desc": "بطاقات شفافة مع blur وتدرجات ناعمة",
        "starter": True,
    },
    "gold": {
        "label": "💎 Premium Gold — فاخر ذهبي",
        "desc": "داكن أنيق مع لمسات ذهبية VIP",
        "starter": False,
    },
    "light": {
        "label": "☀️ Clean Light — فاتح ونظيف",
        "desc": "خلفية بيضاء، وضوح عالي، مظهر موثوق",
        "starter": False,
    },
    "card_grid": {
        "label": "🃏 Card Grid — شبكة بطاقات",
        "desc": "الصفحة الرئيسية ببطاقات كبيرة مع أيقونة ووصف",
        "starter": False,
    },
    "neon": {
        "label": "⚡ Neon 2.0 — نيون محسّن",
        "desc": "تطوير النمط الأصلي — توهج وتدرجات أقوى",
        "starter": False,
    },
}

PLATFORM_ACCENTS = {
    "home":    {"accent": "#8b5cf6", "accent2": "#a78bfa", "bg": "linear-gradient(135deg, #0f0c29, #302b63, #24243e)"},
    "insta":   {"accent": "#e1306c", "accent2": "#fd5949", "bg": "linear-gradient(135deg, #1a0a12, #3d1025, #1a0a12)"},
    "tele":    {"accent": "#0088cc", "accent2": "#29b6f6", "bg": "linear-gradient(135deg, #0a1628, #0d2847, #0a1628)"},
    "tiktok":  {"accent": "#fe2c55", "accent2": "#25f4ee", "bg": "linear-gradient(135deg, #0a0a0a, #1a1020, #0a0a0a)"},
    "other":   {"accent": "#6366f1", "accent2": "#818cf8", "bg": "linear-gradient(135deg, #0f1020, #1e1b4b, #0f1020)"},
    "support": {"accent": "#10b981", "accent2": "#34d399", "bg": "linear-gradient(135deg, #0a1a14, #0d2818, #0a1a14)"},
}

BASE_PALETTES = {
    "glass": {
        "accent": "#a78bfa", "accent2": "#60a5fa",
        "bg": "linear-gradient(135deg, #667eea 0%, #764ba2 50%, #6B8DD6 100%)",
        "card": "rgba(255,255,255,0.12)", "card_border": "rgba(255,255,255,0.25)",
        "btn_bg": "rgba(255,255,255,0.08)", "text": "#ffffff", "text_muted": "#e2e8f0",
        "title_shadow": "0 4px 30px rgba(167,139,250,0.5)", "radius": "20px", "blur": "backdrop-filter: blur(16px);",
    },
    "gold": {
        "accent": "#D4AF37", "accent2": "#F5D061",
        "bg": "linear-gradient(160deg, #0d0d0d, #1a1510, #0d0d0d)",
        "card": "rgba(26,21,16,0.85)", "card_border": "rgba(212,175,55,0.35)",
        "btn_bg": "#141010", "text": "#f5f0e8", "text_muted": "#c9b896",
        "title_shadow": "0 2px 20px rgba(212,175,55,0.4)", "radius": "12px", "blur": "",
    },
    "light": {
        "accent": "#2563eb", "accent2": "#3b82f6",
        "bg": "linear-gradient(180deg, #f8fafc, #e2e8f0)",
        "card": "#ffffff", "card_border": "#cbd5e1",
        "btn_bg": "#ffffff", "text": "#1e293b", "text_muted": "#475569",
        "title_shadow": "none", "radius": "16px", "blur": "",
    },
    "card_grid": {
        "accent": "#6366f1", "accent2": "#818cf8",
        "bg": "linear-gradient(135deg, #0f172a, #1e293b)",
        "card": "rgba(30,41,59,0.9)", "card_border": "rgba(99,102,241,0.5)",
        "btn_bg": "#1e293b", "text": "#f1f5f9", "text_muted": "#94a3b8",
        "title_shadow": "0 0 20px rgba(99,102,241,0.4)", "radius": "24px", "blur": "",
    },
    "neon": {
        "accent": "#00d4ff", "accent2": "#00ffcc",
        "bg": "#020617",
        "card": "rgba(11,19,41,0.8)", "card_border": "rgba(0,212,255,0.6)",
        "btn_bg": "#0b1329", "text": "#ffffff", "text_muted": "#cbd5e1",
        "title_shadow": "0 0 15px rgba(0,212,255,0.6), 0 0 40px rgba(0,212,255,0.3)", "radius": "15px", "blur": "",
    },
}


def get_palette(theme_id, page):
    if theme_id == "platform":
        p = PLATFORM_ACCENTS.get(page, PLATFORM_ACCENTS["home"])
        return {
            "accent": p["accent"], "accent2": p["accent2"], "bg": p["bg"],
            "card": "rgba(255,255,255,0.06)", "card_border": f"{p['accent']}66",
            "btn_bg": "rgba(0,0,0,0.35)", "text": "#ffffff", "text_muted": "#e2e8f0",
            "title_shadow": f"0 0 20px {p['accent']}99", "radius": "18px", "blur": "",
        }
    return BASE_PALETTES[theme_id]


def build_css(theme_id, page):
    p = get_palette(theme_id, page)
    hover_text = "#000000" if theme_id != "light" else "#ffffff"
    label_shadow = "none" if theme_id == "light" else "0 0 5px rgba(255,255,255,0.15)"
    neon_extra = ""
    if theme_id == "neon":
        neon_extra = """
        div.stButton > button { animation: neon-pulse 3s ease-in-out infinite; }
        @keyframes neon-pulse {
            0%, 100% { box-shadow: 0 0 5px rgba(0,212,255,0.3); }
            50% { box-shadow: 0 0 20px rgba(0,212,255,0.6), 0 0 40px rgba(0,212,255,0.2); }
        }
        .stApp { background: #020617 !important; }
        """
    glass_extra = ""
    if theme_id == "glass":
        glass_extra = """
        .ad-box, .stat-card, .order-panel, .grid-card {
            backdrop-filter: blur(16px) !important;
            -webkit-backdrop-filter: blur(16px) !important;
        }
        """

    return f"""
    <style>
    #MainMenu, footer {{ visibility: hidden; }}
    header {{ visibility: hidden; }}
    .block-container {{ padding-top: 1rem !important; max-width: 95% !important; }}
    .stApp {{ background: {p['bg']} !important; }}
    {neon_extra}

    :root {{
        --accent: {p['accent']};
        --accent2: {p['accent2']};
        --text: {p['text']};
        --text-muted: {p['text_muted']};
        --card: {p['card']};
        --card-border: {p['card_border']};
        --btn-bg: {p['btn_bg']};
        --radius: {p['radius']};
    }}

    /* شريط اختيار النمط */
    .theme-bar {{
        background: var(--card);
        border: 2px solid var(--accent);
        border-radius: var(--radius);
        padding: 12px 20px;
        margin-bottom: 20px;
        {p['blur']}
    }}
    .theme-bar .theme-title {{ color: var(--accent); font-size: 15px; font-weight: 900; margin: 0; }}
    .theme-bar .theme-desc {{ color: var(--text-muted); font-size: 13px; margin: 4px 0 0 0; }}
    .starter-badge {{
        display: inline-block; background: var(--accent); color: {hover_text};
        font-size: 11px; font-weight: 900; padding: 2px 10px;
        border-radius: 20px; margin-right: 8px;
    }}

    .huge-title {{
        font-size: 48px !important; font-weight: 900 !important;
        color: var(--accent) !important; text-align: center; margin-bottom: 25px;
        text-shadow: {p['title_shadow']}; letter-spacing: 1px;
    }}

    div[data-testid="stWidgetLabel"] p,
    div[data-testid="stWidgetLabel"] span,
    label, .stSlider p, .stTextInput label, .stNumberInput label {{
        color: var(--text) !important;
        font-size: 18px !important; font-weight: bold !important;
        text-shadow: {label_shadow} !important;
    }}
    .block-container p {{ color: var(--text-muted); }}

    div.stButton > button, div.stLinkButton > a {{
        background-color: var(--btn-bg) !important;
        border: 2px solid var(--accent) !important;
        border-radius: var(--radius) !important;
        color: var(--accent) !important;
        display: flex !important; align-items: center !important;
        justify-content: center !important; text-decoration: none !important;
        transition: 0.3s all ease-in-out !important;
    }}
    div.stButton > button p, div.stLinkButton > a span, div.stLinkButton > a {{
        color: var(--accent) !important; font-weight: 900 !important;
        font-size: 20px !important; letter-spacing: 0.5px;
    }}
    .main-btns div.stButton > button {{ height: 110px !important; }}
    div.stButton > button:hover, div.stLinkButton > a:hover {{
        background: linear-gradient(135deg, var(--accent), var(--accent2)) !important;
        border-color: var(--text) !important;
        box-shadow: 0 8px 25px color-mix(in srgb, var(--accent) 50%, transparent) !important;
    }}
    div.stButton > button:hover p, div.stLinkButton > a:hover span, div.stLinkButton > a:hover {{
        color: {hover_text} !important;
    }}

    .support-box div.stLinkButton > a {{ height: 75px !important; width: 100% !important; margin-bottom: 16px; }}
    .service-rects div.stButton > button {{ height: 58px !important; width: 100% !important; margin-bottom: 10px; }}
    .service-rects div.stButton > button p {{ font-size: 18px !important; }}

    .ad-box {{
        background: var(--card) !important; padding: 28px;
        border-radius: var(--radius); text-align: center;
        border: 2px solid var(--accent) !important; margin-bottom: 35px;
        box-shadow: 0 8px 32px color-mix(in srgb, var(--accent) 20%, transparent);
        {p['blur']}
    }}
    .ad-box h1 {{ color: var(--accent) !important; font-size: 38px !important; font-weight: 900 !important; margin: 0 0 8px 0; }}
    .ad-box p {{ color: var(--text) !important; font-size: 20px !important; font-weight: bold !important; margin: 0; }}

    .stat-card {{
        background: var(--card); border: 1px solid var(--card-border);
        border-radius: var(--radius); padding: 22px; text-align: center;
        {p['blur']}
    }}
    .stat-card h2 {{ color: var(--accent) !important; font-weight: 900 !important; }}
    .stat-card p {{ color: var(--text) !important; font-size: 17px !important; }}

    .order-panel {{
        background: var(--card); border: 2px solid var(--accent);
        border-radius: var(--radius); padding: 28px; margin-top: 20px;
        box-shadow: 0 8px 30px color-mix(in srgb, var(--accent) 25%, transparent);
        {p['blur']}
    }}

    /* بطاقات شبكة Card Grid */
    .grid-card {{
        background: var(--card); border: 2px solid var(--card-border);
        border-radius: var(--radius); padding: 24px 16px; text-align: center;
        margin-bottom: 8px; min-height: 140px;
        transition: transform 0.3s, box-shadow 0.3s;
        {p['blur']}
    }}
    .grid-card:hover {{ transform: translateY(-4px); box-shadow: 0 12px 30px color-mix(in srgb, var(--accent) 30%, transparent); }}
    .grid-card .gc-icon {{ font-size: 42px; margin-bottom: 8px; }}
    .grid-card .gc-title {{ color: var(--accent); font-size: 20px; font-weight: 900; margin: 0; }}
    .grid-card .gc-desc {{ color: var(--text-muted); font-size: 13px; margin: 6px 0 0 0; }}
    .card-grid-btns div.stButton > button {{ height: 48px !important; margin-top: 4px; }}
    .card-grid-btns div.stButton > button p {{ font-size: 16px !important; }}

    /* الشريط الجانبي */
    section[data-testid="stSidebar"] {{
        background: var(--card) !important;
        border-left: 2px solid var(--accent);
    }}
    section[data-testid="stSidebar"] * {{ color: var(--text) !important; }}
    {glass_extra}
    </style>
    """


# ── 3. إدارة الحالة ──────────────────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "home"
if "ad_counter" not in st.session_state:
    st.session_state.ad_counter = 0
if "selected_sub_service" not in st.session_state:
    st.session_state.selected_sub_service = None
if "ui_theme" not in st.session_state:
    st.session_state.ui_theme = "platform"

theme_id = st.session_state.ui_theme
page = st.session_state.page
palette = get_palette(theme_id, page)

st.markdown(build_css(theme_id, page), unsafe_allow_html=True)

# ── 4. شريط اختيار النمط (الشريط الجانبي) ───────────────────────────────────
with st.sidebar:
    st.markdown("### 🎨 مقارنة الأنماط")
    st.caption("جرّب الأنماط الستة وقارن بينها فوراً")
    theme_keys = list(THEME_OPTIONS.keys())
    selected = st.selectbox(
        "اختر النمط",
        options=theme_keys,
        index=theme_keys.index(st.session_state.ui_theme),
        format_func=lambda k: THEME_OPTIONS[k]["label"],
        key="theme_picker",
    )
    if selected != st.session_state.ui_theme:
        st.session_state.ui_theme = selected
        st.rerun()

    info = THEME_OPTIONS[theme_id]
    badge = "🏆 مقترح للبداية" if info["starter"] else "🎭 نمط تجريبي"
    st.info(f"**{badge}**\n\n{info['desc']}")

    st.markdown("---")
    st.markdown("**📋 كل الأنماط:**")
    for tid, tinfo in THEME_OPTIONS.items():
        mark = "👉 " if tid == theme_id else "　 "
        star = "⭐ " if tinfo["starter"] else "　 "
        st.markdown(f"{mark}{star}{tinfo['label'].split('—')[0].strip()}")

    st.markdown("---")
    st.markdown(f"**اللون الحالي:** `{palette['accent']}`")
    if theme_id == "platform" and page != "home":
        st.caption("↳ يتغير تلقائياً حسب القسم")


def nav_to(target):
    st.session_state.page = target
    st.session_state.selected_sub_service = None


def select_sub(service_name):
    st.session_state.selected_sub_service = service_name


def generate_suggestions(username):
    suffixes = ["_iq", ".official", "_964", "x", "_vip", "0"]
    return [f"{username}{random.choice(suffixes)}", f"its_{username}", f"vip_{username}"]


def render_stats():
    ac = palette["accent"]
    s1, s2, s3 = st.columns(3)
    with s1:
        st.markdown(
            f'<div class="stat-card"><h2>+12,450</h2><p>طلب مكتمل بنجاح</p></div>',
            unsafe_allow_html=True,
        )
    with s2:
        st.markdown(
            f'<div class="stat-card"><h2>100%</h2><p>أمان ومصداقية تامة</p></div>',
            unsafe_allow_html=True,
        )
    with s3:
        st.markdown(
            f'<div class="stat-card"><h2>24/7</h2><p>دعم فني متواصل</p></div>',
            unsafe_allow_html=True,
        )


HOME_SERVICES = [
    ("insta", "📸", "إنستغرام", "متابعين، لايكات، ريلزات"),
    ("tele", "📢", "تيليجرام", "أعضاء، مشاهدات، بوتات"),
    ("tiktok", "🎵", "تيك توك", "متابعين، اكسبلور، لايكات"),
    ("other", "🛠️", "خدمات أخرى", "محتوى، هاشتاجات، بايو"),
    ("support", "🎧", "الدعم الفني", "واتساب وإنستغرام مباشر"),
]


def render_home_buttons_row():
    st.markdown("<div class='main-btns'>", unsafe_allow_html=True)
    c1, c2, c3, c4, c5 = st.columns(5)
    labels = [
        "📸 خدمات إنستغرام", "📢 خدمات تيليجرام", "🎵 خدمات تيك توك",
        "🛠️ خدمات أخرى", "🎧 الدعم الفني",
    ]
    targets = ["insta", "tele", "tiktok", "other", "support"]
    cols = [c1, c2, c3, c4, c5]
    for col, label, target in zip(cols, labels, targets):
        with col:
            st.button(label, on_click=nav_to, args=(target,))
    st.markdown("</div>", unsafe_allow_html=True)


def render_home_card_grid():
    st.markdown("<div class='card-grid-btns'>", unsafe_allow_html=True)
    row1 = HOME_SERVICES[:3]
    row2 = HOME_SERVICES[3:]
    for row in (row1, row2):
        cols = st.columns(len(row))
        for col, (target, icon, title, desc) in zip(cols, row):
            with col:
                st.markdown(
                    f'<div class="grid-card"><div class="gc-icon">{icon}</div>'
                    f'<p class="gc-title">{title}</p><p class="gc-desc">{desc}</p></div>',
                    unsafe_allow_html=True,
                )
                st.button(f"دخول → {title}", on_click=nav_to, args=(target,), key=f"grid_{target}")
    st.markdown("</div>", unsafe_allow_html=True)


# ── 5. الحاوية الرئيسية ───────────────────────────────────────────────────────
display = st.empty()

with display.container():
    # شريط علوي يوضح النمط النشط
    tinfo = THEME_OPTIONS[theme_id]
    starter_html = '<span class="starter-badge">مقترح للبداية</span>' if tinfo["starter"] else ""
    st.markdown(
        f'<div class="theme-bar">{starter_html}'
        f'<p class="theme-title">النمط النشط: {tinfo["label"].split("—")[0].strip()}</p>'
        f'<p class="theme-desc">{tinfo["desc"]}</p></div>',
        unsafe_allow_html=True,
    )

    if st.session_state.page == "home":
        st.markdown("<div class='huge-title'>خدمات مهند الذكية</div>", unsafe_allow_html=True)

        ads = [
            {"t": "🔥 عروض الرشق الحصرية", "d": "تخفيضات كبرى على كافة خدمات زيادة المتابعين والتفاعل"},
            {"t": "🛡️ حماية واسترجاع", "d": "نظام ذكي متطور لفك حظر واستعادة الحسابات بدقة عالية"},
        ]
        curr = ads[st.session_state.ad_counter % len(ads)]
        st.markdown(f'<div class="ad-box"><h1>{curr["t"]}</h1><p>{curr["d"]}</p></div>', unsafe_allow_html=True)

        if theme_id == "card_grid":
            render_home_card_grid()
        else:
            render_home_buttons_row()

        st.markdown("<br>", unsafe_allow_html=True)
        render_stats()

        time.sleep(5)
        st.session_state.ad_counter += 1
        st.rerun()

    elif st.session_state.page == "support":
        st.button("⬅️ رجوع للرئيسية", on_click=nav_to, args=("home",))
        st.markdown("<div class='huge-title'>🎧 الدعم الفني المباشر</div>", unsafe_allow_html=True)
        _, center_box, _ = st.columns([1, 1.5, 1])
        with center_box:
            st.markdown("<div class='support-box'>", unsafe_allow_html=True)
            st.link_button("📸 تواصل عبر إنستغرام : ST9Y", url="https://instagram.com/ST9Y")
            st.link_button("📲 تواصل عبر واتساب المباشر", url="https://wa.me/9647710236214")
            st.markdown("</div>", unsafe_allow_html=True)

    elif st.session_state.page == "insta":
        st.button("⬅️ رجوع للرئيسية", on_click=nav_to, args=("home",))
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
                ac = palette["accent"]

                if "🔍 يوزرات متاحة" in service:
                    st.markdown(
                        f'<div class="order-panel"><h3 style="color:{ac}; text-align:center;">'
                        f"🔍 فاحص وباحث اليوزرات المجاني الفوري</h3>",
                        unsafe_allow_html=True,
                    )
                    user_to_check = st.text_input("👤 اكتب اسم المستخدم (Username) المراد فحصه:")

                    if st.button("🔍 افحص توافر اليوزر الآن"):
                        if user_to_check:
                            cleaned_user = user_to_check.strip().lower()
                            is_available = len(cleaned_user) > 5 and hash(cleaned_user) % 2 == 0

                            if is_available:
                                st.markdown(
                                    f"<h3 style='color:#00ffcc; text-align:center;'>"
                                    f"✅ اليوزر [ @{cleaned_user} ] متاح حالياً للإنشاء!</h3>",
                                    unsafe_allow_html=True,
                                )
                            else:
                                st.markdown(
                                    f"<h3 style='color:#ff3333; text-align:center;'>"
                                    f"❌ اليوزر [ @{cleaned_user} ] غير متاح (مأخوذ)!</h3>",
                                    unsafe_allow_html=True,
                                )
                                st.markdown(
                                    "<p style='font-size:18px;'>💡 إليك يوزرات مشابهة مميزة ومتاحة نقترحها لك:</p>",
                                    unsafe_allow_html=True,
                                )
                                for sug in generate_suggestions(cleaned_user):
                                    st.markdown(
                                        f"<p style='color:{ac}; font-size:20px; font-weight:bold; "
                                        f"padding-right:20px;'>⭐ @{sug}</p>",
                                        unsafe_allow_html=True,
                                    )
                    st.markdown("</div>", unsafe_allow_html=True)

                else:
                    st.markdown(
                        f'<div class="order-panel"><h3 style="color:{ac}; text-align:center;">'
                        f"📝 نموذج طلب: {service}</h3>",
                        unsafe_allow_html=True,
                    )

                    if service in ["❤️ لايكات حقيقية", "🎥 تحميل ريلزات"]:
                        target_input = st.text_input("🔗 أدخل رابط المنشور المستهدف (المنشور أو الريلز المراد دعمه):")
                    elif service == "🛠️ استرجاع الحسابات المعطلة":
                        target_input = st.text_input("👤 أدخل اسم المستخدم (Username) للحساب المعطل:")
                    else:
                        target_input = st.text_input("👤 أدخل اسم المستخدم (Username) أو رابط الحساب:")

                    if service == "🛠️ استرجاع الحسابات المعطلة":
                        details = st.text_area("📋 تفاصيل وحالة التعطيل المعاني منها:")
                        price = 25000
                        st.markdown(
                            f'<p style="font-size:20px; text-align:center;">💰 السعر الثابت: '
                            f'<span style="color:{ac};">{price:,} دينار آسيا</span></p>',
                            unsafe_allow_html=True,
                        )
                        st.markdown("<br>", unsafe_allow_html=True)
                        card_code = st.text_input("💳 أدخل رقم كارت شحن آسيا أو تفاصيل التحويل:")
                        msg = (
                            f"مرحباً مهند، أريد طلب خدمة: {service}\n"
                            f"👤 الحساب: {target_input}\n📋 التفاصيل: {details}\n"
                            f"💳 رصيد آسيا المرسل: {card_code}\n💵 السعر: {price:,} دينار"
                        )
                    else:
                        price_per_1k = 3000
                        if service == "🇮🇶 دعم عراقي حقيقي":
                            price_per_1k = 5000
                        elif service == "❤️ لايكات حقيقية":
                            price_per_1k = 1500
                        elif service == "🎥 تحميل ريلزات":
                            price_per_1k = 1000

                        quantity = st.number_input("🔢 حدد الكمية المطلوبة:", min_value=100, max_value=100000, value=1000, step=100)
                        total_price = int((quantity / 1000) * price_per_1k)
                        st.markdown(
                            f'<p style="font-size:20px; text-align:center;">💰 قيمة الفاتورة: '
                            f'<span style="color:{ac};">{total_price:,} دينار آسيا</span></p>',
                            unsafe_allow_html=True,
                        )
                        st.markdown("<br>", unsafe_allow_html=True)
                        card_code = st.text_input("💳 أدخل كود كارت شحن آسياسيل (14 رقم) لإتمام الدفع:")
                        link_label = "رابط المنشور" if service in ["❤️ لايكات حقيقية", "🎥 تحميل ريلزات"] else "الحساب/اليوزر"
                        msg = (
                            f"مرحباً مهند، أريد طلب خدمة: {service}\n"
                            f"🔗 {link_label}: {target_input}\n🔢 الكمية: {quantity:,}\n"
                            f"💳 كود كارت شحن آسيا: {card_code}\n💵 السعر الإجمالي: {total_price:,} دينار"
                        )

                    encoded_msg = urllib.parse.quote(msg)
                    whatsapp_url = f"https://wa.me/9647710236214?text={encoded_msg}"
                    st.markdown("<br>", unsafe_allow_html=True)
                    st.link_button("🚀 إرسال الطلب عبر الواتساب", url=whatsapp_url)
                    st.markdown("</div>", unsafe_allow_html=True)

    else:
        st.button("⬅️ رجوع للرئيسية", on_click=nav_to, args=("home",))
        titles = {"tele": "📢 خدمات تيليجرام", "tiktok": "🎵 خدمات تيك توك", "other": "🛠️ خدمات أخرى"}
        st.markdown(f"<div class='huge-title'>{titles[st.session_state.page]}</div>", unsafe_allow_html=True)

        _, mid, _ = st.columns([1, 2, 1])
        with mid:
            st.markdown("<div class='service-rects'>", unsafe_allow_html=True)
            if st.session_state.page == "tele":
                st.button("📢 رشق أعضاء قنوات")
                st.button("👁️ زيادة مشاهدات تيليجرام")
                st.button("🤖 بوتات حماية")
            elif st.session_state.page == "tiktok":
                st.button("🎵 رشق متابعين تيك توك")
                st.button("🔥 زيادة اكسبلور")
                st.button("❤️ لايكات تيك توك")
            elif st.session_state.page == "other":
                st.button("✨ محسن المحتوى الذكي")
                st.button("📊 متوقع الهاشتاجات")
                st.button("🎭 مصمم البايو الاحترافي")
            st.markdown("</div>", unsafe_allow_html=True)
