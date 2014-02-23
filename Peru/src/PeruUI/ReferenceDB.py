import PeruConstants, PeruDB

def ReferenceInsertFromList(references):
    resultString = ""
    
    for reference in references:
        result = ReferenceInsertStatement(reference)
        if result == -1:
            return result
        resultString += result
    
    return resultString

def ReferenceReadSingleStatement(fields):    
    return("SELECT * FROM REFERENCE WHERE " + PeruConstants.REFERENCE_FIELDS[0] + " = " + fields[0] + ";\n")

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

def ReferenceUpdateStatement(fields):
    
    if len(fields) != len(PeruConstants.REFERENCE_FIELDS):
        return -1
    
    strFields = [(PeruConstants.REFERENCE_FIELDS[i] + ' = ' + str(fields[i])) for i in range(len(fields))]
    
    return ("UPDATE REFERENCE" +
            " SET " + ",".join(strFields) + 
            " WHERE " + PeruConstants.REFERENCE_FIELDS[0] + " = " + fields[0] + ";\n")

def ReferenceDeleteStatement(fields):    
    return("DELETE FROM REFERENCE WHERE " + PeruConstants.REFERENCE_FIELDS[0] + " = " + fields[0] + ";\n")

def ReadReference(fields):
    database = PeruDB.PeruDB()
    output = database.querry(ReferenceReadSingleStatement(fields));
    database.closeDB()
    return output
    
    
def InsertUpdateReference(fields):
    if fields[0] != '':
        InsertReference(fields)
    else:
        UpdateReference(fields)

def InsertReference(fields):
    database = PeruDB.PeruDB()
    output = database.insert(ReferenceInsertStatement(fields))
    database.closeDB()
    return output

def DeleteReference(fields):
    database = PeruDB.PeruDB()
    output = database.delete(ReferenceDeleteStatement(fields))
    database.closeDB()
    return output
    

def ReferenceUpdateStatement(fields):
    
    if len(fields) > len(PeruConstants.REFERENCE_FIELDS) or len(fields) < len(PeruConstants.REFERENCE_FIELDS) - 1:
        return -1
    
    strFields = [str(field) for field in fields]
    
    return "UPDATE " + PeruConstants.REFERENCE + " VALUES(" + ",".join(strFields) + ");\n"

def ReferenceReadStatement(ID):
    
    return "SELECT * FROM " + PeruConstants.REFERENCE + " WHERE ReferenceId = " + ID + ";\n"