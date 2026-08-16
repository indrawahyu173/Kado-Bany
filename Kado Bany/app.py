import streamlit as st
import os

# 1. Bikin pendeteksi lokasi otomatis (Trik Pro)
# Biar sistem selalu nemuin folder foto lu walaupun posisinya di dalam folder lain pas di GitHub
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Pastikan nama folder lu di GitHub adalah 'assets' (pakai 's'). 
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

# 2. Pengaturan dasar halaman website
st.set_page_config(page_title="Kado Spesial Buat Kamu ❤️", page_icon="🎁", layout="centered")

# 3. Bagian Header / Judul
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>Perjalanan Kita ❤️</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Kumpulan memori indah, tawa, dan cerita yang kita lewati berdua.</p>", unsafe_allow_html=True)
st.divider()

# 4. Bagian Galeri (4 Foto)
st.subheader("Memori Berdua 📸")

col1, col2 = st.columns(2)

with col1:
    st.image(os.path.join(ASSETS_DIR, "foto1.jpeg"), caption="Momen 1 - Senyum manisnya")
    st.image(os.path.join(ASSETS_DIR, "foto3.jpeg"), caption="Momen 3 - Jalan-jalan seru")

with col2:
    st.image(os.path.join(ASSETS_DIR, "foto2.jpeg"), caption="Momen 2 - Pas lagi ngedate")
    st.image(os.path.join(ASSETS_DIR, "foto4.jpeg"), caption="Momen 4 - Kenangan tak terlupakan")

st.divider()

# 5. Bagian Video (1 Video Utama)
st.subheader("Video Spesial 🎬")
st.video(os.path.join(ASSETS_DIR, "video1.mp4"))
st.caption("Momen spesial kita - Tonton sampai habis ya!")

# 6. Footer
st.divider()
st.markdown("<p style='text-align: center; color: #ff4b4b;'>Dibuat dengan ❤️ khusus buat kamu.</p>", unsafe_allow_html=True)
