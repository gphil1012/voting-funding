"""
test suite for the dbInterface module
"""
import sys
import unittest
import hypothesis
from hypothesis import given, strategies as st
sys.path.append("../db/")
import dbInterface
from datetime import date
import random

testDb = "../db/zionMainframe.db"

class TestGeneral(unittest.TestCase):
    def setup(self):
        dbOut = dbInterface.OutgoingInterface(testDb)
        dbIn = dbInterface.IncomingInterface(testDb)

    def test_Build(self):
        a = "seems to build"

class TestCongressTable(unittest.TestCase):
    def setUp(self):
        self.inDb = dbInterface.IncomingInterface(testDb)
        self.outDb = dbInterface.OutgoingInterface(testDb)
    
    @given(name=st.text(), houseRep=st.booleans(), email=st.text())
    def test_addingCongressMember(self, name, houseRep, email):
        dob = date(1969, 6, 9).strftime("%x")
        self.inDb.addCongressMember(name, name, houseRep, dob, email)

    def test_getAllCongressMembers(self):
        a = self.inDb.getAllCongressMembers()
    
    def test_getCongressMemberById(self):
        a = random.choice(self.inDb.getAllCongressMembers())
        self.inDb.getCongressMemberById(a['ID'])

class TestFundingTable(unittest.TestCase):
    def setUp(self):
        self.inDb = dbInterface.IncomingInterface(testDb)
        self.outDb = dbInterface.OutgoingInterface(testDb)
    
    @given(donation_amount=st.floats(), year=st.integers(min_value=1900, max_value=3005))
    def test_addDonation(self, donation_amount, year):
        conID = random.choice(self.inDb.getAllCongressMembers())['ID']
        orgID = random.choice(self.inDb.getAllOrganizations())['ID']
        self.inDb.addDonation(conID, orgID, donation_amount, year)

    def test_getAllDonations(self):
        assert self.inDb.getAllDonations() is not None
    
    def test_getDonationsByOrganization(self):
        orgID = random.choice(self.inDb.getAllOrganizations())['ID']
        self.inDb.getDonationsByOrganizationId(orgID)

    def test_getDonationsByCongressId(self):
        conId = random.choice(self.inDb.getAllCongressMembers())['ID']
        self.inDb.getDonationsByCongressId(conId)
    
    def test_getDonationById(self):
        donID = random.choice(self.inDb.getAllDonations())['ID']
        assert self.inDb.getDonationById(donID) is not None


class TestVotesTable(unittest.TestCase):
    def setUp(self):
        self.inDb = dbInterface.IncomingInterface(testDb)
    
    @given(vote=st.integers(min_value=-1, max_value=1))
    def test_addVote(self, vote):
        conID = random.choice(self.inDb.getAllCongressMembers())['ID']
        billID = random.choice(self.inDb.getAllBills())['ID']
        self.inDb.addVote(conID, billID, vote)    

    def test_getVotesByCongress(self):
        conID = random.choice(self.inDb.getAllCongressMembers())['ID']
        self.inDb.getVotesByCongressId(conID)
    
    def test_getVotesByBill(self):
        billID = random.choice(self.inDb.getAllBills())['ID']
        self.inDb.getVotesByBillId(billID)

    def test_getAllVotes(self):
        assert self.inDb.getAllVotes() is not None

class TestBillsTable(unittest.TestCase):
    def setUp(self):
        self.inDb = dbInterface.IncomingInterface(testDb)
    
    @given(name=st.text(), hyperlink=st.text(), year=st.integers(min_value=1900, max_value=3005))
    def test_addBill(self, name, hyperlink, year):
        self.inDb.addBill(name, hyperlink, year)

    def test_getAllBills(self):
        self.inDb.getAllBills()

    def test_getBillById(self):
        billID = random.choice(self.inDb.getAllBills())['ID']
        assert self.inDb.getBillByID(billID) is not None

class TestOrganizationsTable(unittest.TestCase):
    def setUp(self):
        self.inDb = dbInterface.IncomingInterface(testDb)
        self.outDb = dbInterface.OutgoingInterface(testDb)

    @given(name=st.text())
    def test_addOrganization(self, name):
        self.inDb.addOrganization(name)
    
    def test_getAllOrganizations(self):
        assert self.inDb.getAllOrganizations() is not None

    def test_getOrganizationById(self):
        orgID = random.choice(self.inDb.getAllOrganizations())['ID']
        assert self.inDb.getOrganizationById(orgID) is not None

if __name__ == '__main__':
    unittest.main()
