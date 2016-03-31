# -*- coding: utf-8 -*-
import sys
from datetime import datetime
from splinter import Browser
import time
import urllib
from bs4 import BeautifulSoup
import scraperwiki


reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')


def get_browse_soup(browser):
    html = browser.html
    soup = BeautifulSoup(html, "lxml")
    return soup


def browse(url):                                                                                            # loads all tenders
    browser = Browser("phantomjs", service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])
    browser.visit(url)
    return browser

def get_file(url):
    browser = browse(url)
    soup = get_browse_soup(browser)
    print soup.prettify()
    browser.click_link_by_href('#fh')
    #file = soup.find('div', id="legend-wrapper").find('a', text='Exportar Lista en Excel')['href']
    file = ''
    print file
    return  file


if __name__ == '__main__':

    todays_date = str(datetime.now())
    portal = 'https://compranet.funcionpublica.gob.mx/esop/toolkit/opportunity/opportunityList.do'

    tender_xls = get_file(portal)