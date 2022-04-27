from selenium import webdriver
from pathlib import Path
import os
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.common.keys import Keys

#insert path geckodriver
geckoFile = './torScraper/gecko/geckodriver' # way to geckodriver

#insert path TorBrowser
way2 = Path('./tor-browser-linux64-10.5.6_en-US/tor-browser_en-US/Browser/TorBrowser/Data/Browser/profile.default')

profile = FirefoxProfile(way2)
profile.set_preference('network.proxy.type', 1)
profile.set_preference("network.proxy.socks_version", 5)
profile.set_preference('network.proxy.socks', '127.0.0.1')
profile.set_preference('network.proxy.socks_port', 9050)
profile.set_preference("network.proxy.socks_remote_dns", True)
profile.update_preferences()

#insert path exe TorBrowser
torexe = os.popen(r'./tor-browser-linux64-10.5.6_en-US/tor-browser_en-US/Browser/TorBrowser/Tor/tor')
#PROXY = "socks5://localhost:9050" # IP:PORT or HOST:PORT




T = """
   ____       ___  ____ ___ _   _ _____ 
  / ___|     / _ \/ ___|_ _| \ | |_   _|
 | |   _____| | | \___ \| ||  \| | | |  
 | |__|_____| |_| |___) | || |\  | | |  
  \____|     \___/|____/___|_| \_| |_|  
                                                     
    """
print(T)



#take in input txt list of .onion url
def scrape(file_url):
    numEX = 0
    i=0
    with open(file_url) as f:
        lines = f.readlines()

    driver = webdriver.Firefox(executable_path=f'{geckoFile}', firefox_profile= profile)
    list_buoni = []
    for el in lines:
        el = el.replace('\n','')
        el = el.split('.onion/')[0]
        el = el+'.onion'
        #test = el.split('/')[2]+'.txt'
        print(el)

        #set timeout
        driver.set_page_load_timeout(45)
        try:
            driver.get(el)
            time.sleep(5)
            name = str(el).replace('\n','').replace('https://','').replace('http://','').replace('onion/','onion').replace('ly/','ly')
            text = driver.page_source
            # writes in txt file page surce
            f=open("./scraped/" +  name + ".txt","w")
            f.write(text)
            f.close()
        #if there il an Exception  it writes None value on txt file
        except TimeoutException as e:
            name = str(el).replace('\n','').replace('http://','').replace('onion/','onion').replace('ly/','ly')
            text = 'None'
            f=open("./scraped/none/" +  name + ".txt","w")
            f.write(text)
            f.close()

#extracts all '.onion' type urls from the page taken as input
def crawler_onion(url):

    driver = webdriver.Firefox(executable_path=f'{geckoFile}', firefox_profile= profile)

    driver.get(url)
    elems = driver.find_elements_by_xpath("//a[@href]")

    list_url = []

    for elem in elems:
        site = elem.get_attribute("href")
        if '.onion' in site:
            if 'advertise' not in site and 'upload' not in site and '/search' not in site:
                if site not in list_url:
                    list_url.append(site)
    print(list_url)
    return list_url



#take in input an url and extracts all '.onion' type urls from the page taken as input by pre-cleaning unsuitable urls
def scrawler_onion_link_di_link(url):

    driver = webdriver.Firefox(executable_path=f'{geckoFile}', firefox_profile= profile)

    print('start')
    driver.get(url)
    elems = driver.find_elements_by_xpath("//a[@href]")

    url = url.split('.onion/')[0]
    url = url+'.onion/'

    list_url = []

    for elem in elems:
        site = elem.get_attribute("href")
        if '.onion/' in site:
            site = site.split('.onion/')[0]
            site = site+'.onion/'
            if site not in url:
                if 'advertise' not in site and 'upload' not in site and '/search' not in site:
                    ok = site+"--"+url
                f=open("./list1.txt","a")
                f.write(ok+'\n')
                f.close()



