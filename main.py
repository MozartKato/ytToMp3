import os
import yt_dlp

def download_youtube_audio(url, file_name):
    # Opsi untuk mengunduh hanya audio dalam format MP3
    ydl_opts = {
        'format': 'bestaudio/best',
        'extractaudio': True,  # Hanya ambil audio
        'audioformat': 'mp3',  # Format audio yang diinginkan
        'outtmpl': f'downloads/{file_name}.%(ext)s',  # Menyimpan ke folder 'downloads' dengan nama file yang ditentukan
        'postprocessors': [{  # Mengonversi ke MP3
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',  # Kualitas MP3
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f'Mengunduh: {url}')
            ydl.download([url])
            print(f'Berhasil mengunduh audio sebagai MP3: {file_name}.mp3')
    except Exception as e:
        print(f'Terjadi kesalahan: {str(e)}')

if __name__ == '__main__':
    # Meminta input dari pengguna
    url = input("Masukkan URL Video YouTube: ")
    file_name = input("Masukkan nama file untuk disimpan (tanpa ekstensi): ")
    
    # Pastikan folder downloads ada
    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    download_youtube_audio(url, file_name)
