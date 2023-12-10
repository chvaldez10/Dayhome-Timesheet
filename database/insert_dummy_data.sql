INSERT INTO Admin (Username, Password) 
VALUES ('adminUser', 'hashedPassword123');

INSERT INTO Provider (ProviderID, FirstName, LastName) 
VALUES ('Provider001', 'John', 'Doe');

INSERT INTO Children (ChildrenID, FirstName, LastName, ProviderID) 
VALUES ('Child001', 'Alice', 'Smith', 'Provider001');

INSERT INTO CareBy (ProviderID, ChildrenID) 
VALUES ('Provider001', 'Child001');

INSERT INTO DailyLog (DateEntry, LoginTime, SignOutTime, TotalTime, Status, ChildrenID) 
VALUES ('2023-12-08', '08:13:00', '17:15:00', 9.03, 'Attendance Recorded', 'Child001');

INSERT INTO ProviderLog (DateEntry, LoginTime, SignOutTime, TotalTime, Status, ProviderID) 
VALUES ('2023-12-08', '08:00:00', '17:30:00', 9.50, 'Active', 'Provider001');
