from selenium import webdriver
import re

class PriyomScrape(object):
    nextTrafficPattern = "(.+?) ((?:\\d+?kHz ?)+)([A-Z]+/?[A-Z]+) ?(.*)?"
    schedulePattern = "(\\d+:\\d+)\\n(.+)\\n((?:\\d+?kHz\n?)+)\\n([A-Z]+/?[A-Z]+)\\n?(.*)?"
    driver = webdriver.PhantomJS()
    url = "http://priyom.org/number-stations/station-schedule"

    def getSchedule(self):
        self.driver.get(self.url)
        calCont = self.driver.find_element_by_id("calendar-container")
        calBody = calCont.find_element_by_class_name("calendar-body")
        calDay = calBody.find_element_by_class_name("calendar-day")
        calenderItems = calDay.find_elements_by_xpath("./div")
        calenderItems.pop(0)
        output = []
        for item in calenderItems:
            match = re.findall(self.schedulePattern,item.text)
            output.append(match[0])
        return output

    def getNextStation(self):
        output = []
        self.driver.get(self.url)
        nextEvent = self.driver.find_element_by_id("events")

        timeTilNEven = nextEvent.find_element_by_xpath("./h3").text.split(" ")[3]
        if timeTilNEven == "a":
            ttn = "0"
        else:
            ttn = timeTilNEven

        detail = nextEvent.find_elements_by_tag_name("li")

        for item in detail:
            text = item.text
            match = re.findall(self.nextTrafficPattern,text)
            match = match[0]
            atag = item.find_element_by_xpath("./a")
            print(atag.get_attribute("href"))
            output.append({"stationID":match[0],"frequency":match[1],"mode:":match[2],"addInfo":match[3],"href":atag.get_attribute("href")})


        output.append({"TTN": ttn})
        return output