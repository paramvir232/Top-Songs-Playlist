from bs4 import BeautifulSoup
import requests

date = input("Which year you would like to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(url='https://www.billboard.com/charts/hot-100',params=date)
html_file = response.text

print(html_file)