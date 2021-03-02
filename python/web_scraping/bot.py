from bs4 import BeautifulSoup
import requests

source = requests.get("https://ruizsamuel.es/").text

soup = BeautifulSoup(source, 'lxml')

contents = soup.find('div', class_="container has-text-centered")
headline = contents.find('h1', class_="bold-title fade-in one").text.strip()
description = contents.find('div', class_="subtitle is-3 fade-in two").p.text
icons = contents.find('div', class_="social-icons")


engLink = []
engZone = soup.find('div', class_="navbar-menu has-content-centered")
for link in engZone.find_all('a'):
    engLink.append(link.get('href'))

links = []
for link in icons.find_all('a'):
    links.append(link.get('href'))


#print(contents.prettify())
print(headline)
print(description)
print(links)
print(engLink)
