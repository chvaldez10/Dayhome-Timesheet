# Note: dropping the database and tables will results data loss
CREATE DATABASE IF NOT EXISTS DayHomeDatabase;
USE DayHomeDatabase;

CREATE TABLE Admin(
    AdminID VARCHAR(25) PRIMARY KEY,
    Password VARCHAR(255) NOT NULL
);

CREATE TABLE Provider(
    ProviderID VARCHAR(25) PRIMARY KEY,
    FirstName VARCHAR(25) NOT NULL,
    LastName VARCHAR(25) NOT NULL,
    Location VARCHAR(25) NOT NULL UNIQUE
);

CREATE TABLE Children(
    ChildrenID VARCHAR(25) PRIMARY KEY,
    FirstName VARCHAR(25) NOT NULL,
    LastName VARCHAR(25) NOT NULL,
    ProviderID VARCHAR(25),
    FOREIGN KEY (ProviderID) REFERENCES Provider(ProviderID)
);

CREATE TABLE DailyLog(
    DateEntry DATE NOT NULL,
    SignInTime TIME,
    SignOutTime TIME,
    TotalTime FLOAT(4,2) NOT NULL,
    Status VARCHAR(25),
    ChildrenID VARCHAR(25) NOT NULL,
    Location VARCHAR(25),
    HealthCheck VARCHAR(25),
    PRIMARY KEY (DateEntry, ChildrenID),
    FOREIGN KEY (ChildrenID) REFERENCES Children(ChildrenID)
);

CREATE TABLE ProviderLog(
    DateEntry DATE NOT NULL,
    SignInTime TIME,
    SignOutTime TIME,
    TotalTime FLOAT(4,2) NOT NULL,
    ProviderID VARCHAR(25) NOT NULL,
    PRIMARY KEY (DateEntry, ProviderID),
    FOREIGN KEY (ProviderID) REFERENCES Provider(ProviderID)
);

# Indexes for optimization
CREATE INDEX idx_dailylog_childrenid ON DailyLog (ChildrenID);
CREATE INDEX idx_providerlog_providerid ON ProviderLog (ProviderID);