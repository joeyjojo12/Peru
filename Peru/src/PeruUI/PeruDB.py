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
    
    def querry(self, querryString):
        try:
            cur = self.con.cursor()
            cur.execute(querryString)
            return [0, cur.fetchall()]
        
        except lite.Error, e:
            return [1, "Error %s:" % e.args[0]]
            
        except:
            return [1, "Unexpected Error!"]

    def executeCommand(self, commandString):
        try:
            cur = self.con.cursor()
            cur.execute(commandString)
            self.con.commit()
            return[0, cur.rowcount]
        
        except lite.Error, e:
            return [1, "Error %s:" % e.args[0]]

    def insert(self, commandString):
        return self.executeCommand(commandString)            

    def update(self, commandString):
        return self.executeCommand(commandString)

    def delete(self, commandString):
        return self.executeCommand(commandString)