import requests
from bs4 import BeautifulSoup
import re
from datetime import date

today = date.today()

result = requests.get('https://www.live-footballontv.com/chelsea-on-tv.html')

content = result.text

soup = BeautifulSoup(content, 'lxml')

# teams = soup.find_all(class_="fixture__teams")

teams = soup.find('div', class_='fixture').get_text(strip=True, separator=' ')

d1 = today.strftime("%A %w %B %Y")
# print(d1)

next_game = soup.find('div', class_='fixture-date').get_text()

next_game = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', next_game)

print(today.strftime("%A %w %B %Y"))
print(next_game)

if d1 == next_game:
    print('Not playing today')
else:
    print('success')
