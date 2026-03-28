import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Hesap Makinesi", layout="centered", page_icon="🧮")

# ── Custom CSS ──
css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Outfit:wght@300;500;700&display=swap');
[data-testid="stAppViewContainer"] {
    background: linear-gradient(160deg, #0f0c29, #1a1a40, #24243e);
}
[data-testid="stHeader"] {
    background: transparent;
}
h1 {
    font-family: 'Outfit', sans-serif !important;
    font-weight: 700 !important;
    background: linear-gradient(135deg, #00d2ff, #7b2ff7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    font-size: 2.6rem !important;
}
h2, h3 {
    font-family: 'Outfit', sans-serif !important;
    color: #c4c4e0 !important;
}
p, span, label, li {
    font-family: 'Outfit', sans-serif !important;
    color: #b8b8d0 !important;
}
[data-testid="stTabs"] button {
    font-family: 'Outfit', sans-serif !important;
    color: #8888aa !important;
}
[data-testid="stTabs"] button[aria-selected="true"] {
    color: #00d2ff !important;
    border-bottom: 2px solid #7b2ff7;
}
input[type="text"], textarea {
    font-family: 'JetBrains Mono', monospace !important;
    background: rgba(255, 255, 255, 0.04) !important;
    border: 1px solid rgba(123, 47, 247, 0.25) !important;
    border-radius: 12px !important;
    color: #e0e0ff !important;
}
[data-testid="stBaseButton-secondary"] {
    background: linear-gradient(135deg, #7b2ff7, #00d2ff) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 12px !important;
}
[data-testid="stMetric"] {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(123, 47, 247, 0.15);
    border-radius: 16px;
    padding: 16px 20px;
}
[data-testid="stMetricValue"] {
    font-family: 'JetBrains Mono', monospace !important;
    color: #00d2ff !important;
}
[data-testid="stExpander"] {
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(123, 47, 247, 0.12);
    border-radius: 14px;
}
hr {
    border-color: rgba(123, 47, 247, 0.15) !important;
}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# ── Guvenli fonksiyon listesi ──
allowed_names = {
    "sqrt": math.sqrt,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "log": math.log,
    "log10": math.log10,
    "pi": math.pi,
    "e": math.e,
    "abs": abs,
    "pow": pow,
    "np": np,
}

# ── Baslik ──
st.title("🧮 Hesap Makinesi")

# ── Sekmeler ──
tab_calc, tab_graph, tab_ref = st.tabs(["⚡ Hesapla", "📈 Grafik", "📖 Referans"])

# ── TAB 1: Hesaplama ──
with tab_calc:
    expr = st.text_input(
        "Ifade gir",
        placeholder="orn: sqrt(144) + sin(pi/4)",
        label_visibility="collapsed",
    )

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        calc_btn = st.button("Hesapla", use_container_width=True)

    if calc_btn and expr:
        try:
            result = eval(expr, {"__builtins__": None}, allowed_names)
            c1, c2, c3 = st.columns([1, 2, 1])
            with c2:
                st.metric(label="Sonuc", value=f"{result:,.10g}")
        except ZeroDivisionError:
            st.error("Sifira bolme hatasi!")
        except Exception:
            st.error("Gecersiz ifade — lutfen kontrol et.")

    with st.expander("Hizli islemler"):
        qc1, qc2, qc3, qc4 = st.columns(4)
        quick_buttons = [
            ("sqrt", "sqrt("), ("pi", "pi"), ("sin", "sin("), ("cos", "cos("),
            ("tan", "tan("), ("log", "log("), ("log10", "log10("), ("e^x", "e**"),
        ]
        for i, (label, val) in enumerate(quick_buttons):
            col = [qc1, qc2, qc3, qc4][i % 4]
            with col:
                if st.button(label, key=f"q_{i}", use_container_width=True):
                    st.code(val, language="python")

# ── TAB 2: Grafik ──
with tab_graph:
    func = st.text_input(
        "Fonksiyon gir",
        placeholder="orn: np.sin(x) * np.exp(-x**2/20)",
        label_visibility="collapsed",
    )

    rc1, rc2 = st.columns(2)
    with rc1:
        x_min = st.number_input("x min", value=-10.0, step=1.0)
    with rc2:
        x_max = st.number_input("x max", value=10.0, step=1.0)

    gc1, gc2, gc3 = st.columns([1, 1, 1])
    with gc2:
        graph_btn = st.button("Grafik Ciz", use_container_width=True)

    if graph_btn and func:
        try:
            x = np.linspace(x_min, x_max, 500)
            y = eval(func, {"__builtins__": None}, {"x": x, **allowed_names})

            with plt.style.context("dark_background"):
                fig, ax = plt.subplots(figsize=(8, 4.5))
                fig.patch.set_facecolor("#12102e")
                ax.set_facecolor("#12102e")
                ax.plot(x, y, color="#00d2ff", linewidth=2.2)
                ax.fill_between(x, y, alpha=0.08, color="#7b2ff7")
                ax.set_xlabel("x", fontsize=12, color="#8888aa")
                ax.set_ylabel("f(x)", fontsize=12, color="#8888aa")
                ax.set_title(f"f(x) = {func}", fontsize=13, color="#c4c4e0", pad=14)
                ax.tick_params(colors="#6a6a8e")
                ax.grid(True, alpha=0.12, color="#7b2ff7")
                for spine in ax.spines.values():
                    spine.set_color("#2a2a4e")
                st.pyplot(fig)
                plt.close(fig)
        except Exception:
            st.error("Fonksiyon hatali — degisken olarak x kullan.")

# ── TAB 3: Referans ──
with tab_ref:
    st.markdown("### Kullanilabilir fonksiyonlar")
    ref_data = {
        "Fonksiyon": [
            "sqrt(x)", "sin(x)", "cos(x)", "tan(x)",
            "log(x)", "log10(x)", "abs(x)", "pow(x, y)",
            "pi", "e",
        ],
        "Aciklama": [
            "Karekok", "Sinus (radyan)", "Kosinus (radyan)", "Tanjant (radyan)",
            "Dogal logaritma", "10 tabaninda log", "Mutlak deger", "x ussu y",
            "pi = 3.14159", "e = 2.71828",
        ],
        "Ornek": [
            "sqrt(16) = 4", "sin(pi/2) = 1", "cos(0) = 1", "tan(pi/4) = 1",
            "log(e) = 1", "log10(1000) = 3", "abs(-5) = 5", "pow(2,10) = 1024",
            "2*pi = 6.283", "e**2 = 7.389",
        ],
    }
    st.dataframe(ref_data, use_container_width=True, hide_index=True)

    st.markdown("### Grafik ipuclari")
    st.markdown("- Numpy: `np.sin(x)`, `np.exp(x)` kullan")
    st.markdown("- Birlesik: `np.sin(x) + np.cos(2*x)`")
    st.markdown("- Ustel azalma: `np.exp(-x**2) * np.sin(5*x)`")

# ── Footer ──
st.markdown("---")
