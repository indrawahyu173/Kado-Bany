import streamlit as st
import os

# 1. Bikin pendeteksi lokasi otomatis
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

# 2. Pengaturan dasar halaman website
st.set_page_config(page_title="The Shape of Our Heart ❤️", page_icon="🎁", layout="centered")

# 3. Bagian Header / Judul
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>The Shape of Our Heart ❤️</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px; font-style: italic;'>'He deals the cards as a meditation...'</p>", unsafe_allow_html=True)

# 4. Pemutar Musik (Lagu The Shape of My Heart)
st.audio(os.path.join(ASSETS_DIR, "lagu.mp3"), format="audio/mpeg", autoplay=True)
st.divider()

# 5. Bagian Cerita (Storytelling section)
st.subheader("Our Story 📖")
st.markdown("""
> Setiap lembar perjalanan yang kita lewati punya cerita dan maknanya sendiri. 
> Sama seperti alunan musik ini, setiap detik bersama lu adalah bagian terindah dalam hidup gua yang nggak bakal pernah tergantikan.
""")
st.divider()

# 6. Bagian Galeri (4 Foto)
st.subheader("Memori Berdua 📸")

col1, col2 = st.columns(2)

with col1:
    st.image(os.path.join(ASSETS_DIR, "foto1.jpeg"), caption="Momen 1 - Senyum manisnya")
    st.image(os.path.join(ASSETS_DIR, "foto3.jpeg"), caption="Momen 3 - Jalan-jalan seru")

with col2:
    st.image(os.path.join(ASSETS_DIR, "foto2.jpeg"), caption="Momen 2 - Pas lagi ngedate")
    st.image(os.path.join(ASSETS_DIR, "foto4.jpeg"), caption="Momen 4 - Kenangan tak terlupakan")

st.divider()

# 7. Bagian Video (1 Video Utama)
st.subheader("Video Spesial 🎬")
st.video(os.path.join(ASSETS_DIR, "video1.mp4"))
st.caption("Momen spesial kita - Tonton sampai habis ya!")

# 8. Footer
st.divider()
st.markdown("<p style='text-align: center; color: #ff4b4b;'>Dibuat dengan ❤️ khusus buat kamu.</p>", unsafe_allow_html=True)
