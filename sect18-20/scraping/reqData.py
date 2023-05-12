import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.body)
# print(soup.body.div) # got first one
# print(soup.find_all('div'))
# print(soup.find('a'))
# print(soup.select('.titleline')[1])
links = soup.select('.titleline')
votes = soup.select('.score')


# print(votes[0].get('id'))

def create_custom_hn(links, votes):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        hn.append({'title'})
    return hn


print(create_custom_hn(links, votes))
