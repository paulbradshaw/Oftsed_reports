#import the libraries we'll need
import re
import scraperwiki
import urllib2
import lxml.etree
import lxml.html

# Read in a page
#html = scraperwiki.scrape("https://reports.ofsted.gov.uk/provider/files/2631211/urn/103980.pdf")
url = "https://reports.ofsted.gov.uk/provider/files/2631211/urn/103980.pdf"

#This function will contain all the lines below, later
#def scrapepdf(url):

pdfdata = urllib2.urlopen(url).read()
print "The pdf file has %d bytes" % len(pdfdata)

xmldata = scraperwiki.pdftoxml(pdfdata)
print "After converting to xml it has %d bytes" % len(xmldata)
print "The first 2000 characters are: ", xmldata[:2000]


# turn 'xmldata' into an lxml object called 'pdfroot'
pdfroot = lxml.etree.fromstring(xmldata)
#find all <text> tags and put in list variable 'lines'
lines = pdfroot.findall('.//text')
# create new 'linenummber' variable, set at 0
linenumber = 0
# create empty dictionary object which we'll fill with data as we go, then store
record = {}
#loop through each item in 'lines'
for line in lines:
  linenumber = linenumber+1
  #we are not interested in lines that are empty, so this if test ensures the line after only runs if it's not empty
  if line.text is not None:
    #use regex to look for any or no character(s) followed by the string 'incident'
    #followed by any or no character(s) - the result is stored in 'mention'
    mention = re.match(r'.*incident*', line.text)
    #if mention exists (there was a match, and it was created)
    if mention:
      print line.text


