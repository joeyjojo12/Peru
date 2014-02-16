import PeruConstants, PeruDB

def PlaintiffInsertFromList(plaintiffs):
    resultString = ""
    
    for plaintiff in plaintiffs:
        result = PlaintiffInsertStatement(plaintiff)
        if result == -1:
            return result
        resultString += result
    
    return resultString

def PlaintiffInsertStatement(fields):
    
    if len(fields) > len(PeruConstants.PLAINTIFF_FIELDS) or len(fields) < (len(PeruConstants.PLAINTIFF_FIELDS) - 1):
        return -1
    
    strFields = [str(field) for field in fields]
    
    if len(fields) == (len(PeruConstants.PLAINTIFF_FIELDS) - 1):
        return ("INSERT INTO " + PeruConstants.PLAINTIFF + 
                "(" + ",".join(PeruConstants.PLAINTIFF_FIELDS[1:]) + ")" +
                " VALUES(" + ",".join(strFields) + ");\n")
    else:
        return "INSERT INTO " + PeruConstants.PLAINTIFF + " VALUES(" + ",".join(strFields) + ");\n"

def InsertPlaintiff(fields):
    database = PeruDB.PeruDB()
    database.executeInsert(PlaintiffInsertStatement(fields))
    database.commit()
    database.closeDB()
    
    

def PlaintiffUpdateStatement(fields):
    
    if len(fields) > len(PeruConstants.PLAINTIFF_FIELDS) or len(fields) < len(PeruConstants.PLAINTIFF_FIELDS) - 1:
        return -1
    
    strFields = [str(field) for field in fields]
    
    return "UPDATE " + PeruConstants.PLAINTIFF + " VALUES(" + ",".join(strFields) + ");\n"

def PlaintiffReadStatement(ID):
    
    return "SELECT * FROM " + PeruConstants.PLAINTIFF + " WHERE PlaintiffId = " + ID + ";\n"