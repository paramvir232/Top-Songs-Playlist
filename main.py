from bs4 import BeautifulSoup
import requests

# date = input("Which year you would like to travel to? Type the date in this format YYYY-MM-DD: ")
date = '2020-10-09'

response = requests.get(url='https://www.billboard.com/charts/hot-100', params=date)
html_file = response.text

# print(html_file)

soup = BeautifulSoup(html_file, 'html.parser')
raw_title_list = soup.select('li #title-of-a-story')

final_title_list = [title.get_text().strip() for title in raw_title_list]

print(final_title_list)
