import requests
from bs4 import BeautifulSoup
import os
import argparse
import subprocess as sp

parser = argparse.ArgumentParser(description="Clone repos from Github")
parser.add_argument("-u", dest="username", required=True, type=str)
parser.add_argument("-p", dest="path", required=True, type=str)
args = parser.parse_args()


def get_name_of_repo() -> list:
    resp = []
    soup = BeautifulSoup(requests.get(f'https://github.com/{args.username}?tab=repositories').text, 'lxml')
    div = soup.find('div', id='user-repositories-list')
    name = div.find_all('a')
    for n in name:
        if n.get('href').count('/') == 2:
            resp.append(os.path.basename(n.get('href')))
    return resp


def main():
    list_of_repo = get_name_of_repo()
    print(f'Finding repos: {list_of_repo}')
    os.chdir(args.path)
    list_of_exist_repo = list(map(lambda x: x.decode(), sp.check_output(f'ls').split()))
    cloning = 0
    already_cloning = 0
    for repo in list_of_repo:
        if repo in list_of_exist_repo:
            print(f'Repo {repo} already cloning')
            already_cloning += 1
            continue
        print(f'Cloning https://github.com/{args.username}/{repo}')
        os.system(f'git clone https://github.com/{args.username}/{repo}')
        cloning += 1
    print(f'Cloning: {cloning}, already_cloning: {already_cloning}')


if __name__ == '__main__':
    main()
