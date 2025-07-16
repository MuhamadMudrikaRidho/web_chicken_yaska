# Web E-Commerce Chicken Yasaka (Versi Flask)

Aplikasi web e-commerce fungsional untuk penjualan ayam potong. Proyek ini dikembangkan menggunakan Python dengan framework Flask sebagai **Final Project** untuk program **Studi Independen Bersertifikat (MSIB) Kampus Merdeka** di mitra **[Learning X](https://www.learningx.com/)**.

![Screenshot Aplikasi](https://github.com/user-attachments/assets/1e4f90f8-4b53-4fc0-81fe-0fefea3f5c55)

## 🚀 Fitur Utama

-   **Katalog Produk**: Menampilkan semua produk yang tersedia dengan rapi.
-   **Manajemen Keranjang**: Pengguna dapat menambah, mengubah jumlah, dan menghapus item dari keranjang belanja.
-   **Proses Checkout**: Alur untuk menyelesaikan pesanan dari keranjang.
-   **Autentikasi Pengguna**: Sistem registrasi dan login untuk pelanggan.
-   **Desain Responsif**: Tampilan yang menyesuaikan dengan baik di perangkat desktop maupun mobile.
-   **Admin**: Dashboard admin untuk mengelola menu, user, dll.

## 🛠️ Teknologi yang Digunakan

Berikut adalah tumpukan teknologi yang digunakan dalam proyek ini:

-   **Backend**:
    -   **Python**: Bahasa pemrograman utama.
    -   **Flask**: Framework web untuk membangun aplikasi.
-   **Frontend**:
    -   **HTML5**: Struktur halaman web.
    -   **Jinja2**: Template engine dari Flask untuk menyisipkan logika di HTML.
    -   **CSS3**: Styling kustom untuk mempercantik tampilan.
    -   **Bootstrap 5**: Framework CSS untuk komponen UI dan desain responsif.
    -   **jQuery**: Digunakan untuk interaksi dinamis di sisi klien dan integrasi (AJAX) ke backend Flask.
-   **Database**:
    -   SQLite / MySQL

## ⚙️ Instalasi dan Menjalankan Proyek

Ikuti langkah-langkah berikut untuk menjalankan proyek ini di lingkungan lokal Anda.

**Prasyarat:**
-   Python 3.x
-   Pip (Package Installer for Python)

**Langkah-langkah:**

1.  **Clone repositori ini:**
    ```bash
    git clone https://github.com/MuhamadMudrikaRidho/web_chicken_yaska.git
    ```

2.  **Masuk ke direktori proyek:**
    ```bash
    cd web_chicken_yaska
    ```

3.  **Buat dan aktifkan virtual environment:**
    -   **Windows:**
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```
    -   **macOS / Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

4.  **Install semua dependensi yang dibutuhkan:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Buat file Upload di static/**

6.  **Jalankan Factory:**
    ```bash
    python user-factory.py

    python menu-factory.py
    ```

7.  **Jalankan aplikasi Flask:**
    ```bash
    python app.py
    ```

8.  Buka browser Anda dan kunjungi `http://127.0.0.1:5000`.

## 📄 Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT. Lihat file `LICENSE` untuk detail lebih lanjut.
## 🙏 Ucapan Terima Kasih

-   Program **Studi Independen Bersertifikat (MSIB)** dari Kampus Merdeka.
-   Mitra **Learning X** sebagai penyelenggara program.
-   Seluruh mentor dan rekan-rekan yang telah memberikan dukungan.