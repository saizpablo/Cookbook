from bs4 import BeautifulSoup
import requests
import csv

source = requests.get("http://www.japaneseverbconjugator.com/JVerbList.asp?level=Essential").text
soup = BeautifulSoup(source, 'lxml')
contents = soup.find('table', class_="table table-bordered table-striped")

csv_file = open('japverbs.csv', 'w', newline='',)
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Romaji', 'furigana', 'kanji', 'English', 'Type'])

for row in contents.find_all('tr'):
    try:
        rows = row.find_all('td')
        romaji = rows[0].text
        print(romaji)
        
        try:
            furigana = rows[1].find('span', class_="furigana").text
            kanji = rows[1].find('div', class_="JScript").text
        except:
            pass

        english = rows[2].text
        verbClass = rows[3].text
        csv_writer.writerow([romaji,english,furigana,kanji,verbClass])

    except:
        pass

csv_file.close()