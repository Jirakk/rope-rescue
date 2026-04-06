import streamlit as st
import math

# 🔥 모바일 최적 설정
st.set_page_config(page_title="합력 계산기", page_icon="🔧", layout="centered")

# 🔥 CSS (모바일 핵심)
st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-size: 18px;
    }
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        padding-left: 1rem;
        padding-right: 1rem;
        max-width: 500px;
        margin: auto;
    }
    .card {
        background-color: white;
        padding: 18px;
        border-radius: 16px;
        box-shadow: 0px 3px 8px rgba(0,0,0,0.08);
        margin-bottom: 15px;
    }
    .title {
        font-size: 26px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 18px;
        font-weight: 600;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 🔹 제목
st.markdown("<div class='title'>🔧 합력 계산기</div>", unsafe_allow_html=True)

# 🔹 입력 카드
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>📌 입력</div>", unsafe_allow_html=True)

W_kg = st.number_input("하중 W (kg)", min_value=0.0, value=100.0, step=10.0)
A = st.slider("내각 A (도)", 0, 150, 60)

st.markdown("</div>", unsafe_allow_html=True)

# 🔹 계산
W = W_kg * 9.81
F = (W * 2) * math.cos(math.radians(A / 2))

SF = 10
required_capacity = F * SF

F_kN = F / 1000
required_capacity_kN = required_capacity / 1000

# 🔹 결과 카드
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>📊 결과</div>", unsafe_allow_html=True)

st.metric("합력", f"{F_kN:.2f} kN")
st.metric("MBS (10:1)", f"{required_capacity_kN:.2f} kN")

st.markdown("</div>", unsafe_allow_html=True)

# 🔹 위험도 카드
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>⚠️ 위험도</div>", unsafe_allow_html=True)

if A <= 60:
    st.error("🚨 경고")
elif A <= 90:
    st.warning("⚠️ 주의")
else:
    st.success("✅ 안정")

if A < 30:
    st.error("❗ 매우 위험: 재설계 필요")

st.markdown("</div>", unsafe_allow_html=True)

# 🔹 참고 카드
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("📌 참고")
st.markdown("- 본 계산은 근삿값 기준")
st.markdown("- 위험도 경고 시 추가 확인 필수")
st.markdown("</div>", unsafe_allow_html=True)