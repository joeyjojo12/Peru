import PeruConstants

def OfficialInsert(fields):
    
    if len(fields) > len(PeruConstants.OFFICIAL_FIELDS) or len(fields) < len(PeruConstants.OFFICIAL_FIELDS) - 1:
        return -1
    
    strFields = [str(field) for field in fields]
    
    return "INSERT INTO Official VALUES(" + ",".join(strFields) + ");\n"


def OfficialUpdate(fields):
    
    if len(fields) != len(PeruConstants.OFFICIAL_FIELDS):
        return -1
    
    strFields = [str(field) for field in fields]
    
    return "INSERT INTO Official VALUES(" + ",".join(strFields) + ");\n"