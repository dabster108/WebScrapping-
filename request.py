from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://m.timesjobs.com/').text
soup = BeautifulSoup(html_text, "lxml")
jobs = soup.find_all('li', class_='ui-content search-result')

# Loop through job listings to extract company names
for job in jobs:
    company_name = job.find('h4', class_='srp-comp-name')
    if company_name:
        print(company_name.prettify())
