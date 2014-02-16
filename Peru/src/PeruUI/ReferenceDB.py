import PeruConstants, PeruDB

def ReferenceInsertFromList(references):
    resultString = ""
    
    for reference in references:
        result = ReferenceInsertStatement(reference)
        if result == -1:
            return result
        resultString += result
    
    return resultString

def ReferenceInsertStatement(fields):
    
    if len(fields) > len(PeruConstants.REFERENCE_FIELDS) or len(fields) < (len(PeruConstants.REFERENCE_FIELDS) - 1):
        return -1
    
    strFields = [str(field) for field in fields]
    
    if len(fields) == (len(PeruConstants.REFERENCE_FIELDS) - 1):
        return ("INSERT INTO " + PeruConstants.REFERENCE + 
                "(" + ",".join(PeruConstants.REFERENCE_FIELDS[1:]) + ")" +
                " VALUES(" + ",".join(strFields) + ");\n")
    else:
        return "INSERT INTO " + PeruConstants.REFERENCE + " VALUES(" + ",".join(strFields) + ");\n"

def InsertReference(fields):
    database = PeruDB.PeruDB()
    database.executeInsert(ReferenceInsertStatement(fields))
    database.commit()
    database.closeDB()
    
    

def ReferenceUpdateStatement(fields):
    
    if len(fields) > len(PeruConstants.REFERENCE_FIELDS) or len(fields) < len(PeruConstants.REFERENCE_FIELDS) - 1:
        return -1
    
    strFields = [str(field) for field in fields]
    
    return "UPDATE " + PeruConstants.REFERENCE + " VALUES(" + ",".join(strFields) + ");\n"

def ReferenceReadStatement(ID):
    
    return "SELECT * FROM " + PeruConstants.REFERENCE + " WHERE ReferenceId = " + ID + ";\n"