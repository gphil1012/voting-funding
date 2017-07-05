"""
These are the interfaces that will be used
in order to interact with the database
"""
class OutgoingInterface(object):
    """
    This interface will be used by the server
    in order to generate the data to be used
    by the front end to display information to the user
    """
    def __init__(self, dbFilename):
        pass

    def getAllCongressMembers(self):
        """
        returns a list of dicts of the form
        [{
            "name", "houseRep", "ID", "DOB"
        }]
        """
        pass

    def getCongressMemberById(self, searchID):
        pass
    
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
    def __init__(self, dbFilename):
        super(IncomingInterface, self).__init__(dbFilename)

    def addCongressMember(self):
        pass

    def addDonation(self):
        pass

    def addOrganization(self):
        pass

    def addBill(self):
        pass
    
    def addVote(self):
        pass
