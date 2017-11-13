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
        self.c.execute("CREATE TABLE IF NOT EXISTS Teams(teamName TEXT, abbr TEXT, teamID INTEGER PRIMARY KEY)")
        ID = 0
        for teamName, abbr in teams:
            print 'adding {}'.format(teamName)
            self.c.execute("INSERT INTO Teams VALUES('{}','{}',{})".format(teamName, abbr, ID))
            ID += 1
        self.closeCursor()

    def readTeams(self):
        self.createCursor()
        self.c.execute("SELECT * from Teams")
        teams = self.c.fetchall()
        self.closeCursor()
        return teams


