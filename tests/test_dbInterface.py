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
        print "seems to build"

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
    
    def test_addDonation(self):
        pass

    def test_getAllDonations(self):
        pass
    
    def test_getDonationsByOrganization(self):
        pass

    def test_getDonationsByCongressId(self):
        pass
    
    def test_getDonationById(self):
        pass

    pass

class TestVotesTable(unittest.TestCase):
    pass

class TestBillsTable(unittest.TestCase):
    pass

class TestOrganizationsTable(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
