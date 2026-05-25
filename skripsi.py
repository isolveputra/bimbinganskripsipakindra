import streamlit as st

# Pengaturan halaman
st.set_page_config(page_title="Kuis Bimbingan Skripsi", page_icon="💻", layout="centered")

st.title("🎯 Kuis Prasyarat QR Code Bimbingan")
st.write("Selesaikan 3 tantangan informatika ini untuk mendapatkan QR Code Absensi Bimbingan Anda!")
st.divider()

# Inisialisasi session state untuk menyimpan jawaban
if "skor" not in st.session_state:
    st.session_state.skor = 0

# --- SOAL 1 ---
st.subheader("Soal 1: Kompleksitas Algoritma")
soal_1 = st.radio(
    "Manakah dari algoritma pengurutan (sorting) berikut yang memiliki Best-Case Time Complexity sebesar $O(n)$?",
    ["Quick Sort", "Merge Sort", "Bubble Sort", "Selection Sort"],
    index=None,
    key="q1"
)

# --- SOAL 2 ---
st.subheader("Soal 2: Software Engineering")
soal_2 = st.radio(
    "Dalam Arsitektur MVC (Model-View-Controller), bagian yang bertanggung jawab untuk menangani logika bisnis dan interaksi database adalah...",
    ["View", "Controller", "Model", "Router"],
    index=None,
    key="q2"
)

# --- SOAL 3 ---
st.subheader("Soal 3: Basis Data")
soal_3 = st.radio(
    "Perintah SQL yang digunakan untuk menambahkan kolom baru pada tabel yang sudah ada adalah...",
    ["UPDATE TABLE", "ALTER TABLE", "INSERT INTO", "ADD COLUMN"],
    index=None,
    key="q3"
)

st.divider()

# Tombol Evaluasi
if st.button("Cek Jawaban & Ambil QR Code", type="primary"):
    # Validasi jawaban
    benar_1 = (soal_1 == "Bubble Sort")
    benar_2 = (soal_2 == "Model")
    # Catatan: ALTER TABLE nama_tabel ADD nama_kolom tipe_data;
    benar_3 = (soal_3 == "ALTER TABLE")
    
    if benar_1 and benar_2 and benar_3:
        st.balloons()
        st.success("🎉 Selamat! Semua jawaban Anda BENAR. Silakan scan QR Code di bawah untuk absensi bimbingan.")
        
        # Tampilkan QR Code (Ganti URL di bawah dengan file QR Code Anda)
        # Anda bisa meletakkan file gambar 'qrcode.png' di folder yang sama dengan file app.py
        try:
            st.image("qrcode.png", caption="QR Code Bimbingan Skripsi", width=300)
        except:
            st.warning("⚠️ File 'qrcode.png' tidak ditemukan di server. Hubungi Dosen Anda.")
            # Opsi alternatif menggunakan link eksternal jika gambar lokal tidak ada:
            # st.image("https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=LINK_ABSENSI_ANDA", width=300)
            
    else:
        st.error("❌ Waduh, masih ada jawaban yang salah atau belum diisi. Silakan periksa kembali jawabanmu!")
        
        # Memberikan feedback mana yang salah tanpa memberi tahu jawaban benarnya
        if not benar_1 and soal_1 is not None:
            st.info("Petunjuk Soal 1: Algoritma ini sangat efisien jika datanya sudah urut dari awal.")
        if not benar_2 and soal_2 is not None:
            st.info("Petunjuk Soal 2: Bagian ini merepresentasikan struktur data aplikasi Anda.")
        if not benar_3 and soal_3 is not None:
            st.info("Petunjuk Soal 3: Keyword ini digunakan untuk 'mengubah' struktur skema tabel.")
