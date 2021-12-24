import requests
from bs4 import BeautifulSoup
import os
import configparser

config = configparser.ConfigParser()
config.read('load.ini')


def get_name_of_repo() -> list:
    resp = []
    username = config.get("MAIN").get("username")
    soup = BeautifulSoup(requests.get(f'https://github.com/{username}?tab=repositories').text, 'lxml')
    div = soup.find('div', id='user-repositories-list')
    name = div.find_all('a')
    for n in name:
        resp.append(n.get('href'))
    return resp


def main():
    list_of_repo = get_name_of_repo()
    for repo in list_of_repo:
        os.system(f'git clone https://github.com{repo}')


if __name__ == '__main__':
    main()
