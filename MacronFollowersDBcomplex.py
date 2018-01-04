import requests
import time
from lxml import html
import psycopg2
#import sqlalchemy
from datetime import datetime
import matplotlib.pyplot as plt


def emfollowers():
    website = requests.get('https://twitter.com/emmanuelmacron')
    htmlpage = html.fromstring(website.content)

    # Find class 'a' with attribute 'followers' and access its number
    fllw = htmlpage.xpath("//a[@data-nav='followers']/span/@data-count")
    dt = datetime.now()
    cur.execute('INSERT INTO MacFolTw VALUES (%s, %s)', (dt, fllw[0]))
    print(dt)
    print(fllw[0])


def plotColData():

    # Get the data from the MacFolTw Table and plot it
    cur.execute("SELECT NumFol FROM MacFolTw")
    yy = cur.fetchall()
    lastyy = len(yy)
    xx = list(range(1, lastyy+1))

    ay1 = yy[0][0]
    ay2 = yy[lastyy-1][0]

    #print(xx)
    #print(yy)
    #print(lastyy)
    #print(ay1)
    #print(ay2)

    plt.plot(xx, yy, 'r*')
    plt.axis([0, lastyy + 1, ay1-50, ay2+50])
    plt.show()




# get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(host="localhost",database="MacronFollowers", user="postgres", password="polska")

# conn.cur will return a cursor object, you can use this cursor to perform queries
cur = conn.cursor()
print("Connected to MacronFollowers database!")

## execute the INSERT statement
cur.execute("DROP TABLE IF EXISTS MacFolTw")
cur.execute("CREATE TABLE MacFolTw(DateTime TIMESTAMP WITH TIME ZONE, NumFol INTEGER)")

try: 
    while True:
        emfollowers()
        time.sleep(300)
except KeyboardInterrupt:
    # Ctrl + C
    print('Manual break by user')
    plotColData()

# commit the changes to the database
conn.commit()
# close communication with the database
conn.close()







