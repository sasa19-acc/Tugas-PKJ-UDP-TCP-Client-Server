# 🟦 Implementasi TCP Client-Server || Panduan Konfigurasi

> [!NOTE]
> ## ❕ Pemberitahuan  
> Dokumentasi ini disusun mengacu pada materi pembelajaran dan video tutorial yang telah disediakan oleh dosen pengampu.  
> Konten original dari video tersebut sepenuhnya merupakan hak cipta pemiliknya yang sah.  
> 
> 🔗 **Sumber Referensi:**  
> <div align="center">
>
> <a href="https://www.youtube.com/watch?v=GlVfVn17_ug">
>   <img src="https://img.youtube.com/vi/GlVfVn17_ug/0.jpg" width="270">
> </a>
>
> </div>

Bila Anda ingin mencoba implementasi *source code* secara langsung, ikuti tahapan berikut:

**📎 Mengunduh Repository**

Pastikan `git` telah terinstall pada sistem Anda. Eksekusi perintah ini di terminal:

```bash
git clone https://github.com/RockHead07/UDP-TCP-Client-Server.git
```

Selanjutnya, navigasi ke direktori TCP:

```bash
cd UDP-TCP-Client-Server/TCP\ Client\ Server
```

### 📂 Organisasi File

```arduino
TCP Client Server/
├── tcpServer.py
├── tcpClient.py
└── README.md
```

### ⚙️ Persyaratan Sistem

Pastikan sistem Anda memiliki:
- Instalasi `Python 3.x` atau versi terbaru.
- Akses ke Terminal atau Command Prompt.
- (Opsional) Text editor atau IDE seperti VS Code untuk menulis kode `Python`.

Verifikasi instalasi `Python` dengan menjalankan perintah berikut di terminal:

```bash
python --version
py --version
```

Jika sistem menampilkan versi `Python` yang terinstall, maka Python sudah siap digunakan.

### Konfigurasi TCP Server

Tahap awal adalah membuat dan mengaktifkan *TCP Server*. Tidak seperti *UDP*, protokol *TCP* menggunakan mekanisme *connection-oriented*, yang mengharuskan *client* melakukan *handshake* sebelum transmisi data dimulai.

Berikut implementasi ***TCP Server***:

```Python
import socket  # Import modul socket untuk komunikasi network

# Validasi eksekusi langsung (bukan sebagai modul import)
if __name__ == "__main__":
    ip = "127.0.0.1"       # Alamat IP server (localhost)
    port = 12345           # Port yang digunakan untuk listening

    # Inisialisasi socket TCP (SOCK_STREAM menunjukkan protokol TCP)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Binding server ke alamat IP dan port yang ditentukan
    server.bind((ip, port))

    # Aktivasi server untuk menerima koneksi
    # Parameter 5 menentukan maksimal koneksi dalam queue
    server.listen(5)

    # Loop server untuk menangani koneksi client secara berkelanjutan
    while True:
        # Accept koneksi masuk dari client
        client, address = server.accept()

        # Tampilkan informasi client yang terkoneksi
        print(f"Connection from {address[0]}:{address[1]} has been established!")

        # Terima data dari client (buffer maksimal 1024 bytes)
        string = client.recv(1024)
        
        # Konversi data dari bytes ke format string UTF-8
        string = string.decode("utf-8")
        
        # Transformasi pesan ke huruf kapital
        string = string.upper()

        # Kirim balasan ke client dalam format bytes
        client.send(bytes(string, 'utf-8'))

        # Tutup koneksi dengan client
        client.close()
```

Untuk menjalankan program server, buka terminal di direktori proyek, kemudian eksekusi:

```bash
python tcpServer.py
```

*Server* akan berstatus aktif dan siap menerima koneksi dari *Client*.

### Konfigurasi TCP Client

Setelah ***TCP Server*** beroperasi, langkah berikutnya adalah mengembangkan aplikasi *client* untuk mengirim pesan dan menerima respon dari *server*.

Berikut implementasi ***TCP Client***:

```python
import socket  # Import library socket untuk komunikasi jaringan

# Validasi eksekusi langsung
if __name__ == "__main__":
    ip = "127.0.0.1"     # Alamat IP server target (localhost)
    port = 12345         # Port server yang dituju

    # Inisialisasi socket TCP (SOCK_STREAM = protokol TCP)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Establish koneksi ke server menggunakan IP dan port
    server.connect((ip, port))
    
    # Request input pesan dari user
    string = input("Enter a message to send to the server: ")

    # Transmisi pesan ke server dalam format bytes
    server.send(bytes(string, 'utf-8'))

    # Terima response dari server (buffer 1024 bytes)
    buffer = server.recv(1024)

    # Decode data bytes ke string UTF-8
    buffer = buffer.decode("utf-8")

    # Display response dari server
    print(f"Server response: {buffer}")
```

Setelah kode client siap, jalankan client dengan membuka terminal baru (*jangan tutup terminal server*), lalu eksekusi:

```bash
python tcpClient.py
```

Bila konfigurasi benar, *client* akan meminta input pesan dari user, kemudian server akan mengembalikan versi kapitalisasi lengkap / **UPPERCASE** dari pesan tersebut.

### 📤 Hasil Eksekusi

Berikut contoh *output* ketika aplikasi dijalankan:

#### Output Terminal Server

```bash
Connection from 127.0.0.1:63789 has been established!
```

#### Output Terminal Client

Ketika melakukan *input* pesan seperti contoh di bawah, server akan merespons dengan versi huruf kapital:

```bash
Enter a message to send to the server: Indonesia
Server response: INDONESIA
```

# ✨ Ringkasan

Berdasarkan implementasi *TCP Client-Server* ini, dapat disimpulkan bahwa komunikasi menggunakan protokol *TCP* beroperasi dengan prinsip *connection-oriented*, dimana sebelum transmisi data berlangsung, *client* wajib membangun koneksi terlebih dahulu (*three-way handshake*) dengan server.

Karakteristik ini menjadikan ***TCP*** lebih terpercaya (*reliable*) dibandingkan ***UDP***, karena setiap paket data dijamin terkirim dengan urutan yang tepat. Server menerima pesan dari *client*, melakukan pemrosesan (konversi ke huruf kapital), lalu mengirimkan hasilnya kembali ke client sebelum mengakhiri koneksi.
