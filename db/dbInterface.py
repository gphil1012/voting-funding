"""
These are the interfaces that will be used
in order to interact with the database
"""
import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class OutgoingInterface(object):
    """
    This interface will be used by the server
    in order to generate the data to be used
    by the front end to display information to the user
    """
    # TODO these gets can be abstracted quite a bit
    def __init__(self, dbFilename, dbDriver=sqlite3):
        self.dbFilename = dbFilename
        self.dbDriver = dbDriver

    def openConnection(self):
        conn = self.dbDriver.connect(self.dbFilename)
        conn.row_factory = dict_factory
        return conn

    def closeConnection(self, conn):
        conn.commit()
        conn.close()

    def getAllCongressMembers(self):
        """
        returns a list of dicts of the form
        [{
            "name", "houseRep", "ID", "DOB"
        }]
        """
        c = self.openConnection()
        cur = c.cursor().execute("select * from congress")
        value = cur.fetchall()
        self.closeConnection(c)
        return value

    def getCongressMemberById(self, searchID):
        """
        returns a dict of a congress member of the form
        {"name", "houseRep", "ID", "DOB"}
        """
        c = self.openConnection()
        cur = c.cursor().execute("select * from congress where ID=?", (searchID,))
        value = cur.fetchone()
        self.closeConnection(c)
        return value
    
    def getAllDonations(self):
        c = self.openConnection()
        cur = c.cursor().execute("select * from funding")
        value = cur.fetchall()
        self.closeConnection(c)
        return value

    def getDonationById(self, searchID):
        c = self.openConnection()
        cur = c.cursor().execute("select * from funding where ID=?", (searchID,))
        value = cur.fetchone()
        self.closeConnection(c)
        return value

    def getDonationsByCongressId(self, searchID):
        c = self.openConnection()
        cur = c.cursor().execute("select * from funding where congress_ID=?", (searchID,))
        value = cur.fetchall()
        self.closeConnection(c)
        return value
    
    def getDonationsByOrganizationId(self, searchID):
        c = self.openConnection()
        cur = c.cursor().execute("select * from funding where organization_ID=?", (searchID,))
        value = cur.fetchall()
        self.closeConnection(c)
        return value

    def getVotesByCongressId(self, searchID):
        c = self.openConnection()
        cur = c.cursor().execute("select * from votes where congress_ID=?", (searchID,))
        value = cur.fetchall()
        self.closeConnection(c)
        return value

    def getVotesByBillId(self, searchID):
        c = self.openConnection()
        cur = c.cursor().execute("select * from votes where bill_ID=?", (searchID,))
        value = cur.fetchall()
        self.closeConnection(c)
        return value
    
    def getAllVotes(self):
        c = self.openConnection()
        cur = c.cursor().execute("select * from votes")
        value = cur.fetchall()
        self.closeConnection(c)
        return value

    def getAllBills(self):
        c = self.openConnection()
        cur = c.cursor().execute("select * from bills")
        value = cur.fetchall()
        self.closeConnection(c)
        return value
    
    def getBillByID(self, searchID):
        c = self.openConnection()
        cur = c.cursor().execute("select * from bills where ID=?", (searchID,))
        value = cur.fetchone()
        self.closeConnection(c)
        return value
    
    def getAllOrganizations(self):
        c = self.openConnection()
        cur = c.cursor().execute("select * from organizations")
        value = cur.fetchall()
        self.closeConnection(c)
        return value

    def getOrganizationById(self, searchID):
        c = self.openConnection()
        cur = c.cursor().execute("select * from organizations where ID=?", (searchID,))
        value = cur.fetchone()
        self.closeConnection(c)
        return value

class IncomingInterface(OutgoingInterface):
    """
    This interface will be used by the webscraper
    in order to update or add any new information to the database
    """
    def __init__(self, dbFilename, dbDriver=sqlite3):
        super(IncomingInterface, self).__init__(dbFilename, dbDriver)
        self.dbDriver = dbDriver
        self.dbFilename = dbFilename

    def addCongressMember(self, first_name, last_name, houseRep, dob, email=""):
        """
        first_name - string
        last_name - string
        houseRep - boolean
        dob - string dd-mm-yyyy
        """
        c = self.openConnection()
        c.cursor().execute("INSERT INTO congress (first_name, last_name, house_rep, dob, email) VALUES (?,?,?,?,?)", (first_name, last_name, houseRep, dob, email))
        self.closeConnection(c)

    def addDonation(self, congress_ID, org_ID, donation_amount, year):
        """
        congress_ID - int foreign key
        org_ID - int foreign key
        donation_amount - float $$$
        year - int
        """
        c = self.openConnection()
        c.cursor().execute("INSERT INTO funding (congress_ID, organization_ID, donation_amount, year) VALUES (?,?,?,?)", (congress_ID, org_ID, donation_amount, year))
        self.closeConnection(c)

    def addOrganization(self, orgName):
        c = self.openConnection()
        c.cursor().execute("INSERT INTO organizations (name) VALUES (?)", (orgName,))
        self.closeConnection(c)

    def addBill(self, billName, hyperlink, year):
        c = self.openConnection()
        c.cursor().execute("INSERT INTO bills (name, hyperlink, year) VALUES (?, ?, ?)", (billName, hyperlink, year))
        self.closeConnection(c)
    
    def addVote(self, conID, billID, vote):
        c = self.openConnection()
        c.cursor().execute("INSERT INTO votes (congress_ID, bill_ID, vote) VALUES (?, ?, ?)", (conID, billID, vote))
        self.closeConnection(c)
