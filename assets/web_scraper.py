import requests
from bs4 import BeautifulSoup

def fetch_web_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup.get_text()
        else:
            return f"Gagal mengakses url: {url}. Kode status: {response.status_code}"
    except Exception as e:
        return f"Terjadi kesalahan: {str(e)}"