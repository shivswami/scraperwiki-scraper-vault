import scraperwiki

# Blank Python

html = scraperwiki.scrape("http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm")

import lxml.html           
root = lxml.html.fromstring(html)
for tr in root.cssselect("div[align='story_copy'] p"):
    tds = text.cssselect("p")
    if len(tds)==12:
        data = {
            'country' : tds[0].text_content(),
            'years_in_school' : int(tds[7].text_content())
        }
        scraperwiki.sqlite.save(unique_keys=['country'], data=data)import scraperwiki

# Blank Python

html = scraperwiki.scrape("http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm")

import lxml.html           
root = lxml.html.fromstring(html)
for tr in root.cssselect("div[align='story_copy'] p"):
    tds = text.cssselect("p")
    if len(tds)==12:
        data = {
            'country' : tds[0].text_content(),
            'years_in_school' : int(tds[7].text_content())
        }
        scraperwiki.sqlite.save(unique_keys=['country'], data=data)