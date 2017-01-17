#import the libraries we'll need
import re
import scraperwiki
import urllib2
import lxml.etree
import lxml.html

# Read in a page
#html = scraperwiki.scrape("https://reports.ofsted.gov.uk/provider/files/2631211/urn/103980.pdf")
url = "https://reports.ofsted.gov.uk/provider/files/2631211/urn/103980.pdf"
pdfdata = urllib2.urlopen(url).read()
print "The pdf file has %d bytes" % len(pdfdata)

xmldata = scraperwiki.pdftoxml(pdfdata)
print "After converting to xml it has %d bytes" % len(xmldata)
print "The first 2000 characters are: ", xmldata[:2000]

# turn html into an lxml object called 'root'
#root = lxml.html.fromstring(html)
#xmldata = scraperwiki.pdftoxml(pdfdata)
