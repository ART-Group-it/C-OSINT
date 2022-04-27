# C-OSINT

  <a href="https://github.com/SeleniumHQ/selenium">
      <img src="https://img.shields.io/badge/built%20with-Selenium-yellow.svg" />
    </a>
    <a href="https://www.python.org/">
    	<img src="https://img.shields.io/badge/built%20with-Python3-red.svg" />
    </a>

 <pre>

                            ░█████╗░░░░░░░░█████╗░░██████╗██╗███╗░░██╗████████╗
                            ██╔══██╗░░░░░░██╔══██╗██╔════╝██║████╗░██║╚══██╔══╝
                            ██║░░╚═╝█████╗██║░░██║╚█████╗░██║██╔██╗██║░░░██║░░░
                            ██║░░██╗╚════╝██║░░██║░╚═══██╗██║██║╚████║░░░██║░░░
                            ╚█████╔╝░░░░░░╚█████╔╝██████╔╝██║██║░╚███║░░░██║░░░
                            ░╚════╝░░░░░░░░╚════╝░╚═════╝░╚═╝╚═╝░░╚══╝░░░╚═╝░░░

                            COVID Open Source Intelligence Tool for the Dark Web

</pre>

## Basic Information:
C-OSINT is a python framework for extracting web pages (regular or onion) over the TOR network and the surface web.


- **Please note:** Crawling through the TOR network takes time. You can find more information [here](https://www.torproject.org/docs/faq.html.en#WhySlow). 

- **Warning:** Crawling is not illegal, but copyright infringement is. It's always best to double check a website's T&Cs before crawling it. Some websites set what is called robots.txt to tell the crawlers not to visit those pages. We always recommend complying with robots.txt.


## Logical Organization:
The framework is divided into three parts:
- Extractor and scraper [C-OSINT-e](https://github.com/ART-Group-it/C-OSINT/tree/main/Scraper);
- Cleaner and corpus constructor [C-OSINT-d] (https://github.com/ART-Group-it/C-OSINT/tree/main/Scraper);
- NLP based classifiers [C-OSINT-c] (https://github.com/ART-Group-it/C-OSINT/tree/main/Models);


