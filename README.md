# Priyom Scraper
This tool scrapes data off of the Priyom Numbers
station schedule page and returns it in a list to be processed
by a computer

### Usage
```python
import priyomScrape as ps

scraper = ps.PriyomScrape()

nextStation = scraper.getNextStation()
#Example of data returned in "nextStation":  [{'stationID': 'V13', 'frequency': '9276kHz ', 'mode:': 'USB/AM', 'addInfo': '(May not always transmit) [Target: East Asia]', 'href': 'http://s.printf.cc/#a/9276usb'}, {'TTN': '44'}]
print(nextStation)

stationSchedule = scraper.getSchedule()
#Example of data returned in "stationSchedule": [('00:00', 'V13', '11430kHz\n18040kHz', 'USB/AM', '(May not always transmit) [Target: East Asia]'), ('01:00', 'V13', '13974kHz', 'USB/AM', '(May not always transmit) [Target: East Asia]'), ...]
print(stationSchedule)
```

#### Licence information
None of the information returned by this tool is owned by me, I do not claim to own it, and priyom.org do not endorse my tool.
the data this tool returns is 
the property of (priyom.org)[priyom.org] and is distributed under
the Attribution-NonCommercial-ShareAlike 4.0 International licence
which can be found here https://creativecommons.org/licenses/by-nc-sa/4.0/

#### Thanks
Special thanks to the people at priyom.org that make research into topics like this possible
Thank you for the data you provide that helps us monitor and research the things that interest us
