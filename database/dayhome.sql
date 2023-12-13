# Note: dropping the database and tables will results data loss
CREATE DATABASE DayHomeDatabase;
USE DayHomeDatabase;

CREATE TABLE Admin(
    AdminID INT AUTO_INCREMENT PRIMARY KEY,
    Username VARCHAR(25),
    Password VARCHAR(60)
);

CREATE TABLE Provider(
    ProviderID VARCHAR(25) PRIMARY KEY,
    FirstName VARCHAR(25),
    LastName VARCHAR(25)
);

CREATE TABLE Children(
    ChildrenID VARCHAR(25) PRIMARY KEY,
    FirstName VARCHAR(25),
    LastName VARCHAR(25),
    ProviderID VARCHAR(25),
    FOREIGN KEY (ProviderID) REFERENCES Provider(ProviderID)
);

CREATE TABLE CareBy(
    ProviderID VARCHAR(25),
    ChildrenID VARCHAR(25),
    PRIMARY KEY (ProviderID, ChildrenID),
    FOREIGN KEY (ProviderID) REFERENCES Provider(ProviderID),
    FOREIGN KEY (ChildrenID) REFERENCES Children(ChildrenID)
);

CREATE TABLE DailyLog(
    LogID INT AUTO_INCREMENT PRIMARY KEY,
    DateEntry DATE NOT NULL,
    LoginTime TIME,
    SignOutTime TIME,
    TotalTime FLOAT(4,2),
    Status VARCHAR(25),
    ChildrenID VARCHAR(25) NOT NULL,
    Location VARCHAR(25),
    HealthCheck VARCHAR(25),
    FOREIGN KEY (ChildrenID) REFERENCES Children(ChildrenID)
);

CREATE TABLE ProviderLog(
    LogID INT AUTO_INCREMENT PRIMARY KEY,
    DateEntry DATE NOT NULL,
    LoginTime TIME,
    SignOutTime TIME,
    TotalTime FLOAT(4,2),
    Status VARCHAR(25),
    ProviderID VARCHAR(25) NOT NULL,
    FOREIGN KEY (ProviderID) REFERENCES Provider(ProviderID)
);