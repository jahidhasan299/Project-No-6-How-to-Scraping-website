import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
res2 = requests.get('https://news.ycombinator.com/news?p=3')

soup = BeautifulSoup(res.text, "html.parser")
soup2 = BeautifulSoup(res2.text, "html.parser")
soup3 = BeautifulSoup(res2.text, "html.parser")


links = soup.select('.storylink') # we can use here all html tags
subtext = soup.select('.subtext')

links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')

links3 = soup2.select('.storylink')
subtext3 = soup2.select('.subtext')

merge_links = links + links2 + links3
merge_subtext = subtext + subtext2 + subtext3

def sort_stories_by_votes(hacknewslist):
    return sorted(hacknewslist, key=lambda key:key['votes'],reverse=True)

def create_custom_hacknews(links, subtext):
    hacknews = []
    for idx, item in enumerate(links):
        title = item.getText()
        href =  item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points',''))
            if points > 99:
                hacknews.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hacknews)

pprint.pprint(create_custom_hacknews(merge_links, merge_subtext))
