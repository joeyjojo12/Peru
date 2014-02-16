#! /usr/bin/env python3.3
import sys

import sqlite3 as lite
import sys

try:
  
    con = lite.connect('Peru.db')
    
    cur = con.cursor()
    cur.executescript("""
  
        DROP TABLE IF EXISTS WitnessGroup;
        DROP TABLE IF EXISTS Witness;
        DROP TABLE IF EXISTS Official;
        DROP TABLE IF EXISTS CourtCase;
        DROP TABLE IF EXISTS HealingTypes;
        DROP TABLE IF EXISTS ProsecutorGroup;
        DROP TABLE IF EXISTS Prosecutor;
        DROP TABLE IF EXISTS DefendantGroup;
        DROP TABLE IF EXISTS Defendant;
        DROP TABLE IF EXISTS PlaintiffGroup;
        DROP TABLE IF EXISTS Plaintiff;
        DROP TABLE IF EXISTS GenderType;
        DROP TABLE IF EXISTS RegionType;
        DROP TABLE IF EXISTS ReferenceGroup;
        DROP TABLE IF EXISTS Reference;
      
        CREATE TABLE Reference(ReferenceId INTEGER PRIMARY KEY, 
                               Citation     TEXT, 
                               Archive      TEXT, 
                               Stack        TEXT, 
                               Number       INTEGER,
                               DocName      TEXT,
                               Author       TEXT,
                               Year         INTEGER,
                               Type         TEXT,
                               Notes        TEXT
        );
        
        CREATE TABLE ReferenceGroup(ReferenceGroupId INTEGER,
                                    ReferenceId      INTEGER NOT NULL,
                                    PRIMARY KEY(ReferenceGroupId, ReferenceId),
                                    FOREIGN KEY(ReferenceId) REFERENCES Reference(ReferenceId)
        );
        
        CREATE TABLE RegionType (Region    TEXT PRIMARY KEY NOT NULL,
                                 Seq       INTEGER
        );
        
        INSERT INTO RegionType(Region, Seq) VALUES ('Costal', 1);
        INSERT INTO RegionType(Region, Seq) VALUES ('Andes',  2);
        INSERT INTO RegionType(Region, Seq) VALUES ('Jungle', 3);
    
        CREATE TABLE GenderType (Gender    CHAR(1) PRIMARY KEY NOT NULL,
                                 Seq       INTEGER
        );
        
        INSERT INTO GenderType(Gender, Seq) VALUES ('M', 1);
        INSERT INTO GenderType(Gender, Seq) VALUES ('F', 2);
    
        CREATE TABLE Plaintiff(PlaintiffId   INTEGER PRIMARY KEY,
                               FristName   TEXT, 
                               LastName    TEXT,
                               Location    TEXT,
                               Region      REFERENCES RegionType(Region),
                               Gender      REFERENCES GenderType(Gender),
                               Age         INTEGER,
                               AgeRange    INTEGER,
                               Occupation  TEXT,
                               Religion    TEXT,
                               Notes       TEXT
        );
        
        CREATE TABLE PlaintiffGroup(PlaintiffGroupId INTEGER,
                                    PlaintiffId      INTEGER NOT NULL,
                                    PRIMARY KEY(PlaintiffGroupId, PlaintiffId),
                                    FOREIGN KEY(PlaintiffId) REFERENCES Plaintiff(PlaintiffId)
        );
        
        CREATE TABLE Defendant(DefendantId INTEGER PRIMARY KEY,
                               FristName   TEXT, 
                               LastName    TEXT,
                               Location    TEXT,
                               Region      REFERENCES RegionType(Region),
                               Gender      REFERENCES GenderType(Gender),
                               Age         INTEGER,
                               AgeRange    INTEGER,
                               Occupation  TEXT,
                               Religion    TEXT,
                               Notes       TEXT
        );
        
        CREATE TABLE DefendantGroup(DefendantGroupId INTEGER,
                                    DefendantId      INTEGER NOT NULL,
                                    PRIMARY KEY(DefendantGroupId, DefendantId),
                                    FOREIGN KEY(DefendantId) REFERENCES Defendant(DefendantId)
        );
        
        CREATE TABLE Witness(WitnessId INTEGER PRIMARY KEY,
                             FristName   TEXT, 
                             LastName    TEXT,
                             Location    TEXT,
                             Region      REFERENCES RegionType(Region),
                             Gender      REFERENCES GenderType(Gender),
                             Age         INTEGER,
                             AgeRange    INTEGER,
                             Occupation  TEXT,
                             Religion    TEXT,
                             Profession  TEXT,
                             Notes       TEXT
        );
        
        CREATE TABLE WitnessGroup(WitnessGroupId INTEGER,
                                  WitnessId      INTEGER NOT NULL,
                                  PRIMARY KEY(WitnessGroupId, WitnessId),
                                  FOREIGN KEY(WitnessId) REFERENCES Witness(WitnessId)
        );
        
        CREATE TABLE Prosecutor(ProsecutorId INTEGER PRIMARY KEY,
                                FristName   TEXT, 
                                LastName    TEXT,
                                Location    TEXT,
                                Region      REFERENCES RegionType(Region),
                                Gender      REFERENCES GenderType(Gender),
                                Age         INTEGER,
                                AgeRange    INTEGER,
                                Occupation  TEXT,
                                Religion    TEXT,
                                Notes       TEXT
        );
        
        CREATE TABLE ProsecutorGroup(ProsecutorGroupId INTEGER,
                                     ProsecutorId      INTEGER NOT NULL,
                                     PRIMARY KEY(ProsecutorGroupId, ProsecutorId),
                                     FOREIGN KEY(ProsecutorId) REFERENCES Prosecutor(ProsecutorId)
        );
        
        CREATE TABLE Official(OfficialId   INTEGER PRIMARY KEY,
                              FristName    TEXT, 
                              LastName     TEXT,
                              Title        TEXT,
                              Location     TEXT,
                              Region       REFERENCES RegionType(Region),
                              Gender       REFERENCES GenderType(Gender),
                              Age          INTEGER,
                              AgeRange     INTEGER,
                              Occupation   TEXT,
                              Religion     TEXT,
                              Notes        TEXT
        );
        
        CREATE TABLE HealingTypes(HealingTypesID INTEGER PRIMARY KEY,
                                  CourtCaseID    INTEGER NOT NULL,
                                  DefendantID    INTEGER NOT NULL,
                                  Divination     BOOLEAN,
                                  Healing        BOOLEAN,
                                  Herbs          BOOLEAN,
                                  Psychology     BOOLEAN,
                                  Rituals        BOOLEAN,
                                  Sacrifices     BOOLEAN,
                                  Libations      BOOLEAN,
                                  Witchcraft     BOOLEAN,
                                  Other          TEXT,
                                  FOREIGN KEY(CourtCaseID) REFERENCES CourtCase(CourtCaseID),
                                  FOREIGN KEY(DefendantID) REFERENCES Defendant(DefendantID)
        );
        
        CREATE TABLE CourtCase(CourtCaseId          INTEGER PRIMARY KEY,
                               StartDate            DATE,
                               EndDate              DATE,
                               ReferenceGroupID     INTEGER,
                               PlaintiffGroupID     INTEGER,
                               DefendantGroupID     INTEGER,
                               ProsecutorGroupID    INTEGER,
                               WitnessGroupID       INTEGER,
                               Charges              TEXT,
                               Summary              TEXT,
                               CaseNotes            TEXT,
                               FurtherResearchNotes TEXT,
                               HealingNotes         TEXT,
                               FOREIGN KEY(ReferenceGroupID)  REFERENCES ReferenceGroup(ReferenceGroupID),
                               FOREIGN KEY(PlaintiffGroupID)  REFERENCES PlaintiffGroup(PlaintiffGroupID),
                               FOREIGN KEY(DefendantGroupID)  REFERENCES DefendantGroup(DefendantGroupID),
                               FOREIGN KEY(ProsecutorGroupID) REFERENCES ProsecutorGroup(ProsecutorGroupID),
                               FOREIGN KEY(WitnessGroupID)    REFERENCES WitnessGroup(WitnessGroupID)
        );
        
        """)
    
    con.commit()
    
except lite.Error as e:
  
    if con:
        con.rollback()
      
    print("Error %s:" % e.args[0])
    sys.exit(1)

finally:
  
    if con:
        con.close()
