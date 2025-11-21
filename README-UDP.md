# 🟩 Implementasi UDP Client-Server || Panduan Konfigurasi

> [!NOTE]
> ## ❕ Pemberitahuan  
> Dokumentasi ini disusun mengacu pada materi pembelajaran dan video tutorial yang telah disediakan oleh dosen pengampu.  
> Konten original dari video tersebut sepenuhnya merupakan hak cipta pemiliknya yang sah.  
> 
> 🔗 **Sumber Referensi:**  
> <div align="center">
>
> <a href="https://www.youtube.com/watch?v=bKfDS1lOSho">
>   <img src="https://img.youtube.com/vi/bKfDS1lOSho/0.jpg" width="270">
> </a>
>
> <a href="https://www.youtube.com/watch?v=i1AOd7AQcok">
>   <img src="https://img.youtube.com/vi/i1AOd7AQcok/0.jpg" width="270">
> </a>
>
> </div>

Bila Anda ingin mencoba implementasi *source code* secara langsung, ikuti tahapan berikut:

**📎 Mengunduh Repository**

Pastikan `git` telah terinstall pada sistem Anda. Eksekusi perintah ini di terminal:

```bash
git clone https://github.com/RockHead07/UDP-TCP-Client-Server.git
```

Selanjutnya, navigasi ke direktori UDP:

```bash
cd UDP-TCP-Client-Server/UDP\ Client\ Server
```

### 📂 Organisasi File

```arduino
UDP Client Server/
├── udpServer.py
├── udpClient.py
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

### Konfigurasi UDP Server

Tahap awal adalah mengembangkan server *UDP* sebelum mengoperasikan *client*. Server berfungsi untuk menerima pesan dari *client* dan memberikan respon balik.

Berikut implementasi ***UDP Server***:

```Python
import socket  # Import modul socket untuk komunikasi network

# Parameter konfigurasi server
localIP = "127.0.0.1"   # Alamat IP tempat server dijalankan (localhost)
localPort = 9997        # Port yang digunakan untuk listening
buffer = 1024           # Kapasitas maksimum data yang dapat diterima

# Inisialisasi socket UDP
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Binding socket ke IP dan port agar server siap menerima data
serverSocket.bind((localIP, localPort))  # Aktivasi server UDP

print("UDP server up and listening on")

# Loop berkelanjutan untuk mendengarkan pesan dari client
while True:
    data = serverSocket.recvfrom(buffer)  # Terima data dari client
    pesan = data[0]                       # Elemen pertama berisi pesan
    ip_address = data[1]                  # Elemen kedua berisi alamat (IP, port) client

    # Display pesan dan alamat client di terminal
    print("Pesan dari Client: \"{}\"".format(pesan))
    print("IP address Client: \"{}\"".format(ip_address))

    # Server mengirim balasan ke client
    serverSocket.sendto(b"Selamat datang di UDP Server", ip_address)
```

Untuk menjalankan program server, buka terminal di direktori proyek, kemudian eksekusi:

```bash
python udpServer.py
```

Server akan berstatus aktif dan menunggu pesan dari *client*.

### Konfigurasi UDP Client

Setelah ***UDP Server*** siap, selanjutnya adalah mengonfigurasi ***UDP Client***. *Client* bertugas mengirim pesan ke server dan menunggu balasan respon. Berikut implementasi kodenya:

```python
import socket  # Import library socket untuk komunikasi jaringan

# Konfigurasi target server
target_host = "127.0.0.1"   # Alamat IP server (localhost)
target_port = 9997          # Port server untuk komunikasi

# Inisialisasi socket UDP
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Transmisi data ke server (dalam format bytes)
client.sendto(b"Hello UDP Server", (target_host, target_port))

# Terima balasan dari server
data, address = client.recvfrom(4096)    # 4096 = kapasitas maksimum buffer penerimaan

# Display balasan server di terminal
print("Respon dari server: \"{}\"".format(data.decode()))

# Tutup koneksi socket client
client.close()
```

Setelah kode client siap, jalankan client dengan membuka terminal baru (*jangan tutup terminal server*), lalu eksekusi:

```bash
python udpClient.py
```

Bila konfigurasi benar, *client* akan mengirim pesan ke server, menerima respon, dan menampilkan hasilnya di terminal.

### 📤 Hasil Eksekusi

Berikut contoh *output* ketika aplikasi dijalankan:

#### Output Terminal Server

```bash
UDP server up and listening on
Pesan dari Client: "b'Hello UDP Server'"
IP address Client: "('127.0.0.1', 62341)"
```

#### Output Terminal Client

```bash
Respon dari server: "Selamat datang di UDP Server"
```

# ✨ Ringkasan

Berdasarkan implementasi *UDP Client-Server* ini, dapat disimpulkan bahwa komunikasi menggunakan protokol *UDP* beroperasi dengan prinsip *connectionless*, dimana *client* dapat langsung melakukan transmisi data ke server tanpa memerlukan proses *handshake* terlebih dahulu. Server hanya perlu melakukan listening pada IP dan port tertentu, kemudian menerima pesan dan mengirimkan balasannya.