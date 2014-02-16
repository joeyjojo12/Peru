import PeruConstants, PeruDB

def ProsecutorInsertFromList(prosecutors):
    resultString = ""
    
    for prosecutor in prosecutors:
        result = ProsecutorInsertStatement(prosecutor)
        if result == -1:
            return result
        resultString += result
    
    return resultString

def ProsecutorInsertStatement(fields):
    
    if len(fields) > len(PeruConstants.PROSECUTOR_FIELDS) or len(fields) < (len(PeruConstants.PROSECUTOR_FIELDS) - 1):
        return -1
    
    strFields = [str(field) for field in fields]
    
    if len(fields) == (len(PeruConstants.PROSECUTOR_FIELDS) - 1):
        return ("INSERT INTO " + PeruConstants.PROSECUTOR + 
                "(" + ",".join(PeruConstants.PROSECUTOR_FIELDS[1:]) + ")" +
                " VALUES(" + ",".join(strFields) + ");\n")
    else:
        return "INSERT INTO " + PeruConstants.PROSECUTOR + " VALUES(" + ",".join(strFields) + ");\n"

def InsertProsecutor(fields):
    database = PeruDB.PeruDB()
    database.executeInsert(ProsecutorInsertStatement(fields))
    database.commit()
    database.closeDB()
    
    

def ProsecutorUpdateStatement(fields):
    
    if len(fields) > len(PeruConstants.PROSECUTOR_FIELDS) or len(fields) < len(PeruConstants.PROSECUTOR_FIELDS) - 1:
        return -1
    
    strFields = [str(field) for field in fields]
    
    return "UPDATE " + PeruConstants.PROSECUTOR + " VALUES(" + ",".join(strFields) + ");\n"

def ProsecutorReadStatement(ID):
    
    return "SELECT * FROM " + PeruConstants.PROSECUTOR + " WHERE ProsecutorId = " + ID + ";\n"