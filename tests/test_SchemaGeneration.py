"""
Test client for generating database
from schema
"""
import sqlite3
import os

dbDir = "../db/zionMainframe.db"
schemaDir = "../db/schema.sql"
with open(schemaDir) as f:
    sqlCommand = f.read()

sqlCommands = sqlCommand.split(";")

if not os.path.isfile(dbDir):
    open(dbDir, "w+").close()

conn = sqlite3.connect(dbDir)
c = conn.cursor()
for each in sqlCommands:
    # this fails if the db already exists
    try:
        c.execute(each+";")
    except:
        # I'm an awful person
        pass

# todo add some check to
# confirm that the correct columns
# are present