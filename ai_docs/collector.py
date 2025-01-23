import requests
from bs4 import BeautifulSoup

def collect_content(url, output_path):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raises HTTPError for bad responses

    soup = BeautifulSoup(response.content, 'html.parser')
    content = soup.get_text()

    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(content)
