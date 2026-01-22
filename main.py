import streamlit as st
import random

# 1️⃣ Sayfanın başlığı
st.title("🩺 Dijital İkiz – Hemşirelik Karar Destek Prototipi")

st.write("Bu ekran, bir hastanın dijital ikizini simüle eder.")

# 2️⃣ SAHTE HASTA VERİSİ OLUŞTURUYORUZ
heart_rate = random.randint(60, 110)      # Nabız
spo2 = random.randint(88, 100)             # Oksijen
mobility = random.choice([0, 1])           # 0: hareketsiz, 1: hareketli
room_temp = random.randint(20, 30)         # Oda sıcaklığı

# 3️⃣ HASTA VERİLERİNİ GÖSTER
st.subheader("📊 Hasta Verileri")
st.metric("❤️ Nabız", heart_rate)
st.metric("🫁 SpO₂", spo2)
st.metric("🌡️ Oda Sıcaklığı", room_temp)

if mobility == 0:
    st.write("🛏️ Hareketlilik: Hareketsiz")
else:
    st.write("🚶 Hareketlilik: Hareketli")

# 4️⃣ HEMŞİRELİK RİSK ANALİZİ (NANDA MANTIĞI)
st.subheader("⚠️ Hemşirelik Risk Değerlendirmesi")

riskler = []

if mobility == 0 and room_temp > 26:
    riskler.append("Deri Bütünlüğünde Bozulma Riski")

if spo2 < 90:
    riskler.append("Etkisiz Solunum Örüntüsü")

# 5️⃣ SONUCU GÖSTER
if riskler:
    st.error("🚨 RİSK TESPİT EDİLDİ")
    for r in riskler:
        st.write("•", r)
else:
    st.success("✅ Hasta stabil, risk tespit edilmedi.")
