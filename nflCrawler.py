from selenium import webdriver
from time import sleep
from manageDb import DbManager
from selenium.common.exceptions import NoSuchElementException

class NFlCrawler(DbManager):
    def __init__(self):
        DbManager.__init__(self)
        # Connects to a website that generates random sentences
        self.driver = webdriver.PhantomJS("./phantomjs")

    def setUp(self):
        '''
        This is another function that will only be used once. I need this to add all players initially and
        get all information up to this date.
        '''
        teams = self.readTeams()
        for team, abbr, ID in teams:
            print team
            print "-" * len(team)
            team = team.replace(" ", "")
            self.driver.get('http://www.nfl.com/teams/{}/statistics?team={}'.format(team, abbr))
            self.getPlayers()

    def getPlayers(self):
        # elementList[1] is all passing stats
        # //*[@id="team-stats-wrapper"]/table[2]/tbody/tr[3]/td[1], //*[@id="team-stats-wrapper"]/table[2]/tbody/tr[4]/td[1]
        elements_order = {
                          "PASSING STATS": 2,
                          "RUSHING STATS": 3,
                          "RECEIVING STATS": 4,
                          "FIELD GOAL STATS": 5,
                          "PUNT RETURN": 6,
                          "KICKOFF RETURN": 7
                          }
        for position in elements_order:
            print position
            print "-" * len(position)
            nextPlayer = True
            i = 3
            while nextPlayer:
                try:
                    player = self.driver.find_element_by_xpath('//*[@id="team-stats-wrapper"]/table[{}]/tbody/tr[{}]/td[1]/a'
                                                               .format(elements_order[position], i)).get_attribute("href")
                    print player
                    i += 1

                except NoSuchElementException:
                    # This is when there is no next player
                    nextPlayer = False

            print "---------------------------------------------------------------"


    def finish(self):
        # Closes users driver
        self.driver.quit()

if __name__ == "__main__":
    test = NFlCrawler()
    test.setUp()

