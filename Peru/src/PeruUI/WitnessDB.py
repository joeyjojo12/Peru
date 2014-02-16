import PeruConstants, PeruDB

def WitnessInsertFromList(witnesses):
    resultString = ""
    
    for witness in witnesses:
        result = WitnessInsertStatement(witness)
        if result == -1:
            return result
        resultString += result
    
    return resultString

def WitnessInsertStatement(fields):
    
    if len(fields) > len(PeruConstants.WITNESS_FIELDS) or len(fields) < (len(PeruConstants.WITNESS_FIELDS) - 1):
        return -1
    
    strFields = [str(field) for field in fields]
    
    if len(fields) == (len(PeruConstants.WITNESS_FIELDS) - 1):
        return ("INSERT INTO " + PeruConstants.WITNESS + 
                "(" + ",".join(PeruConstants.WITNESS_FIELDS[1:]) + ")" +
                " VALUES(" + ",".join(strFields) + ");\n")
    else:
        return "INSERT INTO " + PeruConstants.WITNESS + " VALUES(" + ",".join(strFields) + ");\n"

def InsertWitness(fields):
    database = PeruDB.PeruDB()
    database.executeInsert(WitnessInsertStatement(fields))
    database.commit()
    database.closeDB()
    
    

def WitnessUpdateStatement(fields):
    
    if len(fields) > len(PeruConstants.WITNESS_FIELDS) or len(fields) < len(PeruConstants.WITNESS_FIELDS) - 1:
        return -1
    
    strFields = [str(field) for field in fields]
    
    return "UPDATE " + PeruConstants.WITNESS + " VALUES(" + ",".join(strFields) + ");\n"

def WitnessReadStatement(ID):
    
    return "SELECT * FROM " + PeruConstants.WITNESS + " WHERE WitnessId = " + ID + ";\n"