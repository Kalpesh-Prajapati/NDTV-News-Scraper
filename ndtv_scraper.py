import requests
from bs4 import BeautifulSoup
import html  # For unescaping HTML entities
import csv

url = "https://www.ndtv.com/latest#pfrom=home-ndtv_mainnavigation"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

news_data = []
ul_data = soup.find('ul', attrs={'class': 'NwsLstPg_ul'})

if ul_data:
    for row in ul_data.find_all('li', attrs={'class': 'NwsLstPg-a-li'}):
        quote = {}

        date_span = row.find('span')
        title_link = row.find('a',attrs={"class":"NwsLstPg_pst_lnk"})
        image = row.find('img')
        data = row.find("p")

        date_time = date_span.text.strip() if date_span else "N/A"
        author = title_link.text.strip() if title_link else "N/A"
        title = html.unescape(image['alt'].strip()) if image and 'alt' in image.attrs else "N/A"
        img_url = image['src'] if image and 'src' in image.attrs else "N/A"
        details = data.text.strip() if data else "N/A"

        # Skip clearly invalid entries
        if title == "N/A" and img_url == "N/A":
            continue

        quote['Date_Time'] = date_time
        quote['Author'] = author
        quote['Title'] = title
        quote['Image'] = img_url
        quote['Detail'] = details

        news_data.append(quote)

    filename = 'news.csv'
    with open(filename, 'w', newline='') as f:
        w = csv.DictWriter(f,['Date_Time','Author','Title','Image','Detail'])
        w.writeheader()
        for quote in news_data:
            w.writerow(quote)
else:
    print("Could not find the news list container.")

