import streamlit as st
import math

st.title("합력 계산기(안전계수 10:1)")

# 입력
W_kg = st.number_input("하중(kg)", min_value=0.0, value=100.0, step=10.0)
A = st.slider("내각", 0, 150, 60)

# 🔥 kg → N 변환
W = W_kg * 9.81

# 계산
F = (W * 2) * math.cos(math.radians(A / 2))

# 안전계수 10:1
SF = 10
required_capacity = F * SF
F_kN = F / 1000
required_capacity_kN = required_capacity / 1000

# 출력
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>📊 결과</div>", unsafe_allow_html=True)

st.metric("합력", f"{F_kN:.2f} kN")
st.metric("필요MBS (10:1)", f"{required_capacity_kN:.2f} kN")

st.markdown("</div>", unsafe_allow_html=True)

# 위험도 표시
st.markdown("### ⚠️ 위험도")

if A <= 60:
    st.error("🚨 경고")
elif A <= 119:
    st.warning("⚠️ 주의")
else:
    st.success("✅ 안정")

# 추가 경고
if A < 30:
    st.error("❗ 매우 위험: 재설계 필요")

# 참고 정보
st.markdown("---")
st.markdown("📌 참고")
st.markdown("- 본 계산은 근삿값 기준")
st.markdown("- 위험도 경고 시 추가 확인 필수")
