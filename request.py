from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://m.timesjobs.com/')
print(html_text)