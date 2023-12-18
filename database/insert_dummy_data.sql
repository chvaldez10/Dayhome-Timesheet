use DayHomeDatabase;

INSERT INTO Admin (AdminID, Password) 
VALUES ("spicyrice", "password");

INSERT INTO Provider (ProviderID, FirstName, LastName) 
VALUES ("spicyrice001", "spicy", "rice");

INSERT INTO Children (ChildrenID, FirstName, LastName, ProviderID) VALUES
("sweetrice001", "sweet", "rice", "spicyrice001"),
("sweetrice002", "sweet", "rice", "spicyrice001")
;

INSERT INTO CareBy (ProviderID, ChildrenID) 
VALUES
("spicyrice001", "sweetrice001"),
("spicyrice001", "sweetrice002")
;

INSERT INTO DailyLog (DateEntry, LoginTime, SignOutTime, TotalTime, Status, ChildrenID) VALUES
("2023-12-08", "08:13:00", "17:15:00", 9.03, "Attendance Recorded", "sweetrice001"),
("2023-12-08", "08:00:00", "16:00:00", 8, "Attendance Recorded", "sweetrice002")
;

INSERT INTO DailyLog (DateEntry, Status, ChildrenID) 
VALUES
("2023-12-09", "Not Scheduled", "sweetrice001"),
("2023-12-09", "Sick", "sweetrice002");

INSERT INTO ProviderLog (DateEntry, LoginTime, SignOutTime, TotalTime, Status, ProviderID) 
VALUES ("2023-12-08", "08:00:00", "17:30:00", 9.50, "Active", "spicyrice001");