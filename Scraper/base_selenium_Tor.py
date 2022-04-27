from selenium import webdriver
from pathlib import Path
import os
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import time
from selenium.webdriver.common.keys import Keys
import platform

mySystem = platform.system() # you can replace with Linux, Darwin,Windows

# check the system
if mySystem == 'Linux':

  mySystem = 'clear'
  way = Path('./geckodriver-v0.26.0-linux64') # path to the file
  geckoFile = way / 'geckodriver' # way to geckodriver

elif mySystem == 'Windows':

  mySystem = 'cls'
  way = Path('geckodriver/windows') # path to the file
  geckoFile = way / 'geckodriver.exe' # way to geckodriver

elif mySystem == 'Darwin':
  mySystem = 'clear'
  #way = Path('./geckodriver-v0.28.0-macos') # path to the file
  geckoFile = '/usr/local/bin/geckodriver' # way to geckodriver




way2 = Path('./tor-browser-linux64-10.5.6_en-US/tor-browser_en-US/Browser/TorBrowser/Data/Browser/profile.default')

profile = FirefoxProfile(way2)
profile.set_preference('network.proxy.type', 1)
profile.set_preference("network.proxy.socks_version", 5)
profile.set_preference('network.proxy.socks', '127.0.0.1')
profile.set_preference('network.proxy.socks_port', 9050)
profile.set_preference("network.proxy.socks_remote_dns", True)
profile.update_preferences()


torexe = os.popen(r'./tor-browser-linux64-10.5.6_en-US/tor-browser_en-US/Browser/TorBrowser/Tor/tor')
#PROXY = "socks5://localhost:9050" # IP:PORT or HOST:PORT

driver = webdriver.Firefox(executable_path=f'{geckoFile}', firefox_profile= profile)
driver.get("https://www.torproject.org/download/")

