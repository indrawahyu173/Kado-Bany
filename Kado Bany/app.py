import streamlit as st

# 1. Pengaturan dasar halaman website
st.set_page_config(page_title="Kado Spesial Buat Kamu ❤️", page_icon="🎁", layout="centered")

# 2. Bagian Header / Judul
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>Perjalanan Kita ❤️</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Kumpulan memori indah, tawa, dan cerita yang kita lewati berdua.</p>", unsafe_allow_html=True)
st.divider()

# 3. Bagian Galeri (4 Foto)
st.subheader("Memori Berdua 📸")

# Bikin 2 kolom untuk grid foto biar rapi
col1, col2 = st.columns(2)

with col1:
    st.image("assets/foto1.jpeg", caption="Momen 1 - Senyum manisnya")
    st.image("assets/foto3.jpeg", caption="Momen 3 - Jalan-jalan seru")

with col2:
    st.image("assets/foto2.jpeg", caption="Momen 2 - Pas lagi ngedate")
    st.image("assets/foto4.jpeg", caption="Momen 4 - Kenangan tak terlupakan")

st.divider()

# 4. Bagian Video (1 Video Utama)
st.subheader("Video Spesial 🎬")
st.video("assets/video1.mp4")
st.caption("Momen spesial kita - Tonton sampai habis ya!")

# 5. Footer
st.divider()
st.markdown("<p style='text-align: center; color: #ff4b4b;'>Dibuat dengan ❤️ khusus buat kamu.</p>", unsafe_allow_html=True)
