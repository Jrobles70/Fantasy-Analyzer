from config import CLOUDSQL_USER, CLOUDSQL_PASSWORD, CLOUDSQL_DATABASE
import MySQLdb


class DbManager:
    def __init__(self):
        try:
            self.db = MySQLdb.connect(host='127.0.0.1',
                                      db=CLOUDSQL_DATABASE,
                                      user=CLOUDSQL_USER,
                                      passwd=CLOUDSQL_PASSWORD,
                                      charset='utf8',
                                      port=3307)
        except Exception as e:
            print('Something went wrong connecting to Database')
            print(e)

    def createCursor(self):
        self.c = self.db.cursor()

    def closeCursor(self):
        self.db.commit()
        self.c.close()

    def createTable(self, info):
        '''
        :param info: Info should be the table name and columns
                     Ex. table(col1 INTEGER, col2 TEXT)
        :return:
        '''
        self.createCursor()
        try:
            self.c.execute("CREATE TABLE IF NOT EXISTS {}".format(info))
            print("{} successfully added to the database".format(info))
        except Exception as e:
            print("Something went wrong. \n {}".format(e))
        self.closeCursor()

    def addTeams(self):
        '''
        This is really only a one time use function. I needed to manually enter the team names and their abbreviations
        so I could efficiently get the team stats.
        '''
        self.createCursor()
        teams = [
                ("Seatle Seahawks", "SEA"),
                ("Arizona Cardinals", "ARI"),
                ("New Orleans Saints", "NO"),
                ("Buffalo Bills", "BUF"),
                ("Green Bay Packers", "GB"),
                ("Chicago Bears", "CHI"),
                ("Cleveland Browns", "CLE"),
                ("Detroit Lions", "DET"),
                ("Pittsburg Steelers", "PIT"),
                ("Indianapolis Colts", "IND"),
                ("Los Angeles Chargers", "LAC"),
                ("Jacksonville Jaguars", "JAX"),
                ("New York Jets", "NYJ"),
                ("Tampa Bay Buccaneers", "TB"),
                ("Cincinnati Bangels", "CIN"),
                ("Tennessee Titans", "TEN"),
                ("Minnesota Vikings", "MIN"),
                ("Washington Redskings", "WAS"),
                ("Houstan Texans", "HOU"),
                ("Los Angeles Rams", "LA"),
                ("Dallas Cowboys", "DAL"),
                ("New York Giants", "NYG"),
                ("San Francisco 49ers", "SF"),
                ("New England Patriots", "NE"),
                ("Denver Broncos", "Den"),
                ("Miami Dolphins", "MIA"),
                ("Carolina Panthers", "CAR"),
                ("Baltimore Ravens", "BAL"),
                ("Kansas City Cheifs", "KC"),
                ("Oakland Raiders", "OAK"),
                ("Philadelphia Eagles", "PHI"),
                ]
        self.c.execute("CREATE TABLE IF NOT EXISTS Teams(teamName TEXT, abbr TEXT, teamId INTEGER PRIMARY KEY)")
        #self.c.execute("CREATE TABLE IF NOT EXISTS Kickers("
        #               "nameId INTEGER FOREIGN KEY, "
        #               "week TEXT, "
        #               "blocked TEXT, "
        #               "fgAtt TEXT, "
        #               "fgMade TEXT, "
        #               "xpMade TEXT, "
        #               "xpAtt TEXT, "
        #               "1to19 TEXT, "
        #               "20to29 TEXT, "
        #               "30to39 TEXT, "
        #               "40to49 TEXT, "
        #               "over50 TEXT)")

        self.c.execute("CREATE TABLE IF NOT EXISTS Rush/Rec("
                       "nameId INTEGER FOREIGN KEY, "
                       "week TEXT, "
                       "rushAtt TEXT, "
                       "rushYrds TEXT, "
                       "rushTds TEXT, "
                       "targets TEXT, "
                       "rec TEXT, "
                       "recYrds TEXT, "
                       "recTds Text, "
                       "Fum TEXT, "
                       "FumLost TEXT"
                       ")")

        self.c.execute("CREATE TABLE IF NOT EXISTS Pass("
        "passAtt TEXT, "
        "passCom TEXT, "
        "passYrds TEXT, "
        "passTds TEXT, "
        "ints TEXT, "
        "sacks TEXT, "
        "Fum TEXT, "
        "FumLost TEXT)")

        #self.c.execute("CREATE TABLE IF NOT EXISTS Off(teamId INTEGER FOREIGN KEY, )")

        self.c.execute("CREATE TABLE IF NOT EXISTS Players(name TEXT, "
                       "teamId INTEGER FOREIGN KEY, "
                       "nameId INTEGER PRIMARY KEY, "
                       "depth TEXT)")

        self.c.execute("CREATE TABLE IF NOT EXISTS Schedule("
                       "teamId INTEGER FOREIGN KEY, "
                       "week1 TEXT, "
                       "week2 TEXT, "
                       "week3 TEXT, "
                       "week4 TEXT, "
                       "week5 TEXT, "
                       "week6 TEXT, "
                       "week7 TEXT, "
                       "week8 TEXT, "
                       "week9 TEXT, "
                       "week10 TEXT, "
                       "week11 TEXT, "
                       "week12 TEXT, "
                       "week13 TEXT, "
                       "week14 TEXT, "
                       "week15 TEXT, "
                       "week16 TEXT, "
                       "week17 TEXT "
                       ")")
        # TODO: self.c.execute("CREATE TABLE IF NOT EXISTS Weather()")


        ID = 0
        for teamName, abbr in teams:
            print 'adding {}'.format(teamName)
            self.c.execute("INSERT INTO Teams VALUES('{}','{}',{})".format(teamName, abbr, ID))
            ID += 1
        self.closeCursor()

    def addNew(self, name, numPos, stats, teadId):
        '''
        All stats include all players who have those stats along with others. For example, the rushing section has all
        players with rushing attempts as well as receiving (or passing if they are a qb) so I will have to check if
        the player has been added for their sections already.
        ie, If a Qb is entered then if we come across them again it will have to be under receiving yards
            If a Rb/Wr is entered then if we come across them again it will have to be under passing yards
        :param name:
        :param numPos:
        :param stats:
        :param teadId:
        :return:
        '''
        self.createCursor()
        self.c.execute("Select name FROM Players")
        players = self.c.fetchall()
        if name in players:
            print('not ready for this yet. Skipping...')
            return

        self.c.execute("INSERT INTO PLAYERS({}, {}, {} '--')".format(name, teamId, len(players)))

        if 'QB' in numPos:
            #TODO: add conditional to check if new stats are going to be entered if player is in db already
            pass
        else:
            # Else enter than as normal
            pass

        self.closeCursor()


    def readTeams(self):
        self.createCursor()
        self.c.execute("SELECT * from Teams")
        teams = self.c.fetchall()
        self.closeCursor()
        return teams


