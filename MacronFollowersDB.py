import requests
from lxml import html
pagestring = requests.get('https://twitter.com/emmanuelmacron')
htmlpage = html.fromstring(pagestring.content)

#Find class a with attribute 'followers' and access its number
fllw = htmlpage.xpath("//a[@data-nav='followers']/span/@data-count")
print(fllw[0])


