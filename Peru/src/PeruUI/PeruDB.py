import sqlite3 as lite
import sys
import PeruConstants

class PeruDB:
    
    con = None
    
    def __init__(self):
        self.openDB()
    
    def openDB(self):
        try:
            self.con = lite.connect(PeruConstants.PERU_DB)
            cur = self.con.cursor()
            cur.execute('SELECT SQLITE_VERSION()')
            data = cur.fetchone()
            print "SQLite version: %s" % data
    
        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)
        
    
    def closeDB(self):        
        if self.con:
            self.con.close()
    
    def executeInsert(self, statement):
        try:
            cur = self.con.cursor()
            cur.execute(statement)
        
        except lite.Error, e:
            print "Error %s:" % e.args[0]
            return -1
    
    def commit(self):
        if self.con:
            self.con.commit()