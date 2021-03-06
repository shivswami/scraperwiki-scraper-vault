import scraperwiki
from bs4 import BeautifulSoup

import string

html = scraperwiki.scrape("http://www.usatoday.com/sports/mlb/statistics/")
soup = BeautifulSoup(html)

tables = soup.find_all("table")
print len(tables)

for table in tables:
    print table.attrs

## if your page has tons of tables, you might need to get more specific
## with a find all like: 
## tables = soup.find_all("table", {"border" : "0", "cellspacing": "1", "cellpadding": "2"})


def scrape_table(table):
    rows = table.find_all('tr') 
    for row in rows:
        headers = row.find_all("th")
        for c,cell in enumerate(headers):
            print c, cell.get_text()
        cells = row.find_all("td")
        for c,cell in enumerate(cells):
            print c, cell.get_text()

        data = {
            'team'         : headers[0].get_text().strip(),
            'RK'     : cells[0].get_text().strip(), 
            'W'         : cells[1].get_text().strip(),
            'L' : cells[2].get_text().strip(),
            'ERA'       : cells[3].get_text().strip(),
            'S3' : cells[4].get_text().strip()
        }
        scraperwiki.sqlite.save(unique_keys=['team'],data=data)
  
    print "et voila!"

scrape_table(tables[1])
import scraperwiki
from bs4 import BeautifulSoup

import string

html = scraperwiki.scrape("http://www.usatoday.com/sports/mlb/statistics/")
soup = BeautifulSoup(html)

tables = soup.find_all("table")
print len(tables)

for table in tables:
    print table.attrs

## if your page has tons of tables, you might need to get more specific
## with a find all like: 
## tables = soup.find_all("table", {"border" : "0", "cellspacing": "1", "cellpadding": "2"})


def scrape_table(table):
    rows = table.find_all('tr') 
    for row in rows:
        headers = row.find_all("th")
        for c,cell in enumerate(headers):
            print c, cell.get_text()
        cells = row.find_all("td")
        for c,cell in enumerate(cells):
            print c, cell.get_text()

        data = {
            'team'         : headers[0].get_text().strip(),
            'RK'     : cells[0].get_text().strip(), 
            'W'         : cells[1].get_text().strip(),
            'L' : cells[2].get_text().strip(),
            'ERA'       : cells[3].get_text().strip(),
            'S3' : cells[4].get_text().strip()
        }
        scraperwiki.sqlite.save(unique_keys=['team'],data=data)
  
    print "et voila!"

scrape_table(tables[1])
