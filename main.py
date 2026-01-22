import streamlit as st

# Sayfa ayarları
st.set_page_config(
    page_title="Hemşirelik Dijital İkizi",
    layout="wide"
)

# SOL PANEL (Sidebar)
st.sidebar.title("🩺 Hemşire Paneli")

sayfa = st.sidebar.radio(
    "Sayfa Seçiniz:",
    ["🏠 Ana Kontrol Paneli", "🔮 Simülasyon & Öngörü", "✅ Klinik Validasyon"]
)

st.sidebar.markdown("---")
st.sidebar.subheader("📥 Hasta Verileri")

nabiz = st.sidebar.number_input("Nabız (bpm)", min_value=40, max_value=150, value=72)
spo2 = st.sidebar.number_input("SpO₂ (%)", min_value=80, max_value=100, value=98)
hareket = st.sidebar.selectbox(
    "Hareketlilik Durumu",
    ["Aktif", "Kısıtlı", "Hareketsiz"]
)

oda_sicakligi = st.sidebar.slider("Oda Sıcaklığı (°C)", 16, 30, 22)

if sayfa == "🏠 Ana Kontrol Paneli":
    st.title("🏠 Ana Kontrol Paneli")
    st.caption("Hastanın anlık bakım durumu – dijital ikiz görünümü")
    st.markdown("---")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Nabız", f"{nabiz} bpm")
    with c2:
        st.metric("SpO₂", f"%{spo2}")
    with c3:
        st.metric("Hareket", hareket)

    st.markdown("---")
    st.info("⚙️ Henüz risk hesaplaması yok. Bir sonraki adımda ekleyeceğiz.")


elif sayfa == "🔮 Simülasyon & Öngörü":
    st.title("🔮 Simülasyon & Öngörü")
    st.write("Bu sayfa, 'ne olursa?' senaryoları içindir.")
    st.warning("Henüz simülasyon yok.")

elif sayfa == "✅ Klinik Validasyon":
    st.title("✅ Klinik Validasyon")
    st.write("Bu sayfa, model doğrulama içindir.")
    st.success("Henüz karşılaştırma yok.")


