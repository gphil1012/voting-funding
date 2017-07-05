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
        pass

    def getDonationById(self, seachID):
        pass

    def getDonationsByCongressId(self, searchID):
        pass
    
    def getDonationsByOrganizationId(self, searchID):
        pass

    def getVotesByCongressId(self, searchID):
        pass

    def getVotesByBillId(self, searchID):
        pass
    
    def getAllBills(self):
        pass
    
    def getBillByID(self, searchID):
        pass

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

    def addOrganization(self):
        pass

    def addBill(self):
        pass
    
    def addVote(self):
        pass
