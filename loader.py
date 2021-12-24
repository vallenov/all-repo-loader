import requests
from bs4 import BeautifulSoup
import os
import configparser
import argparse

config = configparser.ConfigParser()
config.read('load.ini')

parser = argparse.ArgumentParser(description="Clone repos from Github")
parser.add_argument("-u", dest="username", required=True, type=str)
parser.add_argument("-p", dest="path", required=True, type=str)
args = parser.parse_args()


def get_name_of_repo() -> list:
    resp = []
    username = config['MAIN']['username']
    soup = BeautifulSoup(requests.get(f'https://github.com/{args.username}?tab=repositories').text, 'lxml')
    div = soup.find('div', id='user-repositories-list')
    name = div.find_all('a')
    for n in name:
        resp.append(n.get('href'))
    return resp


def main():
    list_of_repo = get_name_of_repo()
    os.chdir(args.path)
    for repo in list_of_repo:
        print(f'Cloning https://github.com{repo}')
        os.system(f'git clone https://github.com{repo}')


if __name__ == '__main__':
    main()
