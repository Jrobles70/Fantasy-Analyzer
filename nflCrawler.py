from selenium import webdriver
from time import sleep
from manageDb import DbManager

class NFlCrawler(DbManager):
    def __init__(self):
        DbManager.__init__(self)
        # Connects to a website that generates random sentences
        self.driver = webdriver.PhantomJS("./phantomjs")

    def getInfo(self):
        '''
        list of elements holds tables which are in the following order:
        class=data-table1
        1: Qbs
        2: Rbs
        3: Wrs
        4: Kickers
        6: Punt Return
        7: Kick Return
        '''
        print 'Getting teams'
        teams = self.readTeams()
        print 'Got teams'
        for team, abbr, ID in teams:
            print 'Starting'
            team = team.replace(" ", "")
            self.driver.get('http://www.nfl.com/teams/{}/statistics?team={}'.format(team, abbr))
            data_els = self.driver.find_elements_by_class_name('data-table1')
            self.getQbStats(data_els)
            self.getRbStats(data_els)
            self.getWrStats(data_els)
            self.getKickerStats(data_els)
            self.getDstStats(data_els)

    def getQbStats(self, elementList):
        pass

    def getRbStats(self, elementList):
        pass

    def getWrStats(self, elementList):
        pass

    def getKickerStats(self, elementList):
        pass

    def getDstStats(self, elementList):
        pass


    def finish(self):
        # Closes users driver
        self.driver.quit()

if __name__ == "__main__":
    test = NFlCrawler()
    test.getInfo()

