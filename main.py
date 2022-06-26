# Copyright(c)2022 vishal ahirwar.
from bs4 import BeautifulSoup as soup
import requests  # to fetch html data from live website
print("Scraping data ...")
res = requests.get(
    url="https://nexttechnology.io/top-10-programming-languages-for-2022/")
html_data = res.text  # content of the response in unicode:str
# making soup i mean BeautifulSoup object
html = soup(html_data, "html.parser")
# filtering h2 from html data[returns list]
top_10_programming_lang = html.find_all(name="h2")

print("Top 10 Programming languages:")

for lang in top_10_programming_lang:
    print(lang.getText())
