import requests
import sys
from pprint import pprint
from collections import Counter

class GitHubUser:

    def __init__(self, username):

        self.username = username
        self.repos = self.user['public_repos']
        self.repos_url = requests.get(self.user['repos_url']).json()
        self.user = requests.get(f'https://api.github.com/users/{self.username}').json()
        self.followers = self.user['followers']

    def get_rep(self):
        return {repo['name']: repo['description'] for repo in self.repos_url}

    def get_lang(self):

        langs = Counter()
        for repo in self.repos_url:
            langs.update([repo['language']])
        return {l: rs for l, rs in langs.most_common()}

    def find_tops(users):

        max_repos = None
        max_followers = None
        langs = Counter()

        for i in users:
            user = GitHubUser(i)
            if max_repos is None or user.repos > max_repos[1]:
                max_repos = (user.username, user.repos)
            if max_followers is None or user.followers > max_followers[1]:
                max_followers = (user.username, user.followers)
            langs.update(user.get_lang())
        max_lang = langs.most_common()[0]

        print(f'\nСамое большое количество репозиториев: {max_repos}')
        print(f'Язык, наиболее популярный среди пользователей: {max_lang}')
        print(f'Самое большое количество followers: {max_followers}')

    def find_user(users):

        for i in users:
            print(users.index(i) + 1, i)
        n = int(input('Введите номер пользователя: '))
        username = users[n-1]
        user = GitHubUser(username)
        print('\nРепозиторий: описание')
        pprint(user.get_repo())
        print('\nЯзыки: количество')
        pprint(user.get_lang())

    def main():
        users = sys.argv[1:]
        find_user(users)
        find_tops(users)

if __name__ == '__main__':
    main()
