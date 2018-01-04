import requests
from lxml import html
website = requests.get('https://twitter.com/emmanuelmacron')
htmlpage = html.fromstring(website.content)

#Find class a with attribute 'followers' and access its number
fllw = htmlpage.xpath("//a[@data-nav='followers']/span/@data-count")
print(fllw[0]) 


