###############################################################################
# Twitter scraper - designed to be forked and used for more interesting things
###############################################################################

import scraperwiki
import simplejson
import urllib2

# Change QUERY to your search term of choice.
# Examples: 'newsnight', 'from:bbcnewsnight', 'to:bbcnewsnight'
QUERY = '#wettendass'
RESULTS_PER_PAGE = '100'
LANGUAGE = ''
NUM_PAGES = 50
UNTIL = '2012-10-07'


for page in range(1, NUM_PAGES+1):
    base_url = 'http://search.twitter.com/search.json?q=%s&rpp=%s&lang=%s&page=%s&until=%s' \
         % (urllib2.quote(QUERY), RESULTS_PER_PAGE, LANGUAGE, page, UNTIL)
    try:
        results_json = simplejson.loads(scraperwiki.scrape(base_url))
        for result in results_json['results']:
            data = {}
            data['to_user'] = result['to_user']
            data['id'] = result['id']
            data['text'] = result['text']
            data['from_user'] = result['from_user']
            data['from_user_id'] = result['from_user_id']
            data['to_user_id'] = result['to_user_id']
            data['created_at'] = result['created_at']
            print data  ['created_at'], ['from_user'], ['from_user_id'], ['to_user'], ['to_user_id'], data['text']
            scraperwiki.sqlite.save(["id"], data)
    except:
        print 'Oh dear, failed to scrape %s' % base_url