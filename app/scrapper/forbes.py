import requests
from bs4 import BeautifulSoup
import csv

def run():
    response = requests.get('https://www.forbes.com/money/')
    soup = BeautifulSoup(response.text, 'html.parser')

    forbes_list = []
    for item in soup.find_all('h2', class_='u00AMdzw'):
        forbes_list.append(item.text)
    
    with open('forbes.csv', 'w') as file:
        writer = csv.writer(file)
        for title in forbes_list:
            writer.writerow([title])


if __name__ == '__main__':
    run()
