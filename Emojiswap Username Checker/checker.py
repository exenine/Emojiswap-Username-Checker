from colorama import Fore
import requests
userList = []
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Origin': 'https://emojimarket.wiki',
    'Connection': 'keep-alive',
    'Referer': 'https://emojimarket.wiki/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
}
print(f'[{Fore.BLUE}-{Fore.RESET}] Loading list of taken usernames')
response = requests.get('https://emojimarket.s3.us-west-2.amazonaws.com/emoji_database.json', headers=headers)
user = response.text.split('"@')
for x in user:
    x=x.split('"')
    if x[0] not in userList:
     userList.append(x[0].strip().strip('{').strip('\n'))
def check(user):
 if user not in userList:
  print(f'[{Fore.GREEN}+{Fore.RESET}] Not Taken: {Fore.GREEN}{user}{Fore.RESET}')
  with open('available.txt', 'a') as out:
    out.write(user + '\n')
 if user in userList:
    print(f'[{Fore.RED}-{Fore.RESET}] Taken: {Fore.RED}{user}{Fore.RESET}')

file = open('users.txt', 'r')
lines = file.readlines()

for index, line in enumerate(lines):
    check(line.strip())