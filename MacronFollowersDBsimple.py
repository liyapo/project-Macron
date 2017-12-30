import requests
import time
from lxml import html
import psycopg2
#import sqlalchemy
from datetime import datetime

# get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(host="localhost",database="MacronFollowers", user="postgres", password="polska")
 
# conn.cur will return a cursor object, you can use this cursor to perform queries
cur = conn.cursor()
print("Connected to MacronFollowers database!")

# execute the INSERT statement
cur.execute("DROP TABLE IF EXISTS MacFol")
cur.execute("CREATE TABLE MacFol(NumConn INTEGER, DateTime TIMESTAMP WITH TIME ZONE, NumFol INTEGER)")

for i in range(20):
    website = requests.get('https://twitter.com/emmanuelmacron')
    htmlpage = html.fromstring(website.content)

    #Find class a with attribute 'followers' and access its number
    fllw = htmlpage.xpath("//a[@data-nav='followers']/span/@data-count")
    dt = datetime.now()
    cur.execute('INSERT INTO MacFol VALUES (%s,%s, %s)', (i+1, dt, fllw[0]))
    print(dt)
    print(fllw[0])
    time.sleep(5)

"""cur.execute("SELECT * FROM MacFol")
rows = cur.fetchall()

for row in rows:
    print(row)"""

# commit the changes to the database
conn.commit()
# close communication with the database
conn.close()







