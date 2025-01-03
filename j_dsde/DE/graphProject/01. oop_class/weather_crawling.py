from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

year, month = 2024, 11
def get_html(year, month):
    url = f'https://www.weather.go.kr/w/observation/land/past-obs/obs-by-day.do?stn=108&yy={year}&mm={month}&obs=1'
    html = urlopen(url)
    bs_obj = BeautifulSoup(html, "html.parser")
    return bs_obj



date_line = []
data_line = []
for td in bs_obj.find_all("td"):
    if td.text == '\n\xa0\n':
        pass
    else :
        table_line.append(td.text)
print(table_line)