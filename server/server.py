"""
http server for getting JSON info to fill in the spots on the frontend
"""
from flask import Flask, jsonify
from flask_restful import reqparse
from flask_cors import CORS
import sys
sys.path.append("../db/")
import dbInterface

dbName = "../db/zionMainframe.db"
db = dbInterface.IncomingInterface(dbName)
app = Flask(__name__)
CORS(app)

@app.route("/")
def siteInfo():
    pass

@app.route("/congress/")
def getAllCongressPeople():
    """
    return a json list of form
    [
        {
            -first_name
            -last_name
            -dob
            -houseRep
            -fundingReceived [
                - amount
                - organization
                - year
            ]
            -billsVotedOn [
                {
                    - bill name
                    - link
                    - year
                    - vote
                }
            ]
        }
    ]
    """
    result = []
    congressPeople = db.getAllCongressMembers()
    for person in congressPeople:
        donations = db.getDonationsByCongressId(person['ID'])
        tmp = []
        if donations:
            for each in donations:
                each['organization'] = db.getOrganizationById(each['organization_ID'])
                tmp.append(each)
        
        donations = tmp
        votes = db.getVotesByCongressId(person['ID'])
        tmp = []
        if votes:
            for each in votes:
                each['bill'] = db.getBillByID(each['bill_ID'])
                tmp.append(each)

        votes = tmp
        person['votes'] = votes
        person['donations'] = donations
        result.append(person)
    
    return jsonify({"data": result})

@app.route("/orgs/")
def getAllOrganizations():
    pass

@app.route("/bills/")
def getAllBills():
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port='8080')